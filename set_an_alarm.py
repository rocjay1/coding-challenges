import subprocess, platform, time

def set_alarm(t, sound, message):
    time.sleep(t - time.time()) # wait until the desired time, starting now
    # subprocess opens the sound in the default music player for mac oss
    if platform.system() == 'Darwin': 
        subprocess.call(('open', sound))
    print(message)

set_alarm(time.time() + 10, "StarWars3.wav", "Wake up!")