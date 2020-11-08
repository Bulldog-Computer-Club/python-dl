from pytube import YouTube
import logger
import curses
import sys

#TODO move these back into the downloader class
selected_stream = None
stdscr = curses.initscr()
size = 0


class downloader:

    def __init__(self, options):
        curses.start_color()
        self.log = logger.logger()
        try:
            self.video = YouTube(options["url"], on_progress_callback=self.progress)
        except:
            self.log.error("error fetching video", stdscr)
            stdscr.addstr("\npress any key to dismiss: ")
            stdscr.getch()

            curses.endwin()
            sys.exit()
        
        self.log.info("successfully fetched video", stdscr)

        if options["mode"] == None:
            options["mode"] = "mp4"

        self.log.info('downloading "' + self.video.title + '"', stdscr)
        self.selected_stream = self.video.streams.order_by('resolution').filter(progressive=True, file_extension=options["mode"]).last()
        self.size = self.selected_stream.filesize
        self.log.info("downloading " + str(self.size) + " bytes from " + self.video.vid_info_url, stdscr)
        self.selected_stream.download(filename=options["output_name"] if options["output_name"] != None else self.video.title)

        self.log.info("done!", stdscr)
        stdscr.addstr("\npress any key to dismiss: ")
        stdscr.getch()
        curses.endwin()

    def progress(self, chunk, file_handle, bytes_remaining):
        size = self.selected_stream.filesize
        progress = (float(abs(bytes_remaining-size)/size))*float(100)
        self.log.bar(stdscr.getyx()[0], progress, 100, stdscr)