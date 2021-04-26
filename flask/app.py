import os
from flask import (
    Flask, redirect, render_template, request, url_for, session
)
import spotipy
from spotipy import oauth2
from savify import Savify
from savify.types import Type, Format, Quality
from savify.utils import PathHolder

sav = Savify(api_credentials=(os.getenv('SPOTIPY_CLIENT_ID'), os.getenv('SPOTIPY_CLIENT_SECRET')), path_holder=PathHolder(downloads_path='downloads'))

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

CACHE = '.spotifycache'
sp_oauth = oauth2.SpotifyOAuth(cache_path=CACHE )

@app.route('/', methods=['GET'])
def login():
    token_info = sp_oauth.get_cached_token()
    if token_info and not sp_oauth.is_token_expired(token_info):
        access_token = token_info['access_token']
        session['access_token'] = access_token
        return render_template('playlist.html')
    else:
        login_url = sp_oauth.get_authorize_url()
        return redirect(login_url)

@app.route('/oauth/callback', methods=['GET'])
def set_token():
    code = request.args['code']
    token_info = sp_oauth.get_access_token(code)
    access_token = token_info['access_token']
    session['access_token'] = access_token
    return render_template('playlist.html')

@app.route('/playlist', methods=['POST'])
def playlist():
    access_token = session['access_token']
    sp_api = spotipy.Spotify(access_token)
    uri = request.form['spotify-uri']
    # playlist = sp_api.playlist(uri)
    
    # sav.download(uri)
    return render_template('playlist.html')
    
if __name__ == '__main__':
    app.run(threaded=True, port=5000)