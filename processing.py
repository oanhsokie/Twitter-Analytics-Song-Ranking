import csv
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

with open('./data/3001.csv', 'r') as f:
    try:
        with open('./data/final3001.csv', 'w') as f2:
            writer = csv.writer(f2)
            header = ['Song', '#Tweet', '#Neg-score_Tweet', '#Pos-score_Tweet', 'Neg-score_Ave', 'Pos-score_Ave']
            writer.writerow(header)

            csv_reader = csv.reader(f, delimiter=',')
            line_count = 0

            cntTweet = {}
            cntNegTweet = {}
            cntPosTweet = {}
            negAve = {}
            posAve = {}

            for row in csv_reader:
                print(row[0] +  " " + row[1] + " " + row[2] +  " " + row[3])
                line_count += 1
                if (row[0] not in cntTweet):
                    cntTweet[row[0]] = 0
                    cntNegTweet[row[0]] = 0
                    cntPosTweet[row[0]] = 0
                    negAve[row[0]] = 0
                    posAve[row[0]] = 0

                cntTweet[row[0]] += 1
                negAve[row[0]] += float(row[1])
                posAve[row[0]] += float(row[3])

                if row[1] > row[3]:
                    cntNegTweet[row[0]] += 1
                if row[3] > row[1]:
                    cntPosTweet[row[0]] += 1


            print(line_count)

            for song in songlist:
                if ('#' in song):
                    row = [song, 0, 0, 0, 0, 0]
                    if (song in cntTweet):
                        row[1] = cntTweet[song]
                        row[2] = cntNegTweet[song]
                        row[3] = cntPosTweet[song]
                        row[4] = negAve[song] / row[1]
                        row[5] = posAve[song] / row[1]
                    writer.writerow(row)

    except Exception as e:
        print("Exception occurred!!!!")