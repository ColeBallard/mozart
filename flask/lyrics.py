import lyricsgenius
genius = lyricsgenius.Genius()

def get_lyrics(artist, song):
  return genius.search_artist(artist, max_songs=0).song(song)
