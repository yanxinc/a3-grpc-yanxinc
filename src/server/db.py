import reddit_pb2


users = {
    0: reddit_pb2.User(userID="cindy"),
    1: reddit_pb2.User(userID="john"),
    2: reddit_pb2.User(userID="bob"),
    3: reddit_pb2.User(userID="alice")
}

posts = {
    0: reddit_pb2.Post(title="post1", text="a post", video_url="video.mp4", author=users[0], score=10, state=reddit_pb2.Post.NORMAL, publication_date="2023-12-08 13:23:09"),
    1: reddit_pb2.Post(title="post2", text="another post", image_url="image1.img", author=users[0], score=7, state=reddit_pb2.Post.LOCKED, publication_date="2023-12-08 17:56:18"),
    2: reddit_pb2.Post(title="post3333", text="asdjfhasljkfhsd", image_url="image2.img", author=users[2], score=333, state=reddit_pb2.Post.NORMAL, publication_date="2023-12-10 12:12:12")
}

comments = {
    0: reddit_pb2.Comment(id=0, post_id=0, author=users[1], text="hello", score=4, state=reddit_pb2.Comment.NORMAL, publication_date="2023-12-10 12:33:33", has_replies=True),
    1: reddit_pb2.Comment(id=1, post_id=0, author=users[2], text="hello also", score=2, state=reddit_pb2.Comment.NORMAL, publication_date="2023-12-13 21:53:14", has_replies=False),
    2: reddit_pb2.Comment(id=2, comment_id=0, author=users[2], text="good morning john", score=22, state=reddit_pb2.Comment.NORMAL, publication_date="2023-12-13 21:53:14", has_replies=False),
    3: reddit_pb2.Comment(id=3, comment_id=0, author=users[3], text="good morning john -from alice", score=33, state=reddit_pb2.Comment.NORMAL, publication_date="2023-12-15 21:53:14", has_replies=False)
}