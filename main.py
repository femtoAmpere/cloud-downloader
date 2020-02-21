#!/usr/local/bin/python3.6

"""
cloud downloader by femtoAmpere
    2019-2020
"""

import sys
import os
import logging

import requests
from bs4 import BeautifulSoup

from downloader import download, post_process

if not os.path.isfile('downloader.log'): open('downloader.log', 'a+').close()
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s *%(levelname)s* %(name)s in %(filename)s.%(funcName)s (%(threadName)s): %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=os.path.join('downloader.log'),
                    filemode='a')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s'))
logging.getLogger("").addHandler(console)


if __name__ == '__main__':
    for dl in sys.argv[1:]:
        if any(h in str(dl).lower() for h in download.catbox.url_patterns):  # is link
            logging.debug("Downloading from catbox!")
            download.catbox.get_link(dl)
        elif any(h in str(dl).lower() for h in download.discord.url_patterns):  # is link
            logging.debug("Downloading from Discord!")
            download.discord.get_link(dl)
        elif any(h in str(dl).lower() for h in download.dropbox.url_patterns):  # is link
            logging.debug("Downloading from Dropbox!")
            download.dropbox.get_link(dl)
        elif any(h in str(dl).lower() for h in download.gfycat.url_patterns):  # is link
            logging.debug("Downloading from gfycat!")
            download.gfycat.get_link(dl)
        elif any(h in str(dl).lower() for h in download.googledrive.url_patterns):
            logging.debug("Downloading from Google Drive!")
            download.googledrive.get_link(dl)
        elif any(h in str(dl).lower() for h in download.mega.url_patterns):
            logging.debug("Downloading from mega.nz!")
            download.mega.get_link(dl)
        elif any(h in str(dl).lower() for h in download.onedrive.url_patterns):
            logging.debug("Downloading from OneDrive!")
            download.onedrive.get_link(dl)
        elif any(h in str(dl).lower() for h in download.smugsmug.url_patterns):  # is link
            logging.debug("Downloading from smugsmug!")
            download.smugsmug.get_link(dl)
        elif any(h in str(dl).lower() for h in download.uploaddir.url_patterns):  # is link
            logging.debug("Downloading from uploaddir!")
            download.uploaddir.get_link(dl)
        elif any(h in str(dl).lower() for h in download.yandisk.url_patterns):
            logging.debug("Downloading from Yandisk!")
            download.yandisk.get_link(dl)
        else:  # is web page
            response = requests.get(sys.argv[1])
            soup = BeautifulSoup(response.content, "html.parser")

            download.get_soups(soup)

            post_process.cleanup()
