import csv

from pynn import NearestNeighborIndex

print("**************************************************************************")
print("***************** Find Nearest Neighbor **********************************")
print("**************************************************************************\n")

userInputLoop = True
haystack = []

while userInputLoop == True:
    userChoice = int(input("Please Enter how you would like to enter your data...\n1: Manually, ex 1,2 3,4\n2: from csv file, ex /path/to/file\nAny other valid whole number: Exit\nChoice: "))
    if type(userChoice) is not int:
        print("invalid choice, please try again")
    elif userChoice == 1:
        haystack = input("Please enter data in pairs with a comma seperation and a space between points, ex 0,0 1,1 2,2\n")
        haystack = haystack.split(" ")
        for i, straw in enumerate(haystack):
            try:
                tempConv = tuple([int(i) for i in straw.split(',')])  
                haystack[i] = tempConv
            except:
                print("Error converting point:", straw)
        userInputLoop = False
    elif userChoice == 2:
        filePath = input("Please enter file path in relation to this current directory or exact\nPath: ")
        try:
            with open(filePath, encoding='utf-8-sig', mode='r') as file:
                csvFile = csv.reader(file)
                for lines in csvFile:
                    node = (tuple([int(s) for s in lines[0].split(',')]))
                    haystack.append(node)
            userInputLoop = False
        except OSError as e:
            print("Error with file: ", ) 
        except Exception as e:
            print("Error Reading file: ", e)
            userInputLoop = False
    else:
        print("Have a nice day!")
        userInputLoop = False

if len(haystack) > 0:
    searching = True
    uut = NearestNeighborIndex(haystack)
    print("Data inserted," , end='')
    while searching:
        queryPoint = input("Please enter a data point to find nearest neighbor: ")
        result = uut.find_nearest(tuple([int(i) for i in queryPoint.split(',')]))

        if result is not None:
            print("Found nearest point at: ", result)
        else:
            print("Unable to find nearest point")
        searchAgain = input("Search for another point y/n? ")
        if searchAgain.lower() == 'n' or searchAgain.lower() == 'no':
            print("Have a nice day!")
            searching = False


