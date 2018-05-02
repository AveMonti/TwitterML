import requests
import json
from twitt import Twitt
from twitts import Twitts


def getTwittsJson():
    r = requests.get('http://localhost:3000/twitts')
    print ("Get value :" + r.text + " \n")
    return r.text

def addTwitts(idValue, tweetValue):
    r = requests.post('http://localhost:3000/twitts', data = {"id": idValue,
                                                           "value": tweetValue})
    print ("Add feedback :" + r.text + " \n")
    return r.text

def getTwitts():
    twittsArray = []
    r = requests.get('http://localhost:3000/twitts')

    parsed_json = json.loads(r.text)
    print(parsed_json)
    for x in parsed_json:
        print(x["_id"])
        print(x["value"])
        newTwitt = Twitt(x["_id"],x["value"])
        twittsArray.append(newTwitt)

    return twittsArray


if __name__ == "__main__":
    addTwitts(9129123,"newTweet2")
    twittArr = getTwitts()
    for x in twittArr:
        print(x.value)
