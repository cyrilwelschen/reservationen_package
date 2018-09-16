import urllib.request
import os.path


def download_from_github(branch="master", python_file=None, target_dir="."):
    base = "https://raw.githubusercontent.com/cyrilwelschen/"
    url = "{}reservationen_package/{}/reservationen_package/{}".format(base, branch, python_file)
    print("download start of {}!".format(python_file))
    print(url)
    urllib.request.urlretrieve(url, filename=os.path.join(target_dir, python_file))
    print("download complete of {}!".format(python_file))


current_branch = "03_refactoring_for_pip_package"
download_from_github(branch=current_branch, python_file="dbf2csv.py", target_dir="/home/cyril/Desktop")
download_from_github(branch=current_branch, python_file="cronjob.py", target_dir="/home/cyril/Desktop")
download_from_github(branch=current_branch, python_file="start_cron.py", target_dir="/home/cyril/Desktop")
