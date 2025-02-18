#!/usr/bin/python3


import dis

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as file:
        bytecode = file.read()
    
    names = dis.get_instructions(bytecode)
    
    valid_names = [name for name in dir() if not name.startswith("__")]

    valid_names.sort()

    for name in valid_names:
        print(name)
