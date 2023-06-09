import pygame
import numpy as np
import math
import time
import threading

pygame.init()

bits = 16
sample_rate = 44100
pygame.mixer.pre_init(sample_rate,bits)

def sine_x(amp, freq, time):
    return int(round(amp * math.sin(2 * math.pi * freq * time)))

class Tone: 
    def sine(freq, duration=1, speaker=None):

        num_samples = int(round(duration * sample_rate))

        sound_buffer = np.zeros((num_samples, 2), dtype=np.int16)
        amplitude = 2 ** (bits - 1) - 1

        for sample_num in range(num_samples):
            t = float(sample_num) / sample_rate

            sine = sine_x(amplitude, freq, t)

            if speaker == 'r': # right speaker
                sound_buffer[sample_num][1] = sine
            elif speaker == 'l': # left speaker
                sound_buffer[sample_num][0] = sine
            else: # both speakers
                sound_buffer[sample_num][0] = sine
                sound_buffer[sample_num][1] = sine

        sound = pygame.sndarray.make_sound(sound_buffer)
        sound.play(loops=1, maxtime=int(duration * 1000))
        time.sleep(duration)

    # play multiple sequencies at once
    @staticmethod
    def create_tone_from_list(freq_list, duration=1, speaker=None):
        freq_threads = []
        for freq in freq_list:
            freq_thread = threading.Thread(target=Tone.sine, args=[freq, duration, speaker])
            freq_threads.append(freq_thread)

        for freq_thread in freq_threads:
            freq_thread.start()
        
        for freq_thread in freq_threads:
            freq_thread.join()
