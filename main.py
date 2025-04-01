from app.io.input import *
from app.io.output import *

def main():
    text_console = read_console()
    text_file = read_file('data/input.txt')
    text_file_pandas = read_file_pandas('data/input.txt')

    write_console(text_console)
    write_console(text_file)
    write_console(text_file_pandas)

    write_file('data/output_console.txt', text_console)
    write_file('data/output_file.txt', text_file)
    write_file('data/output_pandas.txt', text_file_pandas)


if __name__ == '__main__':
    main()