
numbers = []

def only_numbers(function):
    def wrapper(s_input):
        try:
            int(s_input)
        except ValueError:
            print("only numbers, q and p are allowed")
        else:
            function(s_input)
    return wrapper

@only_numbers
def add_number(s):
    numbers.append(s)


while True:
    s = input("add a number, q to quit, p to print: ") 
    if s == "q":
        break
    elif s == "p":
        print(numbers)
    else:
        add_number(s)

