def get_picture(count):
    if count == 1:
        return """+
|
|
|
|
|
~~~~~~~"""
    elif count == 2:
        return """+---.
|
|
|
|
|
~~~~~~~"""
    elif count == 3:
        return """+---.
|   |
|
|
|
|
~~~~~~~"""
    elif count == 4:
        return """+---.
|   |
|   O
|
|
|
~~~~~~~"""
    elif count == 5:
        return """+---.
|   |
|   O
|   |
|
|
~~~~~~~"""
    elif count == 6:
        return """+---.
|   |
|   O
| --|
|
|
~~~~~~~"""
    elif count == 7:
        return """+---.
|   |
|   O
| --|--
|
|
~~~~~~~"""
    elif count == 8:
        return """+---.
|   |
|   O
| --|--
|  /
|
~~~~~~~"""
    else:
        return """+---.
|   |
|   O
| --|--
|  / \\
|
~~~~~~~"""
