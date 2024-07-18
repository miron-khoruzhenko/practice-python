import os
for i in range(3):
  duration = 0.2  # seconds
  freq = 6500  # Hz
  vol = 0.05
  os.system('play -nq -t alsa synth {} sine {} vol {}'.format(duration, freq, vol))
