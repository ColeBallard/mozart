import React from 'react';
import {
  ChakraProvider,
  Box,
  theme,
  Container,
  Heading
} from '@chakra-ui/react';
import { ColorModeSwitcher } from './components/ColorModeSwitcher';
import HookForm from './components/HookForm';
import AudioPlayer from 'react-h5-audio-player';
import 'react-h5-audio-player/lib/styles.css';
import SpotifyWebApi from 'spotify-web-api-js';
const spotifyApi = new SpotifyWebApi();

function Main(props) {
  return (
    <ChakraProvider theme={theme}>
      <Box textAlign="center">
        <Container maxW="xl" my={4} centerContent>
          <ColorModeSwitcher pos="absolute" right={4} />
          <Heading as="h1" size="4xl" isTruncated>Mozart</Heading>
          <Box padding="4" maxW="3xl">
            <HookForm spotify={props.spotify} />
          </Box>
          <Box mt={4} width="100%">
            <AudioPlayer src="http://example.com/audio.mp3" onPlay={e => console.log("onPlay")} />
          </Box>
        </Container>
      </Box>
    </ChakraProvider>
  );
}

class Spotify extends React.Component {
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
      return (<Main spotify={spotifyApi} />);
  }
}

function App() {
  return (
    <Spotify />
  );
}

export default App;
