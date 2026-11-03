#libraries
from vlc import * #For audio
from tinytag import TinyTag #For audio tags
import os #exit & update text
from pathlib import Path
import time
import curses

#Files
import configuration

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

    #curses setup
    stdscr.nodelay(True)
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_YELLOW, -1)
    curses.init_pair(2, curses.COLOR_MAGENTA, -1)
    curses.init_pair(3, curses.COLOR_GREEN, -1)
    curses.init_pair(4, curses.COLOR_CYAN, -1)

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
            stdscr.clear()
            stdscr.addstr(0, 0, program_name, curses.color_pair(1))
            stdscr.addstr(1, 0, current_music, curses.color_pair(2))
            stdscr.addstr(2, 0, current_Author,curses.color_pair(3))
            #stdscr.addstr(3, 0, current_Folder,curses.color_pair(4))
            stdscr.refresh()

            while player.is_playing() or is_paused:
                
                time.sleep(1)
                key = stdscr.getch()
                if key == ord('x'):
                    if is_paused:
                        player.play()
                        stdscr.clear()
                        stdscr.addstr(0, 0, program_name, curses.color_pair(1))
                        stdscr.addstr(1, 0, current_music, curses.color_pair(2))
                        stdscr.addstr(2, 0, current_Author,curses.color_pair(3))
                        #stdscr.addstr(3, 0, current_Folder,curses.color_pair(4))
                        stdscr.refresh()
                        is_paused = False
                    else:
                        player.pause()
                        stdscr.clear()
                        stdscr.addstr(0, 0, program_name, curses.color_pair(1))
                        stdscr.addstr(1, 0, current_music + "[Stopped]", curses.color_pair(2))
                        stdscr.addstr(2, 0, current_Author,curses.color_pair(3))
                        #stdscr.addstr(3, 0, current_Folder,curses.color_pair(4))
                        stdscr.refresh()
                        is_paused = True
                    time.sleep(0.3)
               
            player.stop()
curses.wrapper(playing)