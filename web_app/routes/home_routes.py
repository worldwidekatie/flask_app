# web_app/routes/home_routes.py

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    x = 2 + 2
    return f"Hello World! {x}"

@home_routes.route("/about")
def about():
    return "About me"


@home_routes.route("/tweets.json")
@home_routes.route("/tweets_endpoint")
def list_tweets():
    tweets = [
        {"user": "username1", "text": "Tweet 1"},
        {"user": "username2", "text": "Tweet 2"},
        {"user": "username3", "text": "Tweet 3"},
        {"user": "username1", "text": "Tweet 4"},
        {"user": "username2", "text": "Tweet 5"},
        {"user": "username3", "text": "Tweet 6"},
    ]
    return jsonify(tweets)

@home_routes.route("/tweets")
def list_tweets_for_humans():
    tweets = [
        {"user": "username1", "text": "Tweet 1"},
        {"user": "username2", "text": "Tweet 2"},
        {"user": "username3", "text": "Tweet 3"},
        {"user": "username1", "text": "Tweet 4"},
        {"user": "username2", "text": "Tweet 5"},
        {"user": "username3", "text": "Tweet 6"},
    ]
    #tweet_records = Tweet.query.all()
    #print(tweet_records)
    print(tweets)

    return render_template("tweets.html", message="Here's some tweets", tweets=tweets)#tweet_records)

@home_routes.route("/tweets/new")
def new_tweet():
    return render_template("new_tweet.html")

@home_routes.route("/tweets/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form))

    new_tweet = Tweet(title=request.form["tweet text"], author_id=request.form["user"])
    db.session.add(new_tweet)
    db.session.commit()

    return jsonify({
        "message": "TWEET CREATED OK",
        "tweet": dict(request.form)
    })
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    #return redirect("/books")