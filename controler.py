import audio

def play(radio):
    stop()
    audio.play(radio)

def stop():
    audio.stop()

def get_list_radio():
    return list(audio.URL_BY_RADIO.keys())
