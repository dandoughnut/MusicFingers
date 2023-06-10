from utils import NOTE_MAP
from Tone import Tone
import threading
import time

class Note:
    
    def __init__(self, cooridnates, duration=1):
        
        # TODO: change the default duration to the duration of the frame
        
        # make sure the note string starts with a uppercase letter to match those in note_map.json 
   
        self.note_str = self.map_coordinates_to_note_str(cooridnates[0], cooridnates[1])

        self.duration = duration
        self.freq = NOTE_MAP[self.note_str] # get the frequency of the note from the note map

        print(self.note_str)

    def map_coordinates_to_note_str(self, x, y):
        image_height = 280 # TODO: change this to the height of the frame
        image_width = 280 # TODO: change this to the width of the frame
        delta_h = image_height / 7
        delta_w = image_width / 9

        if x <= delta_h:
            letter = 'C'
        elif x <= delta_h * 2:
            letter = 'D'
        elif x <= delta_h * 3:
            letter = 'E'
        elif x <= delta_h * 4:
            letter = 'F'
        elif x <= delta_h * 5:
            letter = 'G'
        elif x <= delta_h * 6:
            letter = 'A'
        elif x <= delta_h * 7:
            letter = 'B'
        
        if y <= delta_w:
            octave = '0'
        elif y <= delta_w * 2:
            octave = '1'
        elif y <= delta_w * 3:
            octave = '2'
        elif y <= delta_w * 4:
            octave = '3'
        elif y <= delta_w * 5:
            octave = '4'
        elif y <= delta_w * 6:
            octave = '5'
        elif y <= delta_w * 7:
            octave = '6'
        elif y <= delta_w * 8:
            octave = '7'
        elif y <= delta_w * 9:
            octave = '8'
        
        return letter + octave        

    def play(self, speaker=None):
        Tone.sine(self.freq, duration=self.duration, speaker=speaker)

    @staticmethod
    def rest(duration):
        time.sleep(duration)

    # method to play multiple notes at the same time
    @staticmethod
    def play_chord(notes_list):
        note_threads = []

        for note in notes_list:
            note_thread = threading.Thread(target=note.play)
            note_threads.append(note_thread)

        for note_thread in note_threads:
            note_thread.start()

        for note_thread in note_threads:
            note_thread.join()
