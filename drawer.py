import curses



def draw_information(stdscr, app_name: str, music_name: str, author: str, folder: str, options): 
    #Prefernces 
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_YELLOW, -1)
    curses.init_pair(2, curses.COLOR_MAGENTA, -1)
    curses.init_pair(3, curses.COLOR_GREEN, -1)
    curses.init_pair(4, curses.COLOR_CYAN, -1)  
    curses.init_pair(5, curses.COLOR_BLUE, -1)  

    #analog of print
    stdscr.clear()
    stdscr.addstr(0, 0, app_name, curses.color_pair(1))
    stdscr.addstr(1, 0, music_name, curses.color_pair(2))
    stdscr.addstr(2, 0, author, curses.color_pair(3))
    stdscr.addstr(3, 0, folder, curses.color_pair(4))
    stdscr.addstr(4, 0, options, curses.color_pair(5))
    stdscr.addstr(5, 0, "[x] - Pause | [z] - Prev | [c] - Next | [s] - Shuffle | [r] - Repeat | [q] - Quit", curses.color_pair(5))
    stdscr.refresh()