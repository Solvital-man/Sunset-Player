# Sunset player

## Important note
> This project is still under development. If you encounter any errors or bugs, please open an issue on this repository.

## Description
This is a TUI Sunset player by **Solvital**.
Using libraries(Built-in):
- **os**(for exit)
- **pathlib**(for finding path and using it)
- **curses**(For checking key presses & for terminal rendering)
- **time**(To use sleep method)

Using libraries(Dependencies):
- **python-vlc**(for audio)
- **tinytag**(for audio tags)

## Control playback:
1. **Play/Pause** - Play and Pause your favourite tracks by using `x` key!
2. **Next/Previous** - Change your track if you want by using `z` for previous track and `c` for next track
3. **Shuffle** - if your playlist seems boring, shuffle it by using `s` key!
4. **Exit** - if you want to leave, press `q` key!

## Installation
1. Download Python(Python 3.8+ (uses standard libraries: curses, pathlib))
2. Download vlc player(It's important)
3. Download libraries 
```bash
pip install python-vlc tinytag
```
4. run main.py file
```bash
python main.py
```
5. Enjoy!
