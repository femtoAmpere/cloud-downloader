# cloud-downloader
Download cloud hosted content from links or pages. Currently supported:
* https://dropbox.com
* https://drive.google.com/
* https://mega.nz/
* https://onedrive.live.com/
* https://disk.yandex.com

# usage
```
python main.py {link1} {page1} {link2} {...}
```

# requirements:
**Python 3** 
```
pip install -r requirements.txt
```
**fdupes** _Used for cleanup after downloading._
```
apt install fdupes
```
**megatools** _Downloading files from mega.nz._
```
apt install megatools
```
**Subsystem for Linux** _If you want to clean up and download from mega.nz on Windows._
```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```