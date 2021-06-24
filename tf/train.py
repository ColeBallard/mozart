import tensorflow as tf

raw_audio = tf.io.read_file('/Users/coleb/dev/mozart/audio/isolated_sounds/Alstad - The Room Upstairs/bass.wav')
waveform = tf.audio.decode_wav(raw_audio)