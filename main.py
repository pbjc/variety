import features
import praw
import secrets
import sys

feats = [
    features.Polarity,
    features.Subjectivity,
    features.LinkCount,
    features.CommentLength,
]
user_agent = 'python:variety:0.0.1 (by /u/choifish)'

def main():
    _, url = sys.argv
    reddit = praw.Reddit(client_id=secrets.client_id,
                         client_secret=secrets.client_secret,
                         user_agent=user_agent)
    submission = reddit.submission(url=url)
    submission.comments.replace_more(limit=0)
    for feat in feats:
        score = feat().score_comments(submission.comments)
        print('{} score: {}'.format(feat.__name__, score))

if __name__ == '__main__':
    main()
