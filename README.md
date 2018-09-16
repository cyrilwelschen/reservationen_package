# Reservationen Package

Package allows to convert and upload file.

## Set up process

* Install package via pip, see below in "pip handling" section
* Create a local working directory
* [since version 0.0.5 can auto-download, see section "install"] (Download files 'start_cron.py', 'cronjob.py' and 'dbf2cyv.py' from [reservationen_package](https://github.com/cyrilwelschen/reservationen_package) into working directory)
* Create 'configs.txt' containing
    * `prot_file_path: /path/to/Prot.dbf`
    * And in analogue format `working_dir`, `dropbox_access_token` and mail credentials
    
#### Modules needed

* python-crontab

Finally:

    `python3 start_cron.py`

### Install

Run the following to auto-download required files:

    import reservationen_package.install as ins
    ins.download_all(git_branch="master")

## pip handling

To create a new pip package version execute:

`python3 setup.py sdist bdist_wheel`

#### Upload package
Upload to pip test with:

`python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*`


#### Download package
Download with:

`python3 -m pip install --index-url https://test.pypi.org/simple/ reservationen_package`

or for a specific version:

`python3 -m pip install --index-url https://test.pypi.org/simple/ reservationen_package==0.0.4`

You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.
