# Mozart

## Description
App that uses a spotify playlist to make a new song using machine learning.

## Design
- have user input a playlist with 10-30 songs
- get playlist metadata from [Spotify API](https://developer.spotify.com/documentation/web-api/)
- generate song based on inputted music using [Tensorflow](https://github.com/tensorflow/tensorflow) model
- model should train on a variety of (good?) songs

## Contribution
If you have an idea or want to report a bug, please create an issue.

Otherwise:

1. Clone the respository.
```shell
git clone https://github.com/ColeBallard/mozart
```

2. Create a Spotify Web Developer account [here](https://developer.spotify.com/my-applications) and create a new application.

3. In the application settings, add `http://127.0.0.1:5000/oauth/callback` to the **Redirect URIs**. 

4. Create a file called `credentials.sh` and add the following -
```sh
export SECRET_KEY=YOURSECRETKEY
export SPOTIPY_CLIENT_ID=YOURCLIENTID
export SPOTIPY_CLIENT_SECRET=YOURCLIENTSECRET
export SPOTIPY_REDIRECT_URI=http://127.0.0.1:5000/oauth/callback
export FLASK_APP=server.py
export FLASK_ENV=development
```

5. Add the variables in `credentials.sh` to the environment.
```shell
source credentials.sh
```

6. Make a pull request.

## **[Contact](https://coleb.io/contact)**

## Tools
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Spotipy](https://spotipy.readthedocs.io/en/2.17.1/)