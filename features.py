import math
from textblob import TextBlob
from bs4 import BeautifulSoup

class Feature(object):
    @staticmethod
    def weight_by_upvotes(comments):
        '''Gives comments and weights by relative number of upvotes, i.e.
        score / sum.'''
        total = sum(comment.score for comment in comments if comment.score > 0)
        return (max(0, comment.score / total) for comment in comments)

    @staticmethod
    def weighted_comment_score(weights, comments, score_comment):
        return (weight * score_comment(comment)
                for weight, comment in zip(weights, comments))

    @staticmethod
    def sigmoid(x, low=-1, high=1):
        '''Applies a sigmoid to values bounded in a given range to "boost"
        values closer to the center of the range'''
        height = high - low
        amplitude = height / 2
        center = (high + low) / 2
        return height / (1 + math.exp(-4 * (x - center))) - (amplitude - center)

    def score_submission(self, submission):
        submission.comments.replace_more(limit=0)
        comments = submission.comments.list()
        return self.score_comments(comments)

    def score_comments(self, comments):
        raise NotImplementedError

class Polarity(Feature):
    @staticmethod
    def compute_polarity(comment):
        return Feature.sigmoid(TextBlob(comment.body).sentiment.polarity)

    def score_comments(self, comments):
        weights = self.weight_by_upvotes(comments)
        return sum(self.weighted_comment_score(
            weights, comments, self.compute_polarity))

class Subjectivity(Feature):
    @staticmethod
    def compute_subjectivity(comment):
        return Feature.sigmoid(TextBlob(comment.body).sentiment.subjectivity, low=0, high=1)

    def score_comments(self, comments):
        weights = self.weight_by_upvotes(comments)
        return sum(self.weighted_comment_score(
            weights, comments, self.compute_subjectivity))

class PoliticalAffiliation(Feature):
    def score(self, submission):
        raise NotImplementedError

class LinkCount(Feature):
    @staticmethod
    def count_links(comment):
        soup = BeautifulSoup(comment.body_html, 'html.parser')
        return len(soup.findAll('a'))

    def score_comments(self, comments):
        weights = self.weight_by_upvotes(comments)
        return sum(self.weighted_comment_score(
            weights, comments, self.count_links))

class CommentLength(Feature):
    @staticmethod
    def count_words(comment):
        return len(comment.body.split())

    def score_comments(self, comments):
        weights = self.weight_by_upvotes(comments)
        return sum(self.weighted_comment_score(
            weights, comments, self.count_words))
