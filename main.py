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

from downloader import download, post_process

if not os.path.isfile('downloader.log'): open('downloader.log', 'a+').close()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s *%(levelname)s* %(name)s in %(filename)s.%(funcName)s: %(message)s',
                    handlers=[logging.FileHandler('downloader.log', mode='a'), logging.StreamHandler()])

if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    soup = BeautifulSoup(response.content, "html.parser")

    download.get_soups(soup)

    post_process.cleanup()
