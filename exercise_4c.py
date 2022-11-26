from timeit import timeit

i_range = 1000000

def list_using_comp():
    # normal list
    return [i+1 for i in range(i_range)]

def gen_object():
    # generator produced iterator
    return (i+1 for i in range(i_range))

"""
def iterate_generator(generator):
    for item in generator:
        pass

def iterate_list(list1):
    for item in list1:
        pass
"""

def iterate_generic(object):
    for item in object:
        pass


object_result = gen_object()
list_result = list_using_comp()

print("time it took to create (iterable / list):")
print(timeit(gen_object, number=1))
print(timeit(list_using_comp, number=1))

print("\n" + "time it took to iterate (iterable / list):")
print(timeit(lambda: iterate_generic(object_result), number=1))
print(timeit(lambda: iterate_generic(list_result), number=1))