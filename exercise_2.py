
list_1 = [2, 4, 6, 8, 10]

list_2 = [2, 3, 4, 5, 6]


def eGCD(a, b):

    if b == 0:
        return a
    else:
        return eGCD(b, a%b)


def myGCD(num_of_elements, myList):

    if len(myList) == num_of_elements:
        j = 0
        currentGCD = myList[0]
        while j < num_of_elements - 1:
            currentGCD = eGCD(currentGCD, myList[j+1])
            j += 1

        return currentGCD
    else:
        print("The number of elements argument is not equal to the actual size of the list in the input")


eGCD_1 = myGCD(5, list_1)
eGCD_2 = myGCD(5, list_2)

print(eGCD_1)
print(eGCD_2)
