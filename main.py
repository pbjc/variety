import features
import praw
import secrets

user_agent = 'python:variety:0.0.1 (by /u/choifish)'

def main():
    reddit = praw.Reddit(client_id=secrets.client_id,
                         client_secret=secrets.client_secret,
                         user_agent=user_agent)

    # submission = reddit.submission(url='https://www.reddit.com/r/netneutrality/comments/7iym1b/this_is_my_senator_pat_toomey_he_sold_me_and_my/')
    # submission = reddit.submission(url='https://www.reddit.com/r/philosophy/comments/8624sp/a_death_row_inmates_dementia_means_he_cant/')
    submission = reddit.submission(url='https://www.reddit.com/r/philosophy/comments/5u78oy/on_this_day_february_15_2416_years_ago_socrates/')
    score = features.CommentLength().score_submission(submission)
    print(score)

if __name__ == '__main__':
    main()
