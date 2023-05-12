# TODO: implement the following 3 functions. Use docstrings, whitespace, and comments.

def cocktail_sort(L): pass

def bs_sublist(L, left, right, item): pass

def opt_insertion_sort(L): pass

def insertion_sort(L):
    """Naive insertion sort. Adaptive, but still slow."""
    n = len(L)
    for j in range(n): # go through every item
        for i in range(n - 1 - j, n - 1): # bubble it into a sorted sublist
            if L[i] > L[i+1]:                 # 1 comparison
                L[i], L[i+1] = L[i+1], L[i]   # 2 writes 
            else: break