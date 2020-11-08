from pytube import YouTube
import logger
import curses

class downloader:
    def progress_bar(self,stream, chunk,file_handle, bytes_remaining):
        size = self.video.filesize
        i = 0
        while i <= 100:
            progress = i

    def __init__(self, options):
        self.stdscr = curses.initscr()

        curses.start_color()
        log = logger.logger()
        try:
            self.video = YouTube(options["url"], on_complete_callback=self.progress_bar)
        except:
            log.error("error fetching self.video", self.stdscr)
            curses.endwin()
            quit()
        
        log.info("successfully fetched self.video", self.stdscr)

        if options["mode"] == None:
            options["mode"] = "mp4"

        log.info('downloading "' + self.video.title + '"', self.stdscr)
        self.video.streams.order_by('resolution').filter(progressive=True, file_extension=options["mode"]).last().download(filename=options["output_name"] if options["output_name"] != None else self.video.title)
        
        log.bar(self.stdscr.getyx()[0], 50, 100, self.stdscr)

        self.stdscr.addstr("\npress any key to dismiss: ")
        self.stdscr.getch()
        curses.endwin()