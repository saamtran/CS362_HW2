import math


def printLeapYear(printYearStatement):
    print(" === " + printYearStatement + " is a leap year!")

def notLeapYearPrint(printYearStatement):
    print(" === " + printYearStatement + " is not a leap year!")

def isLeapYearCheck(printYearStatement, status):
    if status == 1:
        printLeapYear(printYearStatement)

    else:
        notLeapYearPrint(printYearStatement)


def mainFunction():
    status = 0
    year = input(" === Please enter a year: ")
    printYearStatement = str(year)
    print(" === The year you chose is " + printYearStatement)

    if year < 0:
        isLeapYearCheck(printYearStatement, status)

    else:
        if year > 3:
            if year % 4 == 0:
                status = 1
                if year >= 100:
                    if year % 100 == 0:
                        status = 0
                        if year >= 400:
                            if year % 400 == 0:
                                status = 1
                                isLeapYearCheck(printYearStatement, status)
                            else:
                                status = 0
                                isLeapYearCheck(printYearStatement, status)
                        else:
                            status = 0
                            isLeapYearCheck(printYearStatement, status)
                    else:
                        status = 1
                        isLeapYearCheck(printYearStatement, status)
                else:
                    status = 1
                    isLeapYearCheck(printYearStatement, status)
            else:
                status = 0
                isLeapYearCheck(printYearStatement, status)
        else:
            status = 0
            isLeapYearCheck(printYearStatement, status)



mainFunction()
