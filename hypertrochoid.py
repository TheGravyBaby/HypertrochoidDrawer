from graphics import * 
from math import * 

#https://www.programiz.com/python-programming/examples/lcm
def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

def drawHypotrochoid(R, r, d, scale):

   win = GraphWin("Hypotrochoid", 500, 500)               # opens a graphical window 
   win.setBackground("White")

   theta = 0
   dTheta = .01745    
   currentPoint = Point(0,0)              
   lastPoint = Point(0,0)
   start = False
   maxTheta = 2 * 3.14159 * compute_lcm(r, R) / R

   while theta < maxTheta:                   
      x = (R - r) * cos(theta) + d * cos( (R - r) / r * theta ) 
      y = (R - r) * sin(theta) - d * sin( (R - r) / r * theta )
      
      x = scale * x + 250
      y = scale * y + 250

      lastPoint = currentPoint
      currentPoint = Point(x,y)

      if start:
         l1 = Line(currentPoint, lastPoint)
         l1.draw(win)
         
      theta += dTheta
      start = True                                         # add a little bit to the theta we test for the next loop

   win.getMouse()                                          # Pause to view result
   win.close()

drawHypotrochoid(5, 9, 4, 10)