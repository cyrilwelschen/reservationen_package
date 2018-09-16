import urllib.request
import os


def download_from_github(branch="master", python_file=None, target_dir="."):
    base = "https://raw.githubusercontent.com/cyrilwelschen/"
    url = "{}reservationen_package/{}/reservationen_package/{}".format(base, branch, python_file)
    print("download start of {}!".format(python_file))
    print(url)
    urllib.request.urlretrieve(url, filename=os.path.join(target_dir, python_file))
    print("download complete of {}!".format(python_file))


def download_all(git_branch="master"):
    current_path = os.getcwd()
    download_from_github(branch=git_branch, python_file="dbf2csv.py", target_dir=current_path)
    download_from_github(branch=git_branch, python_file="cronjob.py", target_dir=current_path)
    download_from_github(branch=git_branch, python_file="start_cron.py", target_dir=current_path)
