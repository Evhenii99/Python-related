def mean(myList): 
    print("Function started!")
    the_mean = sum(myList) / len(myList)
    return the_mean

mymean = mean([0, 3, 4])
print(mymean)