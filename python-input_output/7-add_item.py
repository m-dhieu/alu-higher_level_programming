#!/usr/bin/python3


"""Script to add arguments to a list and save as JSON."""

def to_json_string(my_obj):

def dict_to_json(d):

def list_to_json(lst):

def save_to_json_file(my_obj, filename):

def load_from_json_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            json_str = f.read()
            return eval(json_str)
    except FileNotFoundError:
        return []

def add_and_save(*args):
    try:
        existing_list = load_from_json_file("add_item.json")
        existing_list.extend(args)
        save_to_json_file(existing_list, "add_item.json")
    except Exception as e:
        print(f"Error: {e}")

# Example
add_and_save("arg1", "arg2", "arg3")
