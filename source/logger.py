import curses

class logger:
    def __init__(self):
        self.lines = 0
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_RED, -1)
        curses.init_pair(2, curses.COLOR_YELLOW,-1)
        curses.init_pair(3, curses.COLOR_GREEN, -1)

    def error(self, text, scr):
        self.lines += 1
        scr.addstr(self.lines, 0, "[ERROR] ", curses.color_pair(1))
        scr.addstr(text + "\n", curses.color_pair(2))
        scr.refresh()
    
    def info(self, text, scr):
        self.lines += 1
        scr.addstr(self.lines, 0, "[info] ", curses.color_pair(3))
        scr.addstr(text + "\n", curses.color_pair(2))
        scr.refresh()

    def bar(self, pos, x, y, scr):
        x = int(abs(x))
        y = int(abs(y))
        retstr = []
        for i in range(0, y):
            if i <= x:
                retstr.append("=")
            else:
                retstr.append("-")
        res = str(x) + "%" + "|" + "".join(retstr) + "|" + "\n"

        # python doesnt like addstr for some reason :/
        try:
            scr.addstr(scr.getmaxyx()[0] - 1, 1, res)
        except:
            pass

        scr.refresh()