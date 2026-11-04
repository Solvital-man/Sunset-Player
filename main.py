#libraries
from vlc import * #For audio
from tinytag import TinyTag #For audio tags
import os #exit & update text
from pathlib import Path
import time
import curses
import sys

#Files
import configuration
import drawer
import methods

#Variables from configuration
Folder = Path(configuration.Folder)
#Text
program_name = "---Sunset player---"

#Variables
current_index = 0
#Options in this script
finished = False
is_paused = False
index_music = 0
is_shuffled = False
has_folder = True
player = MediaPlayer()
#list of music
music_list = []

for music in Folder.iterdir():
    if music.is_file() and music.suffix.lower() in [".mp3", ".flac", ".ogg", ".wav", ".m4a"]:
        music_list.append(music)

non_shuffled = music_list.copy()

if not music_list:
    print("Error: No music files found, or the folder path is invalid.")
    print("Advice: Check configuration.py file!")
    sys.exit()

#Functions
def playing(stdscr):

    #make global this var.
    global is_paused
    global program_name
    global index_music
    global player
    global is_shuffled
    global non_shuffled
    global music_list
    #curses setup
    drawer.setup_drawers(stdscr)
    stdscr.nodelay(True)

    while True:
        #Turn on music
        player.set_mrl(str(music_list[index_music]))

        player.play()

        musics = TinyTag.get(str(music_list[index_music]))
        current_music = str("Now playing: " + f"{musics.title or music_list[index_music].name}")
        current_Author = str("Author: " + f"{musics.artist or "author that you may know"}")
        current_Folder = str("From folder: " + f"{str(Folder)}")
        options = str(f"Shuffle: [{is_shuffled}], Always Repeat")
        drawer.draw_information(stdscr, program_name, current_music, current_Author, current_Folder, options)
        
        while player.get_state() != State.Ended or is_paused:
                
                time.sleep(0.5)
                try:
                    key = stdscr.get_wch()
                except curses.error:
                    key = None
                if key == 'x' or key == "ч":
                    if is_paused:
                        player.play()
                        drawer.draw_information(stdscr, program_name, current_music, current_Author, current_Folder, options)
                        is_paused = False
                    else:
                        player.pause()
                        drawer.draw_information(stdscr, program_name, current_music + "[Stopped]", current_Author, current_Folder, options)
                        is_paused = True
                    time.sleep(0.3)

                if key == "s" or key == "ы":
                    if not(is_shuffled):
                        current_index = index_music
                        music_list = methods.Shuffle(music_list)
                        is_shuffled = True
                    else:
                        is_shuffled = False
                        music_list = non_shuffled
                    options = str(f"Shuffle: [{is_shuffled}], Always Repeat")
                    drawer.draw_information(stdscr, program_name, current_music, current_Author, current_Folder, options)

                if key == "c" or key == "с":
                    break
                if key == "z" or key == "я":
                    index_music -= 2
                    break
                if key == "q" or key == "й":
                    sys.exit()

        player.stop()
        index_music = (index_music+1) % len(music_list)

#Checking if main.py is a main file
if __name__ == "__main__":
    curses.wrapper(playing)