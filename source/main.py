import os
import sys

import ffmpeg

from downloader import downloader

def docs():
    with open("README.md", "r") as f:
        for line in f.readlines():
            print(line)
        
        quit()

def main(argv):
    if len(argv) <= 1:
        docs()
    
    if argv[1].lower() == "-h" or argv[1].lower() == "--help":
        docs()

    options = {"mode" : None, "output_name" : None}
    for i in range(2, len(argv)):
        if argv[i - 1].lower() == "-o":
            options["output_name"] = argv[i]
            continue
        elif argv[i][0] != "-":
            options["url"] = argv[i]
        elif argv[i].lower() == "-mp4":
            options["mode"] = argv[i].split("-")[1]
        else:
            options[argv[i].split("-")[1]] = True
            

    downloader(options)

if __name__ == "__main__":
    main(sys.argv)