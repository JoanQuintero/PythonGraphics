

#                 Rectangle Information.

# This program displays information about a rectangle drawn by the user.
# Input: 2 mouse clicks for the opposite corners of a rectangle.
# Output: Draw the rectangle.
#Print the perimeter and area of the rectangle.
# Formulas:
#area = (length)(width) perimeter = 2(length + width)





#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

from graphics import *
from math import *

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# GRAPH WINDOW SETTINGS
win = GraphWin("Perimeter+Area - 2~UserClick~Rectangle", 700, 500)
win.setCoords(0, 0, 70, 70)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#RECTANGULAR FRAME (OUTSIDE)
TestPoint = Point(0, 70)
TestPoint1 = Point(70, 70)
TestLine = Line(TestPoint, TestPoint1)
TestLine.draw(win)
TestPoint = Point(0, 0)
TestPoint1 = Point(0, 70)
TestLine = Line(TestPoint, TestPoint1)
TestLine.draw(win)
TestPoint = Point(0, 0)
TestPoint1 = Point(70, 0)
TestLine = Line(TestPoint, TestPoint1)
TestLine.draw(win)
TestPoint2 = Point(70, 0)
TestPoint22 = Point(70, 70)
TestLine2 = Line(TestPoint2, TestPoint22)
TestLine2.draw(win)
#RECTANGULAR FRAME (INSIDE)
TestPoint = Point(1, 69)
TestPoint1 = Point(69, 69)
TestLine = Line(TestPoint, TestPoint1)
TestLine.draw(win)
TestPoint = Point(1, 1)
TestPoint1 = Point(1, 69)
TestLine = Line(TestPoint, TestPoint1)
TestLine.draw(win)
TestPoint = Point(1, 1)
TestPoint1 = Point(69, 1)
TestLine = Line(TestPoint, TestPoint1)
TestLine.draw(win)
TestPoint2 = Point(69, 1)
TestPoint22 = Point(69, 69)
TestLine2 = Line(TestPoint2, TestPoint22)
TestLine2.draw(win)

# FOREVER NAME
T = Text(Point(60,67), "Joan Quintero-HW2-#4")
T.setSize(6)
T.draw(win)
T.setSize(15)
T.setFill('Silver')
T = Text(Point(60,65), "   Area+Perimeter")
T.setSize(6)
T.draw(win)
T.setSize(15)
T.setFill('Silver')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#MEANWHILE INSTRUCTIONS
T = Text(Point(35,50), "Program Will Print Perimeter and Area of 2 User-Clicks Rectangle")
T.draw(win)
T.setFill('Blue')


T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)
T.setSize(20)

T.setSize(19)
T.setSize(19)
T.setSize(19)
T.setSize(19)
T.setSize(19)

T.setSize(18)
T.setSize(18)
T.setSize(18)
T.setSize(18)
T.setSize(18)

T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)
T.setSize(17)

T.setSize(16)
T.setSize(16)
T.setSize(16)
T.setSize(16)
T.setSize(16)

T.setSize(15)
T.setSize(15)
T.setSize(15)
T.setSize(15)
T.setSize(15)

T.setSize(14)
T.setSize(14)
T.setSize(14)
T.setSize(14)
T.setSize(14)
T.setSize(14)
T.setSize(14)
T.setSize(14)
T.setSize(14)
T.setSize(14)
T.setSize(14)
T.setSize(14)
T.setSize(14)
T.setSize(14)
T.setSize(14)
T.setSize(14)
T.setSize(14)
T.setSize(14)
T.setSize(14)
T.setSize(14)

T.setSize(13)
T.setSize(13)
T.setSize(13)
T.setSize(13)
T.setSize(13)

T.setSize(12)
T.setSize(12)
T.setSize(12)
T.setSize(12)
T.setSize(12)

T.setSize(11)
T.setSize(11)
T.setSize(11)
T.setSize(11)
T.setSize(11)

T.setSize(10)
T.setSize(10)
T.setSize(10)
T.setSize(10)
T.setSize(10)


T.undraw()


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#




# Suggestive Instructions Recquiring Action from User
T = Text(Point(15,67), "Click Anywhere For First Point")
T.setSize(20)
T.draw(win)
T.setFill('Red')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# After-User-Action Output
UserClick1 = win.getMouse()
T.undraw()
x1 = UserClick1.getX()
y1 = UserClick1.getY()
FirstClick = Point(x1,y1)
FirstClick.draw(win)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Suggestive Instructions Recquiring Action from User
T = Text(Point(20,67), "Click Anywhere else again for Second Point")
T.setSize(20)
T.draw(win)
T.setFill('Red')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# After-User-Action Output
UserClick2 = win.getMouse()
T.undraw()
x2 = UserClick2.getX()
y2 = UserClick2.getY()
SecondClick = Point(x2,y2)
SecondClick.draw(win)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#FirstClick = Point(x1,y1)
#SecondClick = Point(x2,y2)

# LINE SET TO BE CREATED ONCE USER ACTION IS COMPLETED

Point3 = Point(x1, y2)
Point3.draw(win)
Point4 = Point(x2, y1)
Point4.draw(win)

Line1BtwnClicks = Line(FirstClick, Point(x2, y1))
Line1BtwnClicks.draw(win)

Line2BtwnClicks = Line(FirstClick, Point3)
Line2BtwnClicks.draw(win)

Line3BtwnClicks = Line(Point(x1, y2), SecondClick)
Line3BtwnClicks.draw(win)

Line4BtwnClicks = Line(Point4, SecondClick)
Line4BtwnClicks.draw(win)




#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#



#FirstClick = Point(x1,y1)
#SecondClick = Point(x2,y2)
#Point3 = Point(x1, y2)
#Point4 = Point(x2, y1)


# FORMULAS
Dx1 = abs(x2 - x1)
Dy1 = abs(y2 - y1)
Length = (Dx1)
Width = (Dy1) 

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Length + Width on Graph Window

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




    
Line1BtwnClicks.setFill('Red')
T1 = Text(Point((x1 + 5),(y1 - 3)), "int(Length) ")
T1.setSize(15)
T1.draw(win)
T1.setFill('Red')

T2 = Text(Point((x1 + 5),(y1 - 5)), int(Length))
T2.setSize(12)
T2.draw(win)
T2.setFill('Black')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Line2BtwnClicks.setFill('Blue')
T1 = Text(Point((x1 - 3),(y2)), "int(Width) ")
T1.setSize(15)
T1.draw(win)
T1.setFill('Blue')

T2 = Text(Point((x1 - 3),(y2 - 2)), int(Width))
T2.setSize(12)
T2.draw(win)
T2.setFill('Black')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# FORMULAS
area = Length * Width
perimeter = 2*(Length + Width)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
T1 = Text(Point(5,10), "Area:")
T1.setSize(16)
T1.draw(win)
T1.setFill('Red')

T2 = Text(Point(5,7), int(area))
T2.setSize(14)
T2.draw(win)
T2.setFill('blue')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
T1 = Text(Point(6,5), "Perimeter:")
T1.setSize(16)
T1.draw(win)
T1.setFill('Red')

T2 = Text(Point(5,2), int(perimeter))
T2.setSize(14)
T2.draw(win)
T2.setFill('blue')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
