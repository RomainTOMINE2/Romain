def printTriangle(incr, base, a_center):
    for y in range(4):
        etoiles = base + (y*incr)
        print((etoiles*"*").center(a_center))

def printSapin(height):
    center = ((1+(( height-1)*2))+( height*2)) + 2*( height*2)

    for y in range(1, height+1):
        printTriangle(y*2, 1+((y-1)*2), center)
    printbottom(center)


def middle(colo, esp ):

    if esp < 4 or esp > 6:
        if colo == 5:
            result = "0"

            return " "
    if esp < 3 or esp > 5:
        if colo == 3:
            result = "0"

            return " "

def star(Space, Stars):
    for i in range(0, 3):
        if (i<2):
            print(" "*Stars + "*" + " "*Space + "*" + " "*Space + "*")
            Space=Space-2
            Stars=Stars-2
        else :
            print(" "+Stars + "  *")

         print(" "*(Stars-2) + "***" + " " + "***")
        print(" "*Stars + " *")
        Space=Space+1
        Stars=Stars-2

        for i in range(0, 2):
            print(" "*Space + "* " + " "*Space + "|"+ " "+Space + " *" )
            Space=Space+2
            Stars=Stars-2

star(4, 10)





def bottom(colo, esp) -> str:

    if esp < 4 or esp > 8:
        if colo == 0:
            result = "|"
        elif colo == 1:
            result = "0"
        else:
            result = " "
    else:
        return "*"

    if esp < 4:
        return result+" "
    elif esp > 8:
        return " " + result


def printbottom(aligne):
    for colo in range(3):
        result = ""
        for esp in range(13):
            result += bottom(colo, esp)
        print(result.center(aligne))



printSapin(3)
