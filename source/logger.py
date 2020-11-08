import curses

class logger:
    def __init__(self):
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_RED, -1)
        curses.init_pair(2, curses.COLOR_YELLOW,-1)
        curses.init_pair(3, curses.COLOR_GREEN, -1)

    def error(self, text, scr):
        scr.addstr("[ERROR] ", curses.color_pair(1))
        scr.addstr(text + "\n", curses.color_pair(2))
        scr.refresh()
    
    def info(self, text, scr):
        scr.addstr("[info] ", curses.color_pair(3))
        scr.addstr(text + "\n", curses.color_pair(2))
        scr.refresh()

    def bar(self, pos, x, y, scr):
        retstr = []
        for i in range(0, y):
            if i <= x:
                retstr.append("=")
            else:
                retstr.append("-")
        scr.move(pos, 0)
        scr.addstr("|" + "".join(retstr) + "|" + "\n")
        scr.refresh()