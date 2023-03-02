import os
import uuid


def read_path_vars():
    output = os.getenv("PATH")
    str_arr = output.split(":")
    return str_arr


def add_value_to_path(input, dialogue):
    unique_name = "NEW_VALUE"#str(uuid.uuid1()).replace("-", "")
    value = input.text()
    file1 = open(os.path.expanduser('~/.bashrc'), "a")
    string_to_write = "\n" + unique_name + "=\'" + value + "'\n" + \
                      "export " + unique_name + " \n" + \
                      "export PATH=$PATH:$" + unique_name + "\n"
    file1.write(string_to_write)
    file1.close()
    dialogue.close()

def delete_path_variable():
    unique_name = "NEW_VALUE"
    with open('~/.bashrc', "r") as f:
        lines = f.readlines()
    with open('~/.bashrc', "w") as f:
        for line in lines:
            if unique_name not in line.strip("\n"):
                f.write(line)
