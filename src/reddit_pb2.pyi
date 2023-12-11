from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VoteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UPVOTE: _ClassVar[VoteType]
    DOWNVOTE: _ClassVar[VoteType]
UPVOTE: VoteType
DOWNVOTE: VoteType

class User(_message.Message):
    __slots__ = ("userID",)
    USERID_FIELD_NUMBER: _ClassVar[int]
    userID: str
    def __init__(self, userID: _Optional[str] = ...) -> None: ...

class Post(_message.Message):
    __slots__ = ("title", "text", "video_url", "image_url", "author", "score", "state", "publication_date")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NORMAL: _ClassVar[Post.State]
        LOCKED: _ClassVar[Post.State]
        HIDDEN: _ClassVar[Post.State]
    NORMAL: Post.State
    LOCKED: Post.State
    HIDDEN: Post.State
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    title: str
    text: str
    video_url: str
    image_url: str
    author: User
    score: int
    state: Post.State
    publication_date: str
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ..., video_url: _Optional[str] = ..., image_url: _Optional[str] = ..., author: _Optional[_Union[User, _Mapping]] = ..., score: _Optional[int] = ..., state: _Optional[_Union[Post.State, str]] = ..., publication_date: _Optional[str] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ("id", "comment_id", "post_id", "author", "text", "score", "state", "publication_date", "has_replies")
    class CommentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NORMAL: _ClassVar[Comment.CommentState]
        HIDDEN: _ClassVar[Comment.CommentState]
    NORMAL: Comment.CommentState
    HIDDEN: Comment.CommentState
    ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    HAS_REPLIES_FIELD_NUMBER: _ClassVar[int]
    id: int
    comment_id: int
    post_id: int
    author: User
    text: str
    score: int
    state: Comment.CommentState
    publication_date: str
    has_replies: bool
    def __init__(self, id: _Optional[int] = ..., comment_id: _Optional[int] = ..., post_id: _Optional[int] = ..., author: _Optional[_Union[User, _Mapping]] = ..., text: _Optional[str] = ..., score: _Optional[int] = ..., state: _Optional[_Union[Comment.CommentState, str]] = ..., publication_date: _Optional[str] = ..., has_replies: bool = ...) -> None: ...

class CreatePostRequest(_message.Message):
    __slots__ = ("title", "text", "video_url", "image_url", "author")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    title: str
    text: str
    video_url: str
    image_url: str
    author: User
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ..., video_url: _Optional[str] = ..., image_url: _Optional[str] = ..., author: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class CreatePostResponse(_message.Message):
    __slots__ = ("post_id", "post")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    POST_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    post: Post
    def __init__(self, post_id: _Optional[int] = ..., post: _Optional[_Union[Post, _Mapping]] = ...) -> None: ...

class VotePostRequest(_message.Message):
    __slots__ = ("post_id", "vote_type")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    vote_type: VoteType
    def __init__(self, post_id: _Optional[int] = ..., vote_type: _Optional[_Union[VoteType, str]] = ...) -> None: ...

class VotePostResponse(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: int
    def __init__(self, score: _Optional[int] = ...) -> None: ...

class GetPostRequest(_message.Message):
    __slots__ = ("post_id",)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: int
    def __init__(self, post_id: _Optional[int] = ...) -> None: ...

class GetPostResponse(_message.Message):
    __slots__ = ("post",)
    POST_FIELD_NUMBER: _ClassVar[int]
    post: Post
    def __init__(self, post: _Optional[_Union[Post, _Mapping]] = ...) -> None: ...

class CreateCommentRequest(_message.Message):
    __slots__ = ("comment_id", "post_id", "author", "text")
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    comment_id: int
    post_id: int
    author: User
    text: str
    def __init__(self, comment_id: _Optional[int] = ..., post_id: _Optional[int] = ..., author: _Optional[_Union[User, _Mapping]] = ..., text: _Optional[str] = ...) -> None: ...

class CreateCommentResponse(_message.Message):
    __slots__ = ("comment_id", "comment")
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment_id: int
    comment: Comment
    def __init__(self, comment_id: _Optional[int] = ..., comment: _Optional[_Union[Comment, _Mapping]] = ...) -> None: ...

class VoteCommentRequest(_message.Message):
    __slots__ = ("comment_id", "vote_type")
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    VOTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    comment_id: int
    vote_type: VoteType
    def __init__(self, comment_id: _Optional[int] = ..., vote_type: _Optional[_Union[VoteType, str]] = ...) -> None: ...

class VoteCommentResponse(_message.Message):
    __slots__ = ("score",)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: int
    def __init__(self, score: _Optional[int] = ...) -> None: ...

class GetTopCommentsRequest(_message.Message):
    __slots__ = ("N", "post_id")
    N_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    N: int
    post_id: int
    def __init__(self, N: _Optional[int] = ..., post_id: _Optional[int] = ...) -> None: ...

class GetTopCommentsResponse(_message.Message):
    __slots__ = ("comments",)
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[Comment]
    def __init__(self, comments: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ...) -> None: ...

class ExpandCommentBranchRequest(_message.Message):
    __slots__ = ("N", "comment_id")
    N_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    N: int
    comment_id: int
    def __init__(self, N: _Optional[int] = ..., comment_id: _Optional[int] = ...) -> None: ...

class CommentWithReplies(_message.Message):
    __slots__ = ("comment", "top_replies")
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    TOP_REPLIES_FIELD_NUMBER: _ClassVar[int]
    comment: Comment
    top_replies: _containers.RepeatedCompositeFieldContainer[Comment]
    def __init__(self, comment: _Optional[_Union[Comment, _Mapping]] = ..., top_replies: _Optional[_Iterable[_Union[Comment, _Mapping]]] = ...) -> None: ...

class ExpandCommentBranchResponse(_message.Message):
    __slots__ = ("comments",)
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[CommentWithReplies]
    def __init__(self, comments: _Optional[_Iterable[_Union[CommentWithReplies, _Mapping]]] = ...) -> None: ...
