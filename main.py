#!/usr/local/bin/python3.6

"""
cloud downloader by femtoAmpere
    2019
"""

import sys
import os
import logging

import requests
from bs4 import BeautifulSoup

from downloader import download, post_process, url_patterns
from downloader import dropbox, googledrive, mega, onedrive, yandisk

if not os.path.isfile('downloader.log'): open('downloader.log', 'a+').close()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s *%(levelname)s* %(name)s in %(filename)s.%(funcName)s: %(message)s',
                    handlers=[logging.FileHandler('downloader.log', mode='a'), logging.StreamHandler()])

if __name__ == '__main__':
    for dl in sys.argv[1:]:
        if any(h in str(dl).lower() for h in url_patterns.dropbox):  # is link
            logging.debug("Downloading from Dropbox!")
            dropbox.get_link(dl)
        elif any(h in str(dl).lower() for h in url_patterns.googledrive):
            logging.debug("Downloading from Google Drive!")
            googledrive.get_link(dl)
        elif any(h in str(dl).lower() for h in url_patterns.mega):
            logging.debug("Downloading from mega.nz!")
            mega.get_link(dl)
        elif any(h in str(dl).lower() for h in url_patterns.onedrive):
            logging.debug("Downloading from OneDrive!")
            onedrive.get_link(dl)
        elif any(h in str(dl).lower() for h in url_patterns.yandisk):
            logging.debug("Downloading from Yandisk!")
            yandisk.get_link(dl)
        else:  # is web page
            response = requests.get(sys.argv[1])
            soup = BeautifulSoup(response.content, "html.parser")

            download.get_soups(soup)

            post_process.cleanup()
