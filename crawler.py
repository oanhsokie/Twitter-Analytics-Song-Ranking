from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

access_token = "457694877-DQCTsl8Fa0vG6EIo9oFJDgXdeJe2tIkIDOq6r9De"
access_secret = "B3R6EZSJGON4cFMQfsz2kFALVobJeXPNqW0qU3Fx5FPKO"
consumer_key = "1GzHn7pCUWelJADA0y13HnqEL"
consumer_secret = "phIjiv8pfC93peg7Q4LWEmHC7ErCz8nh5ca5tK5Ca3hsDLN6Gy"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('./data/1213.json', 'a') as f:
                f.write(data)
                print('>', end='', flush=True)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

songAndArtist = ['#youneedtocalmdown', '@taylorswift',
                 '#badguy', '@billieeilish',
                 '#idontcare', '@edsheeran', '@justinbieber',
                 '#moneyinthegrave', '@rickross', '@drake',
                 '#suge', '@dababydababy',
                 '#noguidance', '@chrisbrown', '@drake',
                 '#dancingwithastranger', '@samsmith', '@normani',
                 '#ificanthaveyou', '@shawnmendes',
                 '#truthhurts', '@lizzo',
                 '#withoutme', '@halsey',
                 '#7rings', '@arianagrande',
                 '#godscountry', '@blakeshelton',
                 '#whiskeyglasses', '@morganwallen',
                 '#heylookmaimadeit', '@panicatthedisco',
                 '#thelondon', '@youngthug', '@jcodenc', '@trvisXX',
                 '#concalma', '@daddyyankee', '@katyperry',
                 '#beerneverbrokemyheart', '@lukecombs',
                 '#neverreallyover', '@kattyperry',
                 '#earfquake', '@tylethecreator',
                 '#lookwhatgodgaveher', '@thomasrhett',
                 '#whenthepartysover', '@billieeilish',
                 '#crossme', '@edsheeran',
                 '#goloko', '@YG', '@Tyga','@JonZ',
                 '#thegitup', '@blancobrown',
                 '#someoneyouloved', '@lewiscapaldi',
                 '#walkmehome', '@pink',
                 '#knockinboots', '@lukebryan',
                 '#girlsneedlove', '@iamsummerwalker', '@drake',
                 '#alltomyself', '@danandshay',
                 '#shottaflow', '@nlechoppa1',
                 '#callaita', '@imbadbunny',
                 '#rearviewtown', '@jasonaldean',
                 '#talkyououtofit', '@floridageorgialine',
                 '#sanguineparadise', '@liluzivert',
                 '#herewithme', '@marshmellomusic', '@chvrches',
                 '#otrotrago', '@sechmusic', '@darell_rg4l',
                 '#callyoumine', '@thechainsmokers', '@beberexha',
                 '#raisedoncountry', '@chrisyoungmusic',
                 '#loveaint','@eliyoungband',
                 '#baccatitagain', '@yellabezzy214','@gucci1017', '@quavostuntin',
                 '#bigolefreak', '@theestallion',
                 '#terobare', '@nickyjampr', '@ozuna_pr’s',
                 '#racksinthemiddle', '@roddyricch', '@nipseyhussle','@hit_boy',
                 '#theonesthatdidntmakeitbackhome', '@justincolemoore'
                 ]

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=songAndArtist)


# Good links:
# https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
