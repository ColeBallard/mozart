import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

raw_audio = tf.io.read_file('/Users/coleb/dev/mozart/spleeter/isolated_sounds/Alstad-TheRoomUpstairs/bass.wav')
waveform = tf.audio.decode_wav(raw_audio)