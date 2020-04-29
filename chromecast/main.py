import pychromecast

chromecasts = pychromecast.get_chromecasts()
for cc in chromecasts:
    cc.wait()
    print("%20s: %s" % (cc.device.friendly_name, cc.status.status_text))

cast = next(cc for cc in chromecasts if cc.device.friendly_name == "Wohnung")
cast.wait()

cast.media_controller.play()
cast.start_app()
