import os
import sys

import ffmpeg
from colorama import init

from downloader import downloader

def docs():
    with open("README.md", "r") as f:
        for line in f.readlines():
            print(line)
        
        quit()

def main(argv):
    init()
    if len(argv) <= 1:
        docs()
    
    if argv[1] == "-h" or argv == "--help":
        docs()
        
    url = argv[1]
    for i in range(2, len(argv)):
        if argv[i] == "":
            pass

    downloader(url)

if __name__ == "__main__":
    main(sys.argv)