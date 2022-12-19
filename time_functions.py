import time
from functions import constant_function, line_function, quadratic_function

def time_f(func, arg, n_trials=10):  # uses parameters that allow functions to pass through and time its efficiency
    start = time.time()
    for i in range(n_trials):
        func(arg)
    end = time.time()
    return end - start

def list_function(n):              # checks if an int is in a list
    return -1 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def tuple_function(n):             # checks if an int is in a tuple
    return -1 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)

def string_function(n):            # checks if a character is in a string
    return "z" in "sssssssstttttttttttrrrrrrrrrriiiiiiiiiiiinnnnnnnnnnnnnnnnnnnnnnnng"

def set_function(n):               # checks if an int is in a set
    return -1 in {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}

if __name__ == '__main__':
    # Creates a table of all of the run-times for functions
    print("="*46)
    print(f"{'n':5}{'t_const (ms) ':15}{' t_lin (ms)':15}{'t_quad (ms)':10}")
    print("-"*46)
    for n in [100, 200, 400, 600, 800]:
        t = 5*time_f(constant_function, n)
        t_longer = 5*time_f(line_function, n)
        t_longest = 5*time_f(quadratic_function, n)
        print(f"{n:<5g}{t:<16g}{t_longer:<14g}{t_longest:<10.3g}")
    print("-"*59)
    
    # Creates a table of all of the run-times for built-in collections
    print("="*59)
    print("                   Contains (times in ms)")
    print("-"*59)
    print(f"{'n':5}{'t_list (ms) ':15}{' t_tup (ms)':15}{'t_str (ms)':15}{'t_set (ms)':10}")
    print("-"*59)
    for n in [100, 200, 400, 600, 800]:
        t_list = 5*time_f(list_function, n)
        t_tuple = 5*time_f(tuple_function, n)
        t_str = 5*time_f(string_function, n)
        t_set = 5*time_f(set_function, n)
        print(f"{n:<5g}{t_list:<16g}{t_tuple:<14g}{t_str:<15g}{t_set:<14g}")
    print("-"*59)

