def write_console(text):
    """
    Write output to the console
    :param text: text to write
    :return: None
    """
    print(text)

def write_file(filepath, text):
    """
    Write output to a file

    :param filepath: file to which to write output
    :param text: text to write
    :return: None
    """
    try:
        with open(filepath, 'a', encoding='utf-8') as file:
            file.write(text + '\n')
    except FileNotFoundError:
        raise FileNotFoundError('File not found')
