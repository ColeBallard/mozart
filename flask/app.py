import os
from flask import (
  Flask, redirect, render_template, request, session
)
import spotipy
from spotipy import oauth2
from savify import Savify
from savify.types import Type, Format, Quality
from savify.utils import PathHolder
from savify.logger import Logger
from spleeter.separator import Separator
import lyrics

sav = Savify(api_credentials=(os.getenv('SPOTIPY_CLIENT_ID'), os.getenv('SPOTIPY_CLIENT_SECRET')),quality=Quality.BEST, download_format=Format.WAV, path_holder=PathHolder(downloads_path='../audio/sav_downloads'), skip_cover_art=True, logger=Logger(log_location='info'))

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

CACHE = '.spotifycache'
sp_oauth = oauth2.SpotifyOAuth(cache_path=CACHE)

def validate_playlist(playlist):
  print(playlist)
  if (playlist['tracks']['total'] > 20):
    return -1 # too many tracks
  elif (playlist['tracks']['total'] < 10):
    return -2 # not enough tracks
  for item in playlist['tracks']['items']:
    if(item['track']['duration_ms'] >= 600000):
      return -3 # track duration too long
  return 1 # valid playlist

def make_music(playlist, url):
  print(playlist)
  sav.download(url, query_type=Type.PLAYLIST)
  separator = Separator('spleeter:4stems-16kHz')
  raw_directory = '/Users/coleb/dev/mozart/audio/sav_downloads'
  for file in sorted(os.listdir(raw_directory)):
    filename = os.fsdecode(file)
    if filename.endswith(".wav"):
      separator.separate_to_file(os.path.join(raw_directory, filename), '/Users/coleb/dev/mozart/audio/isolated_sounds')
      continue
    else:
      continue
  
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
  show_alert = False
  access_token = session['access_token']
  sp_api = spotipy.Spotify(access_token)
  url = request.form['spotify-url']
  playl = sp_api.playlist(url)
  valid = validate_playlist(playl)
  if (valid == 1): # valid playlist
    show_alert = False
    make_music(playl, url)
  elif (valid == -1):
    print('too many tracks')
    show_alert = True
    # show too many tracks error message
  elif (valid == -2):
    print('not enough tracks')
    show_alert = True
    # show not enough tracks error message
  elif (valid == -3):
    print('track duration too long')
    show_alert = True
    # show track duration too long error message
  return render_template('playlist.html', show_alert=show_alert)
    
if __name__ == '__main__':
  app.run(threaded=True, port=5000)
  