import dropbox
import os
from dropbox.files import WriteMode


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode=WriteMode('overwrite'))


def upload(local_file_path, access_token, dropbox_folder=""):
    transfer_data = TransferData(access_token)

    file_from = local_file_path
    file_to = dropbox_folder + '/' + os.path.basename(local_file_path)

    # API v2
    transfer_data.upload_file(file_from, file_to)
