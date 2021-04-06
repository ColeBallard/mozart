import logging
from flask import (
    Flask, redirect, render_template, request, url_for, session
)
import spotipy
from spotipy import oauth2

app = Flask(__name__)
app.config['SECRET_KEY'] = ''

CACHE = '.spotifycache'
# Reads client id and client secret from environment variables
sp_oauth = oauth2.SpotifyOAuth(cache_path=CACHE )

@app.route('/', methods=['GET'])
def login():
    # If auth token is already cached and not expired, use that else redirect
    # user to login or refresh token
    token_info = sp_oauth.get_cached_token()
    if token_info and not sp_oauth.is_token_expired(token_info):
        access_token = token_info['access_token']
        session['access_token'] = access_token
        return render_template('playlist.html')
    else:
        login_url = sp_oauth.get_authorize_url()
        return redirect(login_url)

# After generating code, Spotify redirects to this endpoint
@app.route('/oauth/callback', methods=['GET'])
def set_token():
    code = request.args['code']
    token_info = sp_oauth.get_access_token(code)
    access_token = token_info['access_token']
    session['access_token'] = access_token
    return render_template('playlist.html')

# Get user inputted playlist
@app.route('/playlist', methods=['POST'])
def playlist():
    access_token = session['access_token']
    sp_api = spotipy.Spotify(access_token)
    uri = request.form['spotify-uri']
    playlist = sp_api.playlist(uri)
    print(playlist)
    return render_template('playlist.html')
    
    