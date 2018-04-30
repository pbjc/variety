from textblob import TextBlob

class Feature(object):
    def score(self, submission):
        raise NotImplementedError

class Polarity(Feature):
    def score(self, submission):
        raise NotImplementedError

class Subjectivity(Feature):
    def score(self, submission):
        raise NotImplementedError

class PoliticalAffiliation(Feature):
    def score(self, submission):
        raise NotImplementedError

class LinkCount(Feature):
    def score(self, submission):
        raise NotImplementedError

class CommentLength(Feature):
    def score(self, submission):
        raise NotImplementedError
