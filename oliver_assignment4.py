import sys
import timeit

FILENAME = "eng_vocab.txt"

# timer decorator
def timer(function):
    def wrapper():
        time_start = timeit.default_timer()
        result = function()
        time_stop = timeit.default_timer()
        print(f"It took {(time_stop - time_start):.7f} s to run {function.__name__}")
        return result
    return wrapper

# context manager
class MyFileContextManager:
    def __init__(self, filename, operation):
        self._filename = filename
        self._operation = operation

    def __enter__(self):    # runs when using the 'with' keyword
        try:
            self._file = open(self._filename, self._operation)
            return self._file
        except FileNotFoundError:
            print("File not found")
            self.__exit__()     # close the context manager

    def __exit__(self, type, value, traceback):
        self._file.close()


def my_genrator(file):
    for item in file:
        yield item

@timer
def read_generator():
    with MyFileContextManager(FILENAME, "r") as file:
        generator = my_genrator(file)
        for line in generator:
            pass
        return generator

@timer
def read_list():
    with MyFileContextManager(FILENAME, "r") as file:
        return file.read().splitlines()
    
    
def main():
    try:
        text_list = read_list()
        text_generator = read_generator()
        print(text_generator)

        print(sys.getsizeof(text_list), "Bytes are used by the list")
        print(sys.getsizeof(text_generator), "Bytes are used by the generator")
    except Exception:
        print("something is wrong")


if __name__ == "__main__":
    main()
