import tinytag

tag = tinytag.TinyTag.get('music\meherbaan.mp3',image=True)
#image_data = tag.get_image()

album= tag.album                        # album as string
artist=tag.artist                       # artist name as string
#audio_offset= tag.audio_offset         # number of bytes before audio data begins
#bitrate= tag.bitrate                   # bitrate in kBits/s
#duration=tag.duration                  # duration of the song in seconds
#filesize=tag.filesize                  # file size in bytes
genre=tag.genre                         # genre as string
#samlerate=tag.samplerate               # samples per second
title=tag.title                         # title of the song
#track=tag.track                        # track number as string
#track_total= tag.track_total           # total number of tracks as string
year=tag.year                           # year or data as string
