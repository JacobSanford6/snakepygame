import render

TICKSPEED = 30 # amount of times a second that keys are checked, keep lower to better performance and slow down game speed
FRAMERATE = 3  # amount of ticks before rendering a new frame, keep this higher to inscrease performance and slow down game speed

REND = render.Render(TICKSPEED, FRAMERATE)
REND.start()