from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'db'
app.config["MONGO_URI"] = "mongodb://host:port/db"

mongo = PyMongo(app)

@app.route('/tweets', methods=['GET'])
def get_tweets():
	tweets = mongo.db['name_collection']

	results = []
	for tweet in tweets.find():
		results.append({'usernameTweet': tweet['usernameTweet'],
						'user_id': tweet['user_id'],
						'ID': tweet['ID'],
						'text': tweet['text'],
						'url': tweet['url'],
						'datetime': tweet['datetime'],
						'number_retweet': tweet['number_retweet'],
						'number_favorite': tweet['number_favorite'],
						'number_reply': tweet['number_reply'],
						'is_reply':tweet['is_reply'],
						'is_retweet': tweet['is_retweet']})
	return jsonify({'tweets': results})

@app.route('/tweet/<user_id>', methods=['GET'])
def get_tweet(user_id):
	tweets = mongo.db.parse_Vera_Lucia
	tweet = tweets.find_one({'user_id': user_id})
	if tweet:
		output = {'usernameTweet': tweet['usernameTweet'],
						'user_id': tweet['user_id'],
						'ID': tweet['ID'],
						'text': tweet['text'],
						'url': tweet['url'],
						'datetime': tweet['datetime'],
						'number_retweet': tweet['number_retweet'],
						'number_favorite': tweet['number_favorite'],
						'number_reply': tweet['number_reply'],
						'is_reply':tweet['is_reply'],
						'is_retweet': tweet['is_retweet']}
	else:
		output = 'No such user id'

	return jsonify({'result': output})


@app.route('/tweet', methods=['POST'])
def add_tweet():
	tweet = mongo.db.parse_Vera_Lucia

	usernameTweet = request.json['usernameTweet']
	user_id = request.json['user_id']
	ID = request.json['ID']
	text = request.json['text']
	url = request.json['url']
	datetime = request.json['datetime']
	number_retweet = request.json['number_retweet']
	number_favorite = request.json['number_favorite']
	number_reply = request.json['number_reply']
	is_reply = request.json['is_reply']
	is_retweet = request.json['is_retweet']

	tweet_id = tweet.insert_one({'usernameTweet': usernameTweet,
						'user_id': user_id,
						'ID': ID,
						'text': text,
						'url': url,
						'datetime': datetime,
						'number_retweet': number_retweet,
						'number_favorite': number_favorite,
						'number_reply': number_reply,
						'is_reply': is_reply,
						'is_retweet': is_retweet})
	return jsonify({'ok': True, 'message': 'User created successfully!'}), 200


if __name__ == '__main__':
	app.run(debug=True)
