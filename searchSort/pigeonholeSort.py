def pigeonholeSort(list, sort_function):
    max_value = max(map(sort_function, list)) # Find how big the final list has to be
    sorted_list = [None] * max_value # Create a list of that many Nones

    for element in list:
        sorted_list[sort_function(element) - 1] = element # Subtract one because sort_function returns positive ints and lists are 0-indexed

    return [element for element in sorted_list if element is not None] # Filter out Nones and return

def return_same(x):
    return x # This sort function will make the pigeonhole sort ints normally. There's no reason it has to be this function, it just has to return positive ints.

if __name__ == "__main__":
    theSeq = [8, 3, 2, 7, 4, 6, 8]
    print pigeonholeSort(theSeq, return_same)
