def only_digits(value):
    try:
        for n in value:
            if not n.isdigit():
                print("Digits only!")
                return False
        return True
    except ValueError:
        print("Digits only!")


def only_letters(value):
    try:
        for n in value:
            if n.isdigit():
                print("Letters only!")
                return False
        return True
    except ValueError:
        print("Letters only!")


def open_file(filename):
    return open(filename)
