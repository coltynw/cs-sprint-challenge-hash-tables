def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    # check for duplicates and remove all. 
    # convert to absolute values
    # check for duplicates again and return them
    
    result = []

    a = list(dict.fromkeys(a))
    #remove duplicates
    
    b = [abs(ele) for ele in a]
    # set to absolute values

    seen = {}
    dupes = []

    for x in b:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dupes.append(x)
            seen[x] += 1

    result = dupes
    # remove duplicates and put them in dupes array

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
