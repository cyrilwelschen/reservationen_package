import os


def file_found(file_path, content=None):
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
    return file_found("config.txt", "status")


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
    return file_found("vars_test.txt", "@mail.co")


if __name__ == "__main__":
    print(vars_file_found_test())
    setup_files()
