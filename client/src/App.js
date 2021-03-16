import React, { Component } from 'react';
import './App.css';
import SpotifyWebApi from 'spotify-web-api-js';
import SpotifyUri from 'spotify-uri';
const spotifyApi = new SpotifyWebApi();

class App extends Component {
  constructor(){
    super();
    const params = this.getHashParams();
    const token = params.access_token;
    if (token) {
      spotifyApi.setAccessToken(token);
    }
    this.state = { loggedIn: token ? true : false}
  }
  getHashParams() {
    var hashParams = {};
    var e, r = /([^&;=]+)=?([^&;]*)/g,
        q = window.location.hash.substring(1);
    e = r.exec(q)
    while (e) {
       hashParams[e[1]] = decodeURIComponent(e[2]);
       e = r.exec(q);
    }
    return hashParams;
  }

  render() {
    if (!this.state.loggedIn)
      return window.location.href = 'http://localhost:3001'; 
    else
      return (<Form />);
  }
}

class Form extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      nowPlaying: { name: 'Not Checked', albumArt: '' , artists: []},
      track: { name: '', albumArt: [] , artists: []}
    }

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});

  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
    let uri = SpotifyUri.parse(this.state.value)
    console.log(uri.id)
    this.getTrack(uri.id)
  }

  getTrack(id){
    spotifyApi.getTrack(id)
      .then((response) => {
        console.log(response)
        this.setState({
          nowPlaying: { 
              name: response.name, 
              albumArt: response.album.images[0].url,
              artists: response.artists
            },
          track: {
            albumArt: response.album.images,
          }
        });
        console.log(this.state.track.albumArt)
      })
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <label>
            Track ID:
            <input type="text" value={this.state.value} onChange={this.handleChange} />
          </label>
          <input type="submit" value="Submit" />
        </form>

        <div>
          Track name: { this.state.nowPlaying.name }<br/>

          {this.state.nowPlaying.artists.map(artist => (
            <div key={artist.id}>
              <span>{artist.name} </span>
            </div>
          ))}
          {this.state.track.albumArt.map(image => (
            <div key={image.url}>
              <img src={image.url} alt=''/>
            </div>
          ))}
        </div>

      </div>

    );
  }
}

export default App;
