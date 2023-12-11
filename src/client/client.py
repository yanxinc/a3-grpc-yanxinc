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

    def create_post(self, post_req):
        response = self.stub.CreatePost(post_req)
        return response
    
    def vote_post(self, post_id, vote_type):
        request = reddit_pb2.VotePostRequest(post_id=post_id, vote_type=vote_type)
        response = self.stub.VotePost(request)
        return response
    
    def get_post(self, post_id: int):
        request = reddit_pb2.GetPostRequest(post_id=post_id)
        response = self.stub.GetPost(request)
        return response
    
    def create_comment(self, comment_req):
        response = self.stub.CreateComment(comment_req)
        return response
    
    def vote_comment(self, comment_id, vote_type):
        request = reddit_pb2.VoteCommentRequest(comment_id=comment_id, vote_type=vote_type)
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
#     post = reddit_pb2.CreatePostRequest(
#         title= "Post1",
#         # author= reddit_pb2.User(userID="cindy2"),
#         text= "My first Post",
#         image_url= "/path/to/image.img")
#     client.create_post(post)

#     # Upvote or downvote a Post
#     print("============ Upvote or downvote a Post ============")
#     client.vote_post(0, reddit_pb2.DOWNVOTE)

#     # Retrieve Post content
#     print("============ Retrieve Post content ============")
#     post = client.get_post(0)
#     print(post)

#     # Create a Comment
#     print("============ Create a Comment ============")
#     comment = reddit_pb2.CreateCommentRequest(
#         post_id=0,
#         author=reddit_pb2.User(userID="cindy"),
#         text="hello"
#     )
#     comment_rsp = client.create_comment(comment)
#     print(comment_rsp)

#     # Upvote or downvote a Comment
#     print("============ Upvote or downvote a Comment ============")
#     client.vote_comment(0, reddit_pb2.UPVOTE)

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
