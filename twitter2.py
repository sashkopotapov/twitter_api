import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def followers(word, count):
    while True:

        # print('')
        acct = input('Enter Twitter Account("end" to finish):')
        if acct == 'end':
            break
        if (len(acct) < 1): break
        url = twurl.augment(TWITTER_URL,
                            {'screen_name': acct, 'count': count})
        # print('Retrieving', url)
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()

        js = json.loads(data)

        headers = dict(connection.getheaders())
        # print(js)
        for u in js['users']:

            print(u[word])
            if 'status' not in u:
                print('   * No status found')
                continue
