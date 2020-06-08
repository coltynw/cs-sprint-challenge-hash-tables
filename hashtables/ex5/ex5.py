# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    # this one was as easy as just double for looping through and appending the matches, but since the test was super long I had to redo it with a dictionary and splitting up the array

    # result = []

    # for q in queries:
    #     for f in files:
    #         if q in f:
    #             result.append(f)


    



    # long test solution

    result = []
    box = {} # box is dictionary

    for f in files:
        split = f.split("/") # split the array up at the /
        name = split[-1] # take the last part

        if name not in box: # make new spot in dictionary
            box[name] = []
        
        box[name].append(f) # add to dictionary with filename as [key]
    
    for q in queries: 
        if q in box: # if queries is in the dictionary add it to result
            result.extend(box[q]) # add to end

    


    return result



if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
