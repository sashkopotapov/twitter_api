from twitter2 import followers
from twitter1 import timeline


while True:
    switcher = str(input("print 'followers' to see inf about followers and 'timeline' - about user`s timeline('end' "
                         "to finish: "))
    if switcher == "end":
        break

    if switcher == 'followers':
        key = str(input("Enter a 'keyword' to see information about followers you want(type 'list' to see list of "
                        "'keywords: "))
        if key == 'list':
            keywords = ['id', 'id_str', 'name', 'screen_name', 'location', 'description', 'url','entities', 'protected',
                  'followers_count', 'friends_count', 'listed_count', 'created_at', 'favourites_count', 'utc_offset',
                  'time_zone', 'geo_enabled', 'verified', 'statuses_count', 'lang', 'status', 'contributors_enabled',
                  'is_translator', 'is_translation_enabled', 'profile_background_color', 'profile_background_image_url',
                  'profile_background_image_url_https', 'profile_background_tile', 'profile_image_url',
                  'profile_image_url_https', 'profile_banner_url', 'profile_link_color', 'profile_sidebar_border_color',
                  'profile_sidebar_fill_color', 'profile_text_color', 'profile_use_background_image',
                  'has_extended_profile', 'default_profile', 'default_profile_image', 'following', 'live_following',
                  'follow_request_sent', 'notifications', 'muting', 'blocking', 'blocked_by', 'translator_type']
            [print(i) for i in keywords]
        else:
            num = str(input('enter number of followers you want to see(max 200): '))
            print(followers(key, num))
    elif switcher == 'timeline':
        key = str(input("Enter a 'keyword' to see information about timeline you want(type 'list' to see list of "
                        "'keywords: "))
        if key == 'list':
            keywords = ['created_at', 'id', 'id_str', 'text', 'truncated', 'entities', 'source',
                        'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id',
                        'in_reply_to_user_id_str','in_reply_to_screen_name', 'user', 'geo', 'coordinates', 'place',
                        'contributors', 'is_quote_status', 'retweet_count', 'favorite_count', 'favorited', 'retweeted',
                        'possibly_sensitive', 'lang']
            [print(i) for i in keywords]
        else:
            num = str(input('enter number of followers you want to see(max 20): '))
            print(timeline(key, num))

