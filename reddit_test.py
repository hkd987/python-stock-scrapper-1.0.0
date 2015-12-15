import praw

r = praw.Reddit(user_agent='this_is_a_test:1.0.0')
submissions = r.get_subreddit('opensource').get_hot(limit=5)
[str(x) for x in submissions]


