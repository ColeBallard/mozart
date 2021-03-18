import { useForm } from "react-hook-form";
import React from "react";
import {
  FormErrorMessage,
  FormLabel,
  FormControl,
  Input,
  Button,
  Flex
} from "@chakra-ui/react";
import axios from "axios";

export default function HookForm(props) {
  const { handleSubmit, errors, register, formState } = useForm();

  function validateURI(value) {
    if (!value) {
      return "Please enter a Spotify Playlist URI.";
    } else if (value.search('spotify:playlist:') === -1) {
      return "Please enter a valid Spotify Playlist URI.";
    } else return true;
  }

  function getPlaylistData(uri) {
    props.spotify.getPlaylist(uri.replace('spotify:playlist:', ''))
      .then(response => {
        console.log(response);
        axios.post('/api/playlist', {
          playlist: JSON.stringify(response)
        }).then(response => {
          console.log(response);
        }).catch(error => {
          console.log(error);
        });
      },
      err => {
        console.log(err)
      });
  };

  function onSubmit(values) {
    return new Promise(resolve => {
      setTimeout(() => {
        getPlaylistData(values.uri);
        resolve();
      }, 500);
    });
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <FormControl isInvalid={errors.uri}>
        <Flex>
          <FormLabel htmlFor="name">Spotify Playlist URI: </FormLabel>
          <Input
            name="uri"
            placeholder="spotify:playlist:"
            ref={register({ validate: validateURI })}
          />
        </Flex>
        <FormErrorMessage>
          {errors.uri && errors.uri.message}
        </FormErrorMessage>
      </FormControl>
      <Button mt={4} colorScheme="teal" isLoading={formState.isSubmitting} type="submit">
        Submit
      </Button>
    </form>
  );
}
