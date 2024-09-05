# Mozart

## Description
App that uses a spotify playlist to make a new song using machine learning.

## Design
- have user input a playlist with 10-20 tracks, no track more than 10 minutes long (validate with [Spotipy](https://spotipy.readthedocs.io/en/2.17.1/))
- download playlist using [Savify](https://github.com/LaurenceRawlings/savify)
- isolate sounds using [Spleeter](https://github.com/deezer/spleeter) (4stems-16kHz)

## Tools
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Gunicorn](https://gunicorn.org/)
- [Spotipy](https://spotipy.readthedocs.io/en/2.17.1/)
- [Savify](https://github.com/LaurenceRawlings/savify)
- [Spleeter](https://github.com/deezer/spleeter)

## Contribution
If you have an idea or want to report a bug, please create an issue.

Otherwise:

1. Clone the respository.
```shell
git clone https://github.com/ColeBallard/mozart
```

2. Create a Spotify Web Developer account [here](https://developer.spotify.com/my-applications) and create a new application.

3. In the application settings, add `http://127.0.0.1:5000/oauth/callback` to the **Redirect URIs**. 

4. Install [ffmpeg](https://ffmpeg.org/) and [libsndfile](http://www.mega-nerd.com/libsndfile/).
```shell
conda install -c conda-forge ffmpeg libsndfile
```

5. Install [virtualvenv](https://docs.python.org/3/tutorial/venv.html).

On macOS and Linux:
```shell
python3 -m pip install --user virtualenv
```
On Windows:
```shell
py -m pip install --user virtualenv
```

6. Create the virtual environment (in the `flask` folder).

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

7. Activate the virtual environment (still in the `flask` folder).

On macOS and Linux:
```shell
source env/bin/activate
```
On Windows:
```shell
.\env\Scripts\activate
```

8. Create a file called `credentials.sh` (in the `flask` folder) and add the following (replace `YOURSECRETKEY` with a random string, [read more](https://flask.palletsprojects.com/en/1.1.x/config/)) -
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

9. Add the variables in `credentials.sh` to the environment.
```shell
source credentials.sh
```

10. Install spleeter.
```shell
pip install spleeter
```

11. Run flask.
```shell
flask run
```

12. Make a pull request.

Seperate audio files using spleeter.

On macOS and Linux:
```shell
cd spleeter
for f in sav_downloads/*.wav; do spleeter separate -o isolated_sounds -p spleeter:4stems-16kHz $f; done
```

## **[Contact](https://github.com/ColeBallard/coleballard.github.io/blob/main/README.md)**
