import os


class Configs:

    def __init__(self, config_file_path=None):
        if config_file_path:
            self.config_path = config_file_path
        else:
            self.config_path = input("Enter config file path: ")
        self.configs = {}
        if os.path.exists(self.config_path):
            for c in self.known_configs():
                self.configs[c] = self.get_config_content(c)
        else:
            raise FileNotFoundError("config file not found")

    def get_config_content(self, content):
        config = None
        with open(self.config_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if content in line:
                    config = line.split(": ")[1][:-1]
        if config:
            return config
        else:
            raise LookupError("Config file doesn't contain value for {}.".format(content))

    @staticmethod
    def known_configs():
        return ["dropbox_access_token", "status", "admin", "mail_to", "mail_from", "mail_from_pwd", "prot_file_path",
                "working_dir", "python2_path", "python3_path"]


def config_content(file_path, content=None):
    if os.path.exists(file_path):
        if content:
            with open(file_path, 'r') as f:
                line = f.readline()
                if content in line:
                    return True
    else:
        return False
