#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                result.append(0)
                continue
            if (not isinstance(my_list_1[i], (int, float)) or
                    not isinstance(my_list_2[i], (int, float))):
                print("wrong type")
                result.append(0)
                continue
            result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        finally:
            pass
    return result
