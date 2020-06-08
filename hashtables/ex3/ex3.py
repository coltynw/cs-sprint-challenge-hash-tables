def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    # use a double for loop to iterate through the array and use a dictionary to assign keys to all values that appear in all of the subarrays
    
    result = []
    box = {} # box is the dictionary

    for a in arrays: #double for loop 
        for b in a: 
            if b not in box: # if b is not in the dictionary
                box[b] = [] # give that node no key
            else:
                result.append(b) # append b, which is the nodes that have a key, to the resulting list. this will not include the nodes that have no key, because their key is a blank array

    result = list(dict.fromkeys(result)) # remove duplicates



    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
