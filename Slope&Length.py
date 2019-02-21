
#
#
#           Line Segment Information.
#   This program allows the user to draw a line segment
#   and then displays some graphical and textual information
#   about the line segment.
#                            SUCH AS SLOPE AND LENGTH


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

from graphics import *
from math import *

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# GRAPH WINDOW SETTINGS
win = GraphWin("Slope & Length", 700, 500)
win.setCoords(0, 0, 70, 70)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# FOREVER NAME
T = Text(Point(60,67), "Joan Quintero-HW2-#3")
T.setSize(15)
T.draw(win)
T.setFill('Silver')
T = Text(Point(60,65), "   Slope+Length")
T.setSize(15)
T.draw(win)
T.setFill('Silver')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#MEANWHILE INSTRUCTIONS
T = Text(Point(35,50), "Program Will Print (Slope + Length) of 2 User-Clicks")
T.draw(win)
T.setFill('Blue')

# COMMENT: In these next parts you are repeating the same thing over and over,
#  so make it into a for-loop.

T.setSize(30)
T.setSize(30)
T.setSize(30)
T.setSize(30)
T.setSize(30)
T.setSize(30)
T.setSize(30)
T.setSize(30)
T.setSize(30)
T.setSize(30)
T.setSize(30)
T.setSize(30)
T.setSize(30)
T.setSize(30)
T.setSize(30)
T.setSize(30)
T.setSize(30)
T.setSize(30)
T.setSize(30)
T.setSize(30)

T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)
T.setSize(29)

T.setSize(28)
T.setSize(28)
T.setSize(28)
T.setSize(28)
T.setSize(28)
T.setSize(28)
T.setSize(28)
T.setSize(28)
T.setSize(28)
T.setSize(28)
T.setSize(28)
T.setSize(28)
T.setSize(28)
T.setSize(28)
T.setSize(28)
T.setSize(28)
T.setSize(28)
T.setSize(28)
T.setSize(28)
T.setSize(28)

T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)
T.setSize(27)

T.setSize(26)
T.setSize(26)
T.setSize(26)
T.setSize(26)
T.setSize(26)
T.setSize(26)
T.setSize(26)
T.setSize(26)
T.setSize(26)
T.setSize(26)
T.setSize(26)
T.setSize(26)
T.setSize(26)
T.setSize(26)
T.setSize(26)
T.setSize(26)
T.setSize(26)
T.setSize(26)
T.setSize(26)
T.setSize(26)

T.setSize(25)
T.setSize(25)
T.setSize(25)
T.setSize(25)
T.setSize(25)
T.setSize(25)
T.setSize(25)
T.setSize(25)
T.setSize(25)
T.setSize(25)
T.setSize(25)
T.setSize(25)
T.setSize(25)
T.setSize(25)
T.setSize(25)
T.setSize(25)
T.setSize(25)
T.setSize(25)
T.setSize(25)
T.setSize(25)

T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)
T.setSize(24)

T.setSize(23)
T.setSize(23)
T.setSize(23)
T.setSize(23)
T.setSize(23)
T.setSize(23)
T.setSize(23)
T.setSize(23)
T.setSize(23)
T.setSize(23)
T.setSize(23)
T.setSize(23)
T.setSize(23)
T.setSize(23)
T.setSize(23)
T.setSize(23)
T.setSize(23)
T.setSize(23)
T.setSize(23)
T.setSize(23)

T.setSize(22)
T.setSize(22)
T.setSize(22)
T.setSize(22)
T.setSize(22)
T.setSize(22)
T.setSize(22)
T.setSize(22)
T.setSize(22)
T.setSize(22)
T.setSize(22)
T.setSize(22)
T.setSize(22)
T.setSize(22)
T.setSize(22)
T.setSize(22)
T.setSize(22)
T.setSize(22)
T.setSize(22)
T.setSize(22)

T.setSize(21)
T.setSize(21)
T.setSize(21)
T.setSize(21)
T.setSize(21)
T.setSize(21)
T.setSize(21)
T.setSize(21)
T.setSize(21)
T.setSize(21)
T.setSize(21)
T.setSize(21)
T.setSize(21)
T.setSize(21)
T.setSize(21)
T.setSize(21)
T.setSize(21)
T.setSize(21)
T.setSize(21)
T.setSize(21)

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

# LINE SET TO BE CREATED ONCE USER ACTION IS COMPLETED
LineBtwnClicks = Line(FirstClick, SecondClick)
LineBtwnClicks.draw(win)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# FORMULAS
dx = x2 - x1
dy = y2 - y1
slope =  dy/dx
length = sqrt(dx**2 + dy**2)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Slope + Length on Graph Window

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
T1 = Text(Point(15,10), "Your Slope is")
T1.setSize(20)
T1.draw(win)
T1.setFill('Red')

T2 = Text(Point(35,10), str(slope) + ' ')
T2.setSize(20)
T2.draw(win)
T2.setFill('blue')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
T1 = Text(Point(15,5), "The length between your points is")
T1.setSize(20)
T1.draw(win)
T1.setFill('Red')

T2 = Text(Point(45,5), str(length) + ' ')
T2.setSize(20)
T2.draw(win)
T2.setFill('blue')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
