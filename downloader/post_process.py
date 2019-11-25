
import os
import subprocess


def _get_wsl(cmd):
    if os.name == 'nt':
        process_cmd = ['wsl']
    else:
        process_cmd = []
    return process_cmd + cmd


def _clean_fdupes(folder="."):
    print(subprocess.check_output(
        _get_wsl(["fdupes", "-Srd", "--noprompt", folder])
    ))


def _clean_empty_folders(folder="."):
    print(subprocess.check_output(
        _get_wsl(["find", folder, "-type", "d", "-empty"])
    ))
    print(subprocess.check_output(
        _get_wsl(["find", folder, "-type", "d", "-empty", "-delete"])
    ))


def cleanup(folder="."):
    _clean_fdupes(folder)
    _clean_empty_folders(folder)