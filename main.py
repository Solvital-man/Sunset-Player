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

#Functions
#we play
def playing(stdscr):
    global is_paused
    global program_name

    #curses setup
    stdscr.nodelay(True)


    #Finding a music
    for music in Folder.iterdir():

        if music.is_file() and music.suffix.lower() in [".mp3", ".flac", ".ogg", ".wav", ".m4a"]:

                   
            player = MediaPlayer(str(music))
            player.play()
            time.sleep(0.5)

            musics = TinyTag.get(music)
            current_music = "Now playing: " + f"{musics.title or music.name}"
            current_Author = "Author: " + f"{musics.artist or "author that you may know"}"
            current_Folder = "From folder: " + f"{str(Folder)}"
            drawer.draw_information(stdscr, program_name, current_music, current_Author, current_Folder)

            while player.is_playing() or is_paused:
                
                time.sleep(1)
                key = stdscr.getch()
                if key == ord('x'):
                    if is_paused:
                        player.play()
                        drawer.draw_information(stdscr, program_name, current_music, current_Author, current_Folder)
                        is_paused = False
                    else:
                        player.pause()
                        drawer.draw_information(stdscr, program_name, current_music + "[Stopped]", current_Author, current_Folder)
                        is_paused = True
                    time.sleep(0.3)
               
            player.stop()

if __name__ == "__main__":
    curses.wrapper(playing)