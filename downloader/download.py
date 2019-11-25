import os

from send2trash import send2trash

import logging

import requests
import urllib
import re

from downloader import url_patterns
from zipfile import ZipFile
import patoolib

logger = logging.getLogger('file handling')


def get_soups(soup):
    dropbox.get_soup(soup)
    googledrive.get_soup(soup)
    mega.get_soup(soup)
    # onedrive.get_soup(soup)
    yandisk.get_soup(soup)


# Number the filename if it exists already.
def rotate_name(filename):
    n = 1
    while filename in os.listdir('.'):
        fname, ext = os.path.splitext(filename)
        fname = fname + "_{}".format(n)
        if ext:
            fname = fname + ext
        if fname not in os.listdir('.'):
            return fname
        n += 1
    return filename


# unzip/unrar files
def unpack(filename, remove_file=False):
    fname, ext = os.path.splitext(filename)
    ext = ext.lower()
    extract_dir = rotate_name(fname)
    extracted = False
    if ext == ".zip":
        os.mkdir(extract_dir)
        with ZipFile(filename, 'r') as zf:
            zf.extractall(path=extract_dir)
            zf.close()
        extracted = True
    elif ext in [".rar", ".7z"]:  # requires to have 7zip installed
        os.mkdir(extract_dir)
        patoolib.extract_archive(filename, outdir=extract_dir)
        extracted = True
    if remove_file and extracted:
        # os.remove(filename)
        send2trash(filename)


def get_filename(response, fname=None):
    logger.debug("Content disposition: " + str(response.headers["content-disposition"]))
    if not fname:
        try:
            fname = urllib.parse.unquote(
                re.findall("filename\\*=UTF-8''(.+)", response.headers['content-disposition'])[0]
            )
        except:
            fname = None
    if not fname:
        try:
            fname = re.findall("filename=(.+)", response.headers['content-disposition'])[0].replace('"', '')
        except:
            fname = None
    if not fname:
        logger.warning("Could not get filename from html headers. Using fallback..")
        fname = "file.ext"
    logger.debug('Found filename ' + fname)
    return rotate_name(fname)


# Download a file with automatic naming.
def download(url):
    url = str(url).replace('http://https://', 'https://', 1)  # http://https:// sometimes seems to happen?
    try:
        response = requests.get(url, allow_redirects=True)
    except:
        log_failed_download(url)
        return False
    fname = get_filename(response)
    logger.info('Downloading ' + url + ' to ./' + fname)
    with open(fname, 'wb') as f:
        f.write(response.content)
        f.close()
    unpack(filename=fname, remove_file=True)


def log_failed_download(link):
    if any(pattern in link for pattern in url_patterns.dropbox):
        filename = "dropbox.txt"
    elif any(pattern in link for pattern in url_patterns.googledrive):
        filename = "gdrive.txt"
    elif any(pattern in link for pattern in url_patterns.mega):
        filename = "mega.nz.txt"
    elif any(pattern in link for pattern in url_patterns.onedrive):
        filename = "onedrive.txt"
    elif any(pattern in link for pattern in url_patterns.yandisk):
        filename = "yadi.sk.txt"
    else:
        filename = "download.txt"
    logger.error('Failed to download ' + str(link) + '. Saving to link to ' + filename + ' instead')
    with open(filename, 'a+') as file:
        file.write(str(link) + '\n')
        file.close()
