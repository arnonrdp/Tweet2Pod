from os import getenv
from time import sleep
from tweepy import OAuthHandler, API
from post_anchor import anchor_connect


def twitter_connect():
    auth = OAuthHandler(getenv('API_KEY'),
                        getenv('API_KEY_SECRET'))
    auth.set_access_token(getenv('ACCESS_TOKEN'),
                          getenv('ACCESS_TOKEN_SECRET'))
    api = API(auth)
    try:
        api.verify_credentials()
        print('Twitter: conexão bem-sucedida!')
        search_tweets(api)
    except Exception as e:
        print('Twitter: conexão mal-sucedida! Tentando novamente em 2 minutos.\n', e)
        sleep(120)
        twitter_connect()


def search_tweets(api):
    tweets = api.search_tweets('Minuto Touro from:PabloSpyer', tweet_mode='extended', count=1)
    for tweet in tweets:
        print(tweet.author.screen_name)
        print(tweet.created_at)
        print(tweet.full_text)
        print(tweet.extended_entities['media'][0]['media_url_https'])
        print(tweet.extended_entities['media'][0]['video_info']['variants'][-1]['url'])
        print('====================================================')
    anchor_connect()


# TODO: TRATAR LINKS DE VÍDEOS
# {
#   "created_at": "Thu Jul 28 10:42:35 +0000 2022",
#   "id": 1552605433168379904,
#   "id_str": "1552605433168379904",
#   "full_text": "Minuto Touro de Ouro com @PabloSpyer\n\nMeta frustra e cai 6% agora, Quinta de Ouro e disparada do minério.\n\nEleito Melhor Programa de Economia do Rádio Brasileiro em 2021 https://t.co/wbVlQLgOXz",
#   "truncated": "False",
#   "display_text_range": [0, 169],
#   "entities": {
#     "hashtags": [],
#     "symbols": [],
#     "user_mentions": [
#       {
#         "screen_name": "PabloSpyer",
#         "name": "Pablo Spyer",
#         "id": 2408015736,
#         "id_str": "2408015736",
#         "indices": [25, 36]
#       }
#     ],
#     "urls": [],
#     "media": [
#       {
#         "id": 1552605299026149376,
#         "id_str": "1552605299026149376",
#         "indices": [170, 193],
#         "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1552605299026149376/pu/img/WpH5BNskBMIlfg72.jpg",
#         "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1552605299026149376/pu/img/WpH5BNskBMIlfg72.jpg",
#         "url": "https://t.co/wbVlQLgOXz",
#         "display_url": "pic.twitter.com/wbVlQLgOXz",
#         "expanded_url": "https://twitter.com/PabloSpyer/status/1552605433168379904/video/1",
#         "type": "photo",
#         "sizes": {
#           "thumb": { "w": 150, "h": 150, "resize": "crop" },
#           "small": { "w": 383, "h": 680, "resize": "fit" },
#           "large": { "w": 720, "h": 1280, "resize": "fit" },
#           "medium": { "w": 675, "h": 1200, "resize": "fit" }
#         }
#       }
#     ]
#   },
#   "extended_entities": {
#     "media": [
#       {
#         "id": 1552605299026149376,
#         "id_str": "1552605299026149376",
#         "indices": [170, 193],
#         "media_url": "http://pbs.twimg.com/ext_tw_video_thumb/1552605299026149376/pu/img/WpH5BNskBMIlfg72.jpg",
#         "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1552605299026149376/pu/img/WpH5BNskBMIlfg72.jpg",
#         "url": "https://t.co/wbVlQLgOXz",
#         "display_url": "pic.twitter.com/wbVlQLgOXz",
#         "expanded_url": "https://twitter.com/PabloSpyer/status/1552605433168379904/video/1",
#         "type": "video",
#         "sizes": {
#           "thumb": { "w": 150, "h": 150, "resize": "crop" },
#           "small": { "w": 383, "h": 680, "resize": "fit" },
#           "large": { "w": 720, "h": 1280, "resize": "fit" },
#           "medium": { "w": 675, "h": 1200, "resize": "fit" }
#         },
#         "video_info": {
#           "aspect_ratio": [9, 16],
#           "duration_millis": 111851,
#           "variants": [
#             {
#               "bitrate": 950000,
#               "content_type": "video/mp4",
#               "url": "https://video.twimg.com/ext_tw_video/1552605299026149376/pu/vid/480x852/KpAM7EeUeKmBlN6g.mp4?tag=12"
#             },
#             {
#               "content_type": "application/x-mpegURL",
#               "url": "https://video.twimg.com/ext_tw_video/1552605299026149376/pu/pl/jc5wLqVgW4QGo28p.m3u8?tag=12&container=fmp4"
#             },
#             {
#               "bitrate": 632000,
#               "content_type": "video/mp4",
#               "url": "https://video.twimg.com/ext_tw_video/1552605299026149376/pu/vid/320x568/XAQhPwMdjjJOYe2V.mp4?tag=12"
#             },
#             {
#               "bitrate": 2176000,
#               "content_type": "video/mp4",
#               "url": "https://video.twimg.com/ext_tw_video/1552605299026149376/pu/vid/720x1280/AgsN9ioq22ENSI5R.mp4?tag=12"
#             }
#           ]
#         },
#         "additional_media_info": { "monetizable": "False" }
#       }
#     ]
#   }
# }
