import praw

reddit  = praw.Reddit(client_id ='Afu2CHGItzD7dQ',
        client_secret = 'jqcMUeEX9a1Wh2zMk5xFBGMfbm8',
        username='rareserver',
        password='lamasia',
        user_agent='my user agent')

subreddit = reddit.subreddit('Python')
hot_python = subreddit.hot()
for submission in hot_python:
    print(submission.title)
