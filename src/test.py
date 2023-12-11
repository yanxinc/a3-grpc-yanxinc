import unittest
from unittest.mock import MagicMock
import reddit_pb2
# from client import RedditClient

def retrieve_post(client, post_id):
    response = client.get_post(post_id)
    if not response or not hasattr(response, 'post'):
        return None
    return response.post

def retrieve_most_upvoted_comments(client, post_id, N):
    response = client.get_top_comments(post_id, N)
    if not response or not hasattr(response, 'comments'):
        return None
    return response.comments

def expand_most_upvoted_comment(client, post_id, N):
    most_upvoted_comments = client.get_top_comments(post_id, 1)
    if not most_upvoted_comments or len(most_upvoted_comments.comments) < 1:
        return None

    most_upvoted_comment_id = most_upvoted_comments.comments[0].id
    expanded_comment_branch = client.expand_comment_branch(most_upvoted_comment_id, N)
    
    if not expanded_comment_branch or not hasattr(expanded_comment_branch, 'comments'):
        return None
    return expanded_comment_branch.comments

def most_upvoted_reply_under_most_upvoted_comment(client, post_id):
    most_upvoted_comments = client.get_top_comments(post_id, 1)
    if not most_upvoted_comments or len(most_upvoted_comments.comments) < 1:
        return None
    most_upvoted_comment_id = most_upvoted_comments.comments[0].id
    expanded_comment_branch = client.expand_comment_branch(most_upvoted_comment_id, 1)
    if not expanded_comment_branch or not hasattr(expanded_comment_branch, 'comments') or len(expanded_comment_branch.comments) < 1:
        return None

    sorted_comments = sorted(expanded_comment_branch.comments, key=lambda x: x.comment.score, reverse=True)
    return sorted_comments[0].comment

class TestReddit(unittest.TestCase):
    def setUp(self):
        self.post_id = 0
        self.mock_client = MagicMock()
        self.mock_client.get_post.return_value = reddit_pb2.CreatePostResponse(post=reddit_pb2.Post(title="post1", text="a post", video_url="video.mp4", author=reddit_pb2.User(userID='cindy'), score=10, state=reddit_pb2.Post.NORMAL, publication_date="2023-12-08 13:23:09"))
        self.mock_client.get_top_comments.return_value =reddit_pb2.GetTopCommentsResponse(comments=[
            reddit_pb2.Comment(id=0, post_id=0, author=reddit_pb2.User(userID='john'), text="hello", score=4, state=reddit_pb2.Comment.NORMAL, publication_date="2023-12-10 12:33:33", has_replies=True),
            reddit_pb2.Comment(id=1, post_id=0, author=reddit_pb2.User(userID='bob'), text="hello also", score=2, state=reddit_pb2.Comment.NORMAL, publication_date="2023-12-13 21:53:14", has_replies=False)
        ])
        self.mock_client.expand_comment_branch.return_value =reddit_pb2.ExpandCommentBranchResponse(comments=[
            reddit_pb2.CommentWithReplies(
                comment=reddit_pb2.Comment(id=3, comment_id=0, author=reddit_pb2.User(userID='alice'), text="good morning john -from alice", score=33, state=reddit_pb2.Comment.NORMAL, publication_date="2023-12-15 21:53:14", has_replies=False),
                top_replies=[]
            )
        ])
        # self.mock_client = RedditClient()

    def test_retrieve_post(self):
        result = retrieve_post(self.mock_client, self.post_id)

        self.assertIsNotNone(result)
        self.assertEqual(result.title, "post1")
        self.assertEqual(result.text, "a post")
        self.assertEqual(result.score, 10)

    def test_retrieve_most_upvoted_comments(self):
        result = retrieve_most_upvoted_comments(self.mock_client, self.post_id, 2)

        self.assertIsNotNone(result)
        self.assertTrue(len(result) <= 2)
        self.assertEqual(result[0].post_id, 0)
        self.assertEqual(result[0].score, 4)

    def test_expand_most_upvoted_comment(self):
        result = expand_most_upvoted_comment(self.mock_client, self.post_id, 1)

        self.assertIsNotNone(result)
        self.assertTrue(len(result) == 1)
        self.assertEqual(result[0].comment.text, "good morning john -from alice")
        self.assertEqual(len(result[0].top_replies), 0)

    def test_most_upvoted_reply_under_most_upvoted_comment(self):
        result = most_upvoted_reply_under_most_upvoted_comment(self.mock_client, self.post_id)

        self.assertIsNotNone(result)
        self.assertEqual(result.text, "good morning john -from alice")
        self.assertEqual(result.score, 33)

if __name__ == '__main__':
    unittest.main()