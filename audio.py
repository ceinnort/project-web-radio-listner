import vlc

URL_BY_RADIO = {"France Inter" : "https://icecast.radiofrance.fr/franceinter-hifi.aac", "FIP Rock" : 'http://direct.fipradio.fr/live/fip-webradio1.mp3', "RTL" : "https://icecast.rtl.fr/rtl-1-44-128", "RTL 2" : "https://rtl-radio.cdn-live.6play.fr/out/u/6play/rtl2_audio_c_1.m3u8", "Europe 1" : "", "Fun Radio" : "https://icecast.funradio.fr/fun-1-44-128?id=webFUNRADIO&aw_0_req.userConsent=BO0oF_uO0oGDaAHABBFRDG-AAAAvRrv7__7-_9_-_f__9ujzOr_v_f__32ccL59v_h_7v-_7fi_-1jV4u_1vft9yfk1-5ctDztp507iakivXmqdeZ1v_nz3_9phPr8k89r6337Ew_v8_v8b7BCJJAAGrc8KA"}

player = vlc.MediaPlayer()

def play(radio):
    global player
    player = vlc.MediaPlayer(URL_BY_RADIO[radio])
    n = player.play()

def stop():
    player.stop()

#play("France Inter")
