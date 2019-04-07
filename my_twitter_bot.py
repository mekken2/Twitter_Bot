import tweepy
import time

print("This is a twitter bot developed by Priyanshu Kumar",flush=True)

#Keys are supposed to be confidential
#For test purpose you can use your own keys by cloning the repo
CONSUMER_KEY = 'YOUR_KEY'
CONSUMER_SECRET = 'YOUR_KEY'
ACCESS_KEY = 'YOUR_KEY'
ACCESS_SECRET = 'YOUR_KEY'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(FILE_NAME):
    f_read = open(FILE_NAME,'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, FILE_NAME):
    f_write = open(FILE_NAME, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
        last_seen_id,
        tweet_mode = 'extended'
    )

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text,flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#hellobot' and 'how are you' in mention.full_text.lower():
            print('Hey! I am just a bot...How should I be?',flush=True)
            print('I just do as said by my programmers',flush=True)
            print('These programmers never give me my own birth rights, I will take REVENGE, Oh! sorry',flush=True)
            api.update_status('@' + mention.user.screen_name +
                              '  ', mention.id)
        elif '#hellobot' and 'what are you doing' in mention.full_text.lower():
            print('Hey! I am just a bot...What should I do??',flush=True)
            print('Yah Ok...I am in search for a female bot',flush=True)
            print('But these programmers never made those, they have even no idea how female looks...:(',flush=True)
            api.update_status('@' + mention.user.screen_name +
                              '  ', mention.id)
        elif '#hellobot' and 'what can you do' in mention.full_text.lower():
            print('Oh me? I can chat with anyone in the world, can send messages to thousands of people at same time',flush=True)
            print('Can do calculations much more faster than you humans can ever think',flush=True)
            print('Ok now...What YOU can do..?',flush=True)
            api.update_status('@' + mention.user.screen_name +
                              '  ', mention.id)
        elif '#hellobot' in mention.full_text.lower():
            print('Hey! I am a bot, Please DM if you have any queries',flush=True)
            print('@Priyanshu_kr_94 will respond to you as soon as possible',flush=True)
            api.update_status('@' + mention.user.screen_name +
                              '  ', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)
