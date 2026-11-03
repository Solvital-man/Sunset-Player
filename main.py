#libraries
from vlc import * #For audio
from tinytag import TinyTag #For audio tags
import os #exit & update text
from pathlib import Path
import time
import curses

#Files
import configuration
import drawer
#Variables from configuration
Folder = Path(configuration.Folder)
#Text
program_name = "---Sunset player---"

#Variables in this script
has_songs = True
finished = False
is_paused = False
index_music = 0

player = MediaPlayer()
#list of music
music_list = []

for music in Folder.iterdir():
    if music.is_file() and music.suffix.lower() in [".mp3", ".flac", ".ogg", ".wav", ".m4a"]:
        music_list.append(music)

if not music_list:
    print("This folder doesn't have any music!")
    sys.exit()

#Functions
def playing(stdscr):

    #make global this var.
    global is_paused
    global program_name
    global index_music
    global player

    #curses setup
    stdscr.nodelay(True)

    while True:
        #Turn on music
        player.set_mrl(str(music_list[index_music]))

        player.play()

        musics = TinyTag.get(str(music_list[index_music]))
        current_music = "Now playing: " + f"{musics.title or music_list[index_music].name}"
        current_Author = "Author: " + f"{musics.artist or "author that you may know"}"
        current_Folder = "From folder: " + f"{str(Folder)}"
        
        drawer.draw_information(stdscr, program_name, current_music, current_Author, current_Folder)
        while player.get_state() != State.Ended or is_paused:
                
                time.sleep(0.5)
                key = stdscr.getch()
                if key == ord('x') or key == ord("ч"):
                    if is_paused:
                        player.play()
                        drawer.draw_information(stdscr, program_name, current_music, current_Author, current_Folder)
                        is_paused = False
                    else:
                        player.pause()
                        drawer.draw_information(stdscr, program_name, current_music + "[Stopped]", current_Author, current_Folder)
                        is_paused = True
                    time.sleep(0.3)

                if key == ord("c") or key == ord("с"):
                    break

                if key == ord("z") or key == ord("я"):
                    index_music -= 2
                    break
        player.stop()
        index_music = (index_music+1) % len(music_list)


#Checking if main.py is a main file
if __name__ == "__main__":
    curses.wrapper(playing)