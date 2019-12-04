# cloud-downloader
Download cloud hosted content from links or pages. Currently supported:
* https://dropbox.com
* https://drive.google.com/
* https://mega.nz/
* https://onedrive.live.com/
* https://disk.yandex.com

## usage
```
python main.py {link1} {page1} {link2} {...}
```

## Requirements:
**Python 3** 
```
pip install -r requirements.txt
```
**Linux** (optional)
* _**fdupes** Used for cleanup after downloading._
* _**megatools**(megadl) Downloads files from mega.nz._
* _**p7zip-full** Python patoolib uses 7zip._
```
apt install fdupes megatools p7zip-full
```
**Windows** (optional)
* _**Subsystem for Linux** Executing the shell commands on Windows._
* _**7zip** Python patoolib uses 7zip._
```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
https://www.7-zip.org/download.html
```