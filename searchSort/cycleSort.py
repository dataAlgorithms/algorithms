def cycleSort(vector):

    writes = 0

    # Loop through the vector to find cycles to rotate
    for cycleStart, item in enumerate(vector):

        # Find where to put the item
        pos = cycleStart
        for item2 in vector[cycleStart+1:]:
            if item2 < item:
                pos += 1

        # If the item is already there, this is not a cycle
        if pos == cycleStart:
            continue

        # otherwise, put the item there or right after any duplicates
        while item == vector[pos]:
            pos += 1

        vector[pos], item = item, vector[pos]
        writes += 1

        # rotate the rest of the cycle
        while pos != cycleStart:

            # Find where to put the item
            pos = cycleStart
            for item2 in vector[cycleStart+1:]:
                if item2 < item:
                    pos += 1

            # Put the item there or right after any duplicates
            while item == vector[pos]:
                pos += 1

            vector[pos], item = item, vector[pos]
            writes += 1

    return writes

'''
10 [0, 0, 1, 1, 2, 2, 2, 2, 3.5, 4, 5, 6, 7, 8, 9]
'''
if __name__ == "__main__":

    x = [0, 1, 2, 2, 2, 2, 1, 9, 3.5, 5, 8, 4, 7, 0, 6]
    w = cycleSort(x)
    print w, x
