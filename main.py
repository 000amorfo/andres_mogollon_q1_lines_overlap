def checkOverlapping(x1, x2, x3, x4):
    if(x1 == x2 and x3 == x4):
        if(x1 == x3):
            return "they overlap"
        else:
            return "NO overlap"
    elif(x1 == x2):
        if(x1 >= x3 and x1 <= x4):
            return "they overlap"
        else:
            return "NO overlap"
    elif(x3 == x4):
        if(x3 >= x1 and x3 <= x2):
            return "they overlap"
        else:
            return "NO overlap"
    else:
        if(x1 >= x3):
            if(x1 <= x4):
                return "they overlap"
            else:
                return "NO overlap"
        elif(x2 >= x3):
            if(x2 <= x4):
                return "they overlap"
            else:
                return "NO overlap"

def checkStructure(coordinates):
    if coordinates[0] != '(' or coordinates[len(coordinates) - 1] != ')':
        print("you need this structure (1,3)")
        return False
    else:
        return True

def extractCoordinates(coordinates):

    acu = ""
    acu2 = 0

    for value in coordinates:
        acu2 = acu2 + 1
        if(acu2 != 1 and acu2 != len(coordinates)):
            acu = acu + value

    coord_x1Tmp = acu.split(",")[0]
    coord_x2Tmp = acu.split(",")[1]

    if(int(coord_x1Tmp) > int(coord_x2Tmp)):
        array.append(int(coord_x2Tmp))
        array.append(int(coord_x1Tmp))
    else:
        array.append(int(coord_x1Tmp))
        array.append(int(coord_x2Tmp))

    return True


def askForData():

    if("one" not in dict):
        print("insert coord 1 ... example (1,5)")
        line1 = input()
        if checkStructure(line1):
            dict["one"] = line1
        else:
            askForData()

    if("two" not in dict):
        print("insert coord 2 ... example (2,6)")
        line2 = input()
        if checkStructure(line2):
            dict["two"] = line2
        else:
            askForData()

dict = {}
array = []
if __name__=='__main__':

    askForData()
    extractCoordinates(dict["one"])
    extractCoordinates(dict["two"])
    result = checkOverlapping(array[0], array[1], array[2], array[3])
    print(result)
