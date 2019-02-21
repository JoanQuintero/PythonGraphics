

# An archery target consists of a central circle of yellow surrounded
# by concentric rings of red, blue, black and white. Each ring has the
# same “width,” which is the same as the radius of the yellow circle.
# Write a program that draws such a target.
# Hint: Objects drawn later will appear on top of objects drawn earlier.

from graphics import *

ArcheryTarget = GraphWin('Archery Target', 600, 600)
ArcheryTarget.setCoords(0,0, 200, 200)


# FOREVER NAME
T = Text(Point(170,197), "Joan Quintero-HW2-#1")
T.setSize(15)
T.draw(ArcheryTarget)
T.setFill('Silver')
T = Text(Point(170,192), "   Archery Target")
T.setSize(15)
T.draw(ArcheryTarget)
T.setFill('Silver')

Radius = 50

CenterOfGraph = Point(100, 100)
CenterText = Point(100, 100 + Radius + 10)
NameInput = Text(CenterText, "TARGET ACQUIRED!")
NameInput.draw(ArcheryTarget)

MainCircle = Circle(CenterOfGraph, Radius)
MainCircle.draw(ArcheryTarget)
MainCircle.setFill('White')

BlackRing = Circle(CenterOfGraph, Radius - 10)
BlackRing.draw(ArcheryTarget)
BlackRing.setFill('Black')

BlueRing = Circle(CenterOfGraph, Radius - 20)
BlueRing.draw(ArcheryTarget)
BlueRing.setFill('Blue')

RedRing = Circle(CenterOfGraph, Radius - 30)
RedRing.draw(ArcheryTarget)
RedRing.setFill('Red')

YellowRing = Circle(CenterOfGraph, Radius - 40)
YellowRing.draw(ArcheryTarget)
YellowRing.setFill('Yellow')

