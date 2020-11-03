from pytube import YouTube
import logger
import curses

class downloader:
    def __init__(self, url, mode="video"):
        self.stdscr = curses.initscr()
        curses.start_color()
        log = logger.logger()
        print()
        try:
            video = YouTube(url)
        except:
            log.error("error fetching video", self.stdscr)
            curses.endwin()
            quit()
        
        log.info("successfully fetched video", self.stdscr)

        if mode == "video":
            log.info('downloading "' + video.title + '"', self.stdscr)
            log.bar(50, 100, self.stdscr)
