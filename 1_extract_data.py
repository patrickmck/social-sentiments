from pprint import pprint
import praw
import pickle

# Pro tip: never upload keys, secrets, passwords etc. to Github. Use environment variables instead.
jk_client_id = ''
jk_client_secret = ''
jk_username = ''
jk_password = ''
query_subreddit = 'wallstreetbets'
query_size = 1000
query_period = 'month'

# Connect to PRAW instance
reddit_client = praw.Reddit(
    client_id=jk_client_id,
    client_secret=jk_client_secret,
    password=jk_password,
    user_agent="test",
    username=jk_username,
)

# For more on list comprehension see https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions.
query_submissions = [
    {
        "key": s.value # TODO fill in desired data points
    }
    for s in reddit_client.subreddit(query_subreddit) # TODO filter for top N in last month
    if not s.stickied
]
print(len(query_submissions))
pprint(query_submissions[:2])


for sub in query_submissions:
    # TODO Iterate over submissions and get comment data for each one
    continue

# Pickling is a type of data serialisation, see https://docs.python.org/3/library/pickle.html.
with open('reddit_data.pickle', 'wb') as f:
    pickle.dump(query_submissions, f, pickle.HIGHEST_PROTOCOL)