def put_together_number():
    """
    Put together the number from keyed in digital characters.
    """
    concatenated_number = ""
    while 1:
        entered_data = input("Введите числовой символ: ")
        if entered_data.isdecimal():
            concatenated_number += entered_data
        elif entered_data in ["stop", "Stop", "STOP"]:
            break
        else:
            continue

    return concatenated_number


print(put_together_number())
