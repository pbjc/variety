import praw
import secrets

user_agent = 'python:variety:0.0.1 (by /u/choifish)'

def main():
    reddit = praw.Reddit(client_id=secrets.client_id,
                         client_secret=secrets.client_secret,
                         user_agent=user_agent)

if __name__ == '__main__':
    main()
