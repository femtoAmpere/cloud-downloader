
import os
import subprocess

clean_dir = '.'


def _get_wsl(cmd):
    if os.name == 'nt':
        process_cmd = ['wsl']
    else:
        process_cmd = []
    return process_cmd + cmd


def _clean_fdupes():
    print(subprocess.check_output(
        _get_wsl(["fdupes", "-Srd", "--noprompt", clean_dir])
    ))


def _clean_empty_folders():
    print(subprocess.check_output(
        _get_wsl(["find", clean_dir, "-type", "d", "-empty"])
    ))
    print(subprocess.check_output(
        _get_wsl(["find", clean_dir, "-type", "d", "-empty", "-delete"])
    ))


def cleanup():
    _clean_fdupes()
    _clean_empty_folders()