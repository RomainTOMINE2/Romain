def printTriangle(incr, base, a_center):
    for y in range(4):
        etoiles = base + (y*incr)
        print((etoiles*"*").center(a_center))

def printSapin(height):
    center = ((1+(( height-1)*2))+( height*2)) + 2*( height*2)

    for y in range(1, height+1):
        printTriangle(y*2, 1+((y-1)*2), center)
    printBottom(center)

def Bottom():
    return "*"



def printBottom(aligne):
    for colo in range(3):
        result = ""
        for esp in range(5):
            result += Bottom()
        print(result.center(aligne))



printSapin(3)
