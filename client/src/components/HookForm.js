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
    const spotifyApi = props.spotify;
    const newUri = uri.replace('spotify:playlist:', '');
    console.log(newUri);
    spotifyApi.getPlaylist(newUri)
      .then(response => {
        console.log(response)
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
