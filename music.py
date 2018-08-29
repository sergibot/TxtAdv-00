from pygame import mixer 

mixer.init()
mixer.music.load('./media/Her.mp3')
mixer.music.play()

import time
while True:
    print("This prints once a minute.")
    time.sleep(60)
# for more info: http://www.pygame.org/docs/ref/music.html



