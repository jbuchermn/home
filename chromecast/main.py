import pychromecast
import time

chromecasts = pychromecast.get_chromecasts()
cast = next(cc for cc in chromecasts if cc.device.friendly_name == "Wohnung")
cast.wait()

mc = cast.media_controller
mc.play_media('https://www.bensound.com/bensound-music/bensound-summer.mp3', 'audio/mp3')

print("Block...")
mc.block_until_active()
print("...%s" % mc.status)

print("Pause...")
mc.pause()
print("...%s" % mc.status)

time.sleep(5)

print("Play...")
mc.play()
