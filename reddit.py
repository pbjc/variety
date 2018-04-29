"""Interfaces for basic reddit objects."""

class Thread(object):
    def user(self):
        raise NotImplementedError

    def subreddit(self):
        raise NotImplementedError

    def comments(self):
        raise NotImplementedError

class Comment(object):
    def user(self):
        raise NotImplementedError

    def upvotes(self):
        raise NotImplementedError

    def text(self):
        raise NotImplementedError

class User(object):
    def comments(self):
        raise NotImplementedError

"""These classes implement the reddit object interface using mock data, i.e.
none of this data is backed by the reddit API or a database."""

class MockThread(Thread):
    def __init__(self, user, subreddit, comments=None):
        self._user = user
        self._subreddit = subreddit
        self._comments = comments or []

    def user(self):
        return self._user

    def subreddit(self):
        return self._subreddit

    def comments(self):
        return self._comments

class MockComment(Comment):
    def __init__(self, user, upvotes, text):
        self._user = user
        self._upvotes = upvotes
        self._text = text

    def user(self):
        return self._user

    def upvotes(self):
        return self._upvotes

    def text(self):
        return self._text

class MockUser(User):
    def __init__(self, comments=None):
        self._comments = comments or []

    def comments(self):
        return self._comments
