import nltk
import json
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import csv
import re

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


songlist =      ['#youneedtocalmdown', '@taylorswift',
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
# Processing all tweet
sid = SentimentIntensityAnalyzer()
with open('./data/3001.json', 'r') as f:
    try:
        with open('./data/3001.csv', 'a') as f2:
            writer = csv.writer(f2)
            # header = ['HashTag', 'Neg Score', 'Neu Score', 'Pos Score']
            # writer.writerow(header)
            for line in f:
                print('>', end='', flush=True)
                tweet = json.loads(line)
                try:
                    tokens = preprocess(tweet['text'])
                    sentence = ""
                    for tk in tokens:
                        sentence += tk + " "
                    ss = sid.polarity_scores(sentence)
                    for str in songlist:
                        if (str in sentence):
                            row = [str, ss['neg'], ss['neu'], ss['pos']]
                            writer.writerow(row)
                except:
                    print('ERROR', end='', flush=True)

    except BaseException as e:
        print("Exception occurred!!!!! ")


# Song | #Tweet | #Neg-score tweet | #Pos-score tweet | Ave neg score | Ave pos score

# #Hashtag | Neg score | Neu score | Pos score | Text