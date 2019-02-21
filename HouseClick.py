

#                 HOUSE CLICKS.


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

from graphics import *
from math import *

win = GraphWin("House-Click", 700, 500)
win.setCoords(0, 0, 70, 70)

def nameTitle():
    T = Text(Point(60,67), "Joan Quintero")
    T.setSize(6)
    T.draw(win)
    T.setSize(15)
    T.setFill('Silver')
    T = Text(Point(60,65), " ExtraCredit: House-Click")
    T.setSize(5)
    T.draw(win)
    T.setSize(15)
    T.setFill('Silver')   
nameTitle()

def draw(NametobeDRAWN):
    NametobeDRAWN.draw(win)
    
def undraw(NameWhatToRemove):
    NameWhatToRemove.undraw()

T = Text(Point(35,50), "This Program Will Draw a House Based On User Clicks")
T.setFill('Blue')
draw(T)

def introTextLoop(n,z):
    for i in range(n):
        T.setSize(z)
        
introTextLoop(65,20)
introTextLoop(5,19)
introTextLoop(5,18)
introTextLoop(25,17)
introTextLoop(5,16)
introTextLoop(5,15)
introTextLoop(20,14)
introTextLoop(5,13)
introTextLoop(5,12)
introTextLoop(5,11)
introTextLoop(5,10)

undraw(T)


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Suggestive Instructions Recquiring Action from User
T = Text(Point(25,5), "Click anywhere for your first set of points")
T.setSize(15)
draw(T)
T.setFill('Red')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# After-User-Action Output
UserClick1 = win.getMouse()
x1 = UserClick1.getX()
y1 = UserClick1.getY()
undraw(T)


GuideLine = Line(Point(0, 24), Point(33, 24))
GuideText = Text(Point(17,25.5), "Why don't you choose values inside?")
GuideText.setSize(15)
GuideText.setFill('Red')
print("x1",x1)
print("y1",y1)
Again = Text(Point(25, 20), "Click again within...")
AgainLine = Line(Point(33, 24), Point( 33, 0))
Again.setSize(15)
while (y1 >= 24) or x1 >= 33:
    draw(GuideLine)
    draw(GuideText)
    draw(Again)
    draw(AgainLine)
    UserClick1 = win.getMouse()
    x1 = UserClick1.getX()
    y1 = UserClick1.getY()
    undraw(GuideText)
    undraw(GuideLine)
    undraw(Again)
    undraw(AgainLine)

    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
T = Text(Point(30,65), "Click another coordinate, try getting a bigger coordinate for X and Y.")
T.setSize(15)
draw(T)
T.setFill('Red')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
UserClick2 = win.getMouse()
x2 = UserClick2.getX()
y2 = UserClick2.getY()
undraw(T)


GuideLine2 = Line(Point(40, 70), Point(40, 50))
GuideText2 = Text(Point(54,48), "Why don't you choose values inside?")
GuideText2.setSize(15)
GuideText2.setFill('Red')
print("x2",x2)
print("y2",y2)
Again2 = Text(Point(55, 55), "Click again within...")
AgainLine2 = Line(Point(40, 50), Point(70, 50))
Again2.setSize(15)

while x2 <= 40 or y2 <= 50:
        draw(GuideLine2)
        draw(GuideText2)
        draw(Again2)
        draw(AgainLine2)
        UserClick2 = win.getMouse()
        x2 = UserClick2.getX()
        y2 = UserClick2.getY()
        undraw(GuideText2)
        undraw(GuideLine2)
        undraw(Again2)
        undraw(AgainLine2)

BaseOfHouse = Rectangle(Point(x1, y1), Point(x2, y2))
draw(BaseOfHouse)
BaseOfHouse.setOutline('brown')
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Suggestive Instructions Recquiring Action from User
T = Text(Point(30,65), "Click a coordinate above the mid-section of the rectangle")
T.setSize(15)
draw(T)
T.setFill('Red')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# After-User-Action Output
UserClick3 = win.getMouse()
undraw(T)
x3 = UserClick3.getX()
y3 = UserClick3.getY()


GuideLine3 = Line(Point(x1, (y2 + 13)), Point(x2, (y2+13)))
GuideLine3.setFill('blue')
GuideText3 = Text(Point(x1 + 10,y2 + 5), "Why not have a nice house?")
GuideText3.setSize(15)
GuideText3.setFill('Red')

Again3 = Text(Point(x1 + 10, y2 + 10), "Click anywhere here...")
AgainLine3 = Line(Point((x2 - x1), y2), Point((x2 - x1), 70))
AgainLine3.setFill('Red')
Again3.setSize(15)


DarkMatter = Rectangle(Point(70,y2), Point(0,0))
DarkMatter.setFill('Black')
DarkMatter2 = Rectangle(Point(x2, y2), Point(70, 70))
DarkMatter2.setFill('Black')
DarkMatter3 = Rectangle(Point(x1, y2), Point(0, 70))
DarkMatter3.setFill('Black')
while (x3 >= x2) or (y3 <= y2):
    draw(DarkMatter)
    draw(DarkMatter2)
    draw(DarkMatter3)
    draw(GuideLine3)
    draw(GuideText3)
    draw(Again3)
    draw(AgainLine3)
    UserClick3 = win.getMouse()
    x3 = UserClick3.getX()
    y3 = UserClick3.getY()
    undraw(GuideText3)
    undraw(GuideLine3)
    undraw(Again3)
    undraw(AgainLine3)
    undraw(DarkMatter)
    undraw(DarkMatter2)
    undraw(DarkMatter3)

RoofLine1 = Line(Point(x3, y3), Point(x1, y2))
RoofLine2 = Line(Point(x3, y3), Point(x2, y2))

draw(RoofLine1)
draw(RoofLine2)

for i in range(5):
    win.setBackground('gray')
    win.setBackground('black')
Door = Rectangle(Point((x1 + 2), (y1 + 2)), Point((x1 + 6), (y1 + 18)))
draw(Door)
DoorOutline = Rectangle(Point((x1 + 2.1), (y1 + 2.1)), Point((x1 + 6), (y1 + 18)))
draw(DoorOutline)
DoorOutline.setOutline('red')
win.setBackground('white')

DoorKnob = Circle(Point((x1 + 4), (y1 + 12.5)), 1.10)
draw(DoorKnob)
T = Text(Point((x1 + 4.2111112), (y1 + 12.5114)), "Welcome")
T.setSize(5)
draw(T)


for i in range(1000):
    BaseOfHouseShade = Rectangle(Point((x1 - 0.2), y1), Point(x2 + 0.2, y2))
    draw(BaseOfHouseShade)
    BaseOfHouseShade.setOutline('blue')
    RoofLineShade1 = Line(Point((x3 - 0.1), (y3 - 0.2)), Point((x1 - 0.2), y2))
    RoofLineShade2 = Line(Point((x3 + 0.1), (y3 + 0.2)), Point((x2 + 0.2), y2))
    draw(RoofLineShade1)
    RoofLineShade1.setFill('Cyan')
    draw(RoofLineShade2)
    RoofLineShade2.setFill('red')

    undraw(BaseOfHouseShade)
    undraw(RoofLineShade1)
    undraw(RoofLineShade2)


