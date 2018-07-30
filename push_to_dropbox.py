import dropbox
from dropbox.files import WriteMode
import time

TIME_STAMP_FILE = "upload_stamp.txt"
PROT_FILE = "Prot.dbf"
GASTRO_PROT_DIR = "GastroData/"


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode=WriteMode('overwrite'))


def upload(local_dir, filename):
    access_token = 'dropbox_token'
    transfer_data = TransferData(access_token)

    file_from = local_dir + filename
    file_to = '/' + filename  # The full path to upload the file to, including the file name

    # API v2
    transfer_data.upload_file(file_from, file_to)


def make_stamp():
    with open(TIME_STAMP_FILE, "w") as f:
        f.write(time.strftime("%X %d.%m.%y"))


def main():
    make_stamp()
    upload("", TIME_STAMP_FILE)
    upload(GASTRO_PROT_DIR, PROT_FILE)


if __name__ == '__main__':
    main()
