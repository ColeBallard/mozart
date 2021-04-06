from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, session
)
import spotipy
from spotipy import oauth2

bp = Blueprint('mozart', __name__)

CACHE = '.spotifycache'
# Reads client id and client secret from environment variables
sp_oauth = oauth2.SpotifyOAuth(cache_path=CACHE )

@bp.route('/', methods=['GET'])
def login():
    # If auth token is already cached and not expired, use that else redirect
    # user to login or refresh token
    token_info = sp_oauth.get_cached_token()
    if token_info and not sp_oauth.is_token_expired(token_info):
        access_token = token_info['access_token']
        session['access_token'] = access_token
        return redirect(url_for('mozart.playlist'))
    else:
        login_url = sp_oauth.get_authorize_url()
        return redirect(login_url)

# After generating code, Spotify redirects to this endpoint
@bp.route('/oauth/callback', methods=['GET'])
def set_token():
    code = request.args['code']
    token_info = sp_oauth.get_access_token(code)
    access_token = token_info['access_token']
    session['access_token'] = access_token
    return redirect(url_for('mozart.playlist'))

# Get user inputted playlist
@bp.route('/playlist', methods=['GET'])
def playlist():
    access_token = session['access_token']
    sp_api = spotipy.Spotify(access_token)

    return render_template('playlist.html')