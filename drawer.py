import curses



def draw_information(stdscr, app_name: str, music_name: str, author: str, folder: str): 
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_YELLOW, -1)
    curses.init_pair(2, curses.COLOR_MAGENTA, -1)
    curses.init_pair(3, curses.COLOR_GREEN, -1)
    curses.init_pair(4, curses.COLOR_CYAN, -1)  
    
    stdscr.clear()
    stdscr.addstr(0, 0, app_name, curses.color_pair(1))
    stdscr.addstr(1, 0, music_name, curses.color_pair(2))
    stdscr.addstr(2, 0, author, curses.color_pair(3))
    stdscr.addstr(3, 0, folder, curses.color_pair(4))
    stdscr.refresh()