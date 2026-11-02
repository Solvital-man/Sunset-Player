#libraries
from colorama import Fore, Style, init #For style & color
from vlc import * #For audio
from tinytag import TinyTag #For audio tags
import os #exit & update text
from pathlib import Path
import time
import keyboard

#Files
import configuration

#init
init(autoreset = True)

#Variables from configuration
Folder = Path(configuration.Folder)
#Text
program_name = Fore.YELLOW + "---Sunset player---"

#Variables in this script
has_songs = True
finished = False
is_paused = False
#Functions
#Clear
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
#we play
def playing():
    #Finding a music
    for music in Folder.iterdir():

        if music.is_file() and music.suffix.lower() in [".mp3", ".flac", ".ogg", ".wav", ".m4a"]:

                   
            player = MediaPlayer(str(music))
            player.play()
            time.sleep(0.5)

            musics = TinyTag.get(music)
            current_music = "Now playing: " + Fore.MAGENTA + f"{musics.title or music.name}"
            current_Author = "Author: " + Fore.GREEN + f"{musics.artist or "author that you may know"}"
            current_Folder = "From folder: " + Fore.CYAN + f"{str(Folder)}"
            clear_screen()
            print(program_name)
            print(current_music)
            print(current_Author)
            print(current_Folder)

            while player.is_playing() or is_paused:
                time.sleep(1)
                if keyboard.is_pressed("x"):
                    if is_paused:
                        player.play()
                        clear_screen()
                        print(program_name)
                        print(current_music)
                        print(current_Author)
                        print(current_Folder)
                        is_paused = False
                    else:
                        player.stop()
                        clear_screen()
                        print(program_name + "(stopped)")
                        print(current_music)
                        print(current_Author)
                        print(current_Folder)
                        is_paused = True
                    time.sleep(0.3)

            player.stop()
playing()
curses.wrapper(main)