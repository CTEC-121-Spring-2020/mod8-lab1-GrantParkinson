"""
CTEC 121
<Grant Parkinson>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""




from graphics import *
from dog import Dog
from msdie import MSDie
import docTest
def main():
    '''
    # mod 7 assignment review
    myDict = {}
    # key - value
    # create element
    myDict["key"] = "value"
    myDict["key"] = "new value"
    print(myDict.keys())
    print(myDict.values())
    print(myDict.items())


    #
    filehandle = open("sample.txt", 'r')
    print()
    readreturn = filehandle.read()
    print(type(readreturn))
    print("*", filehandle.read(), "*")
    filehandle.close()
    print()
    '''
    '''
    print()
    print(5*'All that ')
    print()
    '''
    # section 1
    '''
    win = GraphWin("demo", 1000, 1000)
    myCircle = Circle(Point(500,500), 200)
    myCircle.setFill("green")
    myCircle.draw(win)
    win.getMouse()
    '''
    # section 2
    """
    d = Dog("Dog")
    print(d)
    print(d.getName())
    d.setName("Godzilla")
    print(d.getName())
    d.bark()
    print()
    # section 3
    die = MSDie(12)
    print("numer of sides", die.getSides())
    print("value:", die.getValue())
    die.setValue(5)
    print("value:", die.getValue())
    die.setValue(12)
    print("value:", die.getValue())
    die.roll()
    print("value:", die.getValue())
    die.roll()
    print("value:", die.getValue())
    die.roll()
    print("value:", die.getValue())
    """
    print()
    # print module/file header documention
    print(docTest.__doc__)
    # print class docs
    print(docTest.DocTest.__doc__)
    # print method docs
    print(docTest.DocTest.method.__doc__)
    print()


main()
