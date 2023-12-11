import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import argparse
import grpc
import reddit_pb2
import reddit_pb2_grpc

class RedditClient:
    def __init__(self, host='localhost', port=40000):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = reddit_pb2_grpc.RedditServiceStub(self.channel)

    def create_post(self, post_data):
        post = reddit_pb2.CreatePostRequest(
            title= post_data["title"],
            text= post_data["text"],
            image_url= "/path/to/image.img"
        )
        if "author" in post_data: post.author = reddit_pb2.User(userID=post_data["author"])
        if "video_url" in post_data: post.video_url = post_data["video_url"]
        elif "image_url" in post_data: post.image_url = post_data["image_url"]

        response = self.stub.CreatePost(post)
        return response
    
    def vote_post(self, post_id, isUpvote):
        vote = reddit_pb2.UPVOTE if isUpvote else reddit_pb2.DOWNVOTE
        request = reddit_pb2.VotePostRequest(post_id=post_id, vote_type=vote)
        response = self.stub.VotePost(request)
        return response
    
    def get_post(self, post_id: int):
        request = reddit_pb2.GetPostRequest(post_id=post_id)
        response = self.stub.GetPost(request)
        return response
    
    def create_comment(self, comment_data):
        comment = reddit_pb2.CreateCommentRequest(
            author=reddit_pb2.User(userID=comment_data["author"]),
            text=comment_data["text"]
        )

        if "comment_id" in comment_data: comment.comment_id = comment_data["comment_id"]
        elif "post_id" in comment_data: comment.post_id = comment_data["post_id"]

        response = self.stub.CreateComment(comment)
        return response
    
    def vote_comment(self, comment_id, isUpvote):
        vote = reddit_pb2.UPVOTE if isUpvote else reddit_pb2.DOWNVOTE
        request = reddit_pb2.VoteCommentRequest(comment_id=comment_id, vote_type=vote)
        response = self.stub.VoteComment(request)
        return response
    
    def get_top_comments(self, post_id, N):
        request = reddit_pb2.GetTopCommentsRequest(post_id=post_id, N=N)
        response = self.stub.GetTopComments(request)
        return response
    
    def expand_comment_branch(self, comment_id, N):
        request = reddit_pb2.ExpandCommentBranchRequest(comment_id=comment_id, N=N)
        response = self.stub.ExpandCommentBranch(request)
        return response

# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--host', default='localhost')
#     parser.add_argument('--port', type=int, default=40000)
#     args = parser.parse_args()
#     client = RedditClient(args.host, args.port)

#     # Create a Post
#     print("============ Create a post ============")
#     post_data = {
#         "title": "Post123",
#         "text": "post post post",
#         "image_url": "/path/to/image.img",
#         # "author": 'cindy2'
#     }
#     print(client.create_post(post_data))

#     # Upvote or downvote a Post
#     print("============ Upvote or downvote a Post ============")
#     print(client.vote_post(0, False))

#     # Retrieve Post content
#     print("============ Retrieve Post content ============")
#     post = client.get_post(0)
#     print(post)

#     # Create a Comment
    # print("============ Create a Comment ============")
    # comment_data = {
    #     "post_id":0,
    #     "author":"cindy",
    #     "text":"hello"
    # }
    # comment_rsp = client.create_comment(comment_data)
    # print(comment_rsp)

#     # Upvote or downvote a Comment
#     print("============ Upvote or downvote a Comment ============")
#     print(client.vote_comment(0, True))

#     # Retrieving a list of N most upvoted comments under a post
#     print("============ Retrieving a list of N most upvoted comments under a post ============")
#     top_comments = client.get_top_comments(0, 2)
#     print(top_comments)

#     # Expand a comment branch
#     print("============ Expand a comment branch ============")
#     expanded_comments = client.expand_comment_branch(0, 5)
#     print(expanded_comments)

# if __name__ == '__main__':
#     main()
