import os
import asyncio
from pydub import AudioSegment
# sound1 = AudioSegment.from_wav('../spleeter/isolated_sounds/amies-Silenced/bass.wav')

isolated_sounds_path = '/Users/coleb/dev/mozart/spleeter/isolated_sounds'

async def create_audio_segment(files, subdir, a):
  for file in files:
    if file.find('.wav') != -1:
      a.append(AudioSegment.from_wav(subdir + '/' + file))

async def main():
  i = 0
  for subdir, dirs, files in os.walk(isolated_sounds_path):
    a = []
    await create_audio_segment(files, subdir, a)
    print(a)
  # overlay0 = a[0].overlay(a[1],position=0)
  # overlay1 = overlay0.overlay(a[2],position=0)
  # overlay2 = overlay1.overlay(a[3],position=0)
  # overlay2.export(str(i) + '.wav', format='wav')
  # i += 1

asyncio.run(main())

# # sound1 6 dB louder
# louder = sound1 + 6

# # Overlay sound2 over sound1 at position 0  (use louder instead of sound1 to use the louder version)
# overlay = sound1.overlay(sound2, position=0)


# # simple export
# file_handle = overlay.export("output.mp3", format="mp3")