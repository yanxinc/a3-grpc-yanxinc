import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import argparse
import grpc
from concurrent import futures
import reddit_pb2
import reddit_pb2_grpc
from datetime import datetime
import db



class RedditService(reddit_pb2_grpc.RedditServiceServicer):
    def __init__(self):
        self.posts = db.posts
        self.post_id_tracker = len(db.posts)
        self.comments = db.comments
        self.comment_id_tracker = len(db.comments)
        self.subreddits = db.subreddits

    def CreatePost(self, request, context):
        post_id = self.post_id_tracker
        self.post_id_tracker += 1

        post = reddit_pb2.Post(
            title=request.title,
            text=request.text,
            score=0,
            state=reddit_pb2.Post.NORMAL,
            publication_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        if request.HasField("video_url"): post.video_url = request.video_url
        elif request.HasField("image_url"): post.image_url = request.image_url

        if request.HasField("author"): post.author.CopyFrom(request.author)
        if request.HasField("subreddit_id"): 
            if request.subreddit_id not in self.subreddits:
                context.abort(grpc.StatusCode.NOT_FOUND, "Subreddit not found")
            post.subreddit_id = request.subreddit_id       
            for tag in self.subreddits[request.subreddit_id].tags:
                post.tags.append(tag)

        self.posts[post_id] = post
    
        return reddit_pb2.CreatePostResponse(post_id=post_id, post=post)
    
    def VotePost(self, request, context):
        post_id = request.post_id

        if post_id not in self.posts:
            context.abort(grpc.StatusCode.NOT_FOUND, "Post not found")

        if request.vote_type == reddit_pb2.VoteType.UPVOTE:
            self.posts[post_id].score += 1
        elif request.vote_type == reddit_pb2.VoteType.DOWNVOTE:
            self.posts[post_id].score -= 1

        return reddit_pb2.VotePostResponse(score=self.posts[post_id].score)
    
    def GetPost(self, request, context):
        post_id = request.post_id

        if post_id not in self.posts:
            context.abort(grpc.StatusCode.NOT_FOUND, "Post not found")

        return reddit_pb2.GetPostResponse(post=self.posts[post_id])
    
    def CreateComment(self, request, context):
        comment_id = self.comment_id_tracker
        self.comment_id_tracker += 1

        comment = reddit_pb2.Comment(
            id=comment_id,
            author=request.author,
            text=request.text,
            score=0,
            state=reddit_pb2.Post.NORMAL,
            publication_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            has_replies=False
        )

        if request.HasField("comment_id"): 
            comment.comment_id = request.comment_id
            self.comments[request.comment_id].has_replies = True
        elif request.HasField("post_id"):
            comment.post_id = request.post_id

        self.comments[comment_id] = comment

        return reddit_pb2.CreateCommentResponse(comment_id=comment_id, comment=comment)
    
    def VoteComment(self, request, context):
        comment_id = request.comment_id

        if comment_id not in self.comments:
            context.abort(grpc.StatusCode.NOT_FOUND, "Comment not found")

        if request.vote_type == reddit_pb2.VoteType.UPVOTE:
            self.comments[comment_id].score += 1
        elif request.vote_type == reddit_pb2.VoteType.DOWNVOTE:
            self.comments[comment_id].score -= 1

        return reddit_pb2.VoteCommentResponse(score=self.comments[comment_id].score)

    def GetTopComments(self, request, context):
        N = request.N
        post_id = request.post_id

        post_comments = [c for c in self.comments.values() if c.HasField('post_id') and c.post_id == post_id]
        top_comments = sorted(post_comments, key=lambda x: x.score, reverse=True)[:N]

        response = reddit_pb2.GetTopCommentsResponse(comments=top_comments)
        return response
    
    def expand_comment_helper(self, comment_id, N):
        comments = [c for c in self.comments.values() if c.HasField('comment_id') and c.comment_id == comment_id]
        return sorted(comments, key=lambda x: x.score, reverse=True)[:N]
    
    def ExpandCommentBranch(self, request, context):
        N = request.N
        comment_id = request.comment_id

        comments = self.expand_comment_helper(comment_id, N)

        response = reddit_pb2.ExpandCommentBranchResponse()

        for comment in comments:
            comment_with_replies = response.comments.add()
            comment_with_replies.comment.CopyFrom(comment)
            comment_with_replies.top_replies.extend(self.expand_comment_helper(comment.id, N))
        return response
        
class RedditServer:
    def start(self, host, port):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        reddit_pb2_grpc.add_RedditServiceServicer_to_server(RedditService(), server)
        server.add_insecure_port(f'{host}:{port}')
        server.start()
        server.wait_for_termination()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', type=int, default=40000)
    args = parser.parse_args()

    server = RedditServer()
    print(f"Starting server at {args.host}:{args.port}")
    server.start(args.host, args.port)

if __name__ == "__main__":
    main()