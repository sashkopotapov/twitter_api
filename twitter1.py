import urllib.request, urllib.parse, urllib.error
import twurl
import ssl
import json


TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
def timeline(key, num):
    while True:
        print('')
        acct = input("Enter Twitter Account('end' to finish:")
        if acct == 'end':
            break
        if (len(acct) < 1): break
        url = twurl.augment(TWITTER_URL,
                            {'screen_name': acct, 'count': num})
        print('Retrieving', url)
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()
        d = json.loads(data)
        # print('Remaining', headers['x-rate-limit-remaining'])
        for u in d:
            print(u[key])
            if 'status' not in u:
                print('   * No status found')
                continue
