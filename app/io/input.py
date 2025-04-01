import pandas

def read_console():
    """
    Read input from the console
    :return: input text
    """
    return input('Enter something: ')

def read_file(filepath):
    """
    Read input from a file

    :param filepath: file from which to read input
    :return: information from the file
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def read_file_pandas(filepath):
    """
    Read input from a file using pandas

    :param filepath: file from which to read input
    :return: information from the file
    """
    text = pandas.read_csv(filepath)
    return text.to_string()