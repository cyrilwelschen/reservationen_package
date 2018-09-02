import os


class Configs:

    def __init__(self, config_file_path):
        self.config_path = input("Enter config file path: ")
        if os.path.exists(self.config_path):
            self.get_all_content()
        else:
            raise FileNotFoundError("config file not found")

    def get_config_content(self, content):
        if content:
            with open(self.config_path, 'r') as f:
                line = f.readline()
                if content in line:
                    return True
        else:
            return False

    def get_all_content(self):
        pass

    def known_configs(self):
        return ["dropbox_access_token", ]


def config_content(file_path, content=None):
    if os.path.exists(file_path):
        if content:
            with open(file_path, 'r') as f:
                line = f.readline()
                if content in line:
                    return True
    else:
        return False


def setup_files():
    if not config_file_exists():
        set_whole_config_file()


def config_file_exists():
    return config_content("config.txt", "status")


def configs():
    return ["status", "admin_name"]


def set_whole_config_file():
    with open("config.txt", "w") as f:
        for c in configs():
            c_inp = input("enter {}: ".format(c))
            f.write(c + ":" + c_inp+"\n")


def reset_config_file():
    os.remove("config.txt")
    set_whole_config_file()


def vars_file_found_test():
    return config_content("vars_test.txt", "@mail.co")


if __name__ == "__main__":
    print(vars_file_found_test())
    setup_files()
