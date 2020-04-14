x=[1,2,3]
y=[4,5]

def outer_product (x,y):
    # simplifying the list lengths
    lengthY = len(y)  # len =2
    lengthX = len(x)  # len =3
    answer = []       # later answer
    for i in range(lengthX):
        # this will reset everyLoop to be later appended
        listOne = []
        # smaller loop that is for the "list" with in the list(main list)
        for j in range(lengthY):
            calc = (x[i] * y[j]) # single digit
            listOne.append(calc) # appended to the temporary list that is y
        answer.append(listOne)   # after appending to the temp list, the finished (list witn in list) gets appendix
    return answer
z=outer_product(x,y);print(z)