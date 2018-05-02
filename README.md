## Config DB
```
$ mongod --port 27025 --dbpath workspace/python/TwitterML/nodeJs/data/db/

```
## Start NodeServer
```
$ npm start

```

## How to start
Add yout twitter user name nad password in cofing.py file
```
#Config file
DATACOUP_USERNAME = "exampleUsername"
DATACOUP_PASSWORD = "examplePassword"

```
If you want colect most popular hashtag run:
```
$ python script.py

```
with method
```
if __name__ == "__main__":
    username = config.DATACOUP_USERNAME
    password = config.DATACOUP_PASSWORD
    login_twitter(username,password)
    getTredHash()

```
If you wanna check out other hashtag use method
```
if __name__ == "__main__":
    username = config.DATACOUP_USERNAME
    password = config.DATACOUP_PASSWORD
    login_twitter(username,password)
    openHashtag("#YourHashTag")

```

Get value from database use:

```
python request.py getTwitts()

```
