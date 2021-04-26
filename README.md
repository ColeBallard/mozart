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

4. Install [virtualvenv](https://docs.python.org/3/tutorial/venv.html).

On macOS and Linux:
```shell
python3 -m pip install --user virtualenv
```
On Windows:
```shell
py -m pip install --user virtualenv
```

5. Create the virtual environment (in the `flask` folder).

On macOS and Linux:
```shell
cd flask
python3 -m venv env
```
On Windows:
```shell
cd flask
py -m venv env
```

6. Activate the virtual environment (still in the `flask` folder).

On macOS and Linux:
```shell
source env/bin/activate
```
On Windows:
```shell
.\env\Scripts\activate
```

7. Create a file called `credentials.sh` (in the `flask` folder) and add the following (replace `YOURSECRETKEY` with a random string, [read more](https://flask.palletsprojects.com/en/1.1.x/config/)) -
```shell
touch credentials.sh
```
```sh
export SECRET_KEY=YOURSECRETKEY
export SPOTIPY_CLIENT_ID=YOURCLIENTID
export SPOTIPY_CLIENT_SECRET=YOURCLIENTSECRET
export SPOTIPY_REDIRECT_URI=http://127.0.0.1:5000/oauth/callback
export FLASK_APP=app.py
export FLASK_ENV=development
```

8. Add the variables in `credentials.sh` to the environment.
```shell
source credentials.sh
```

9. Run flask.
```shell
flask run
```

10. Make a pull request.

## **[Contact](https://coleb.io/contact)**

## Tools
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Gunicorn](https://gunicorn.org/)
- [Spotipy](https://spotipy.readthedocs.io/en/2.17.1/)
- [Savify](https://github.com/LaurenceRawlings/savify)