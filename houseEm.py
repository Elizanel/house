from graphics import *

newWin = GraphWin('house', 400, 400)
newWin.setBackground("LightPink")
center=Point(200,200)
rect = Rectangle(Point(25,90), Point(170,200))
rect.draw(newWin)
#Add my name
name=Text(Point(100,5),
"Elizanel Martinez Moquete")
name.draw(newWin)
name.setSize(12)
#make a sun 
center = Point(180,20)
yellowCircle = Circle(center,20)
yellowCircle.setFill('yellow')
yellowCircle.draw(newWin)
#Body for the house 
rect.setFill('light slate gray')
rectb=Rectangle(Point(30,180), Point(160,190))
rectb.draw(newWin)
rectb.setFill('SlateBlue')
rectbb=Rectangle(Point(65,110), Point(125,200))
rectbb.draw(newWin)
rectbb.setFill('brown')
rectc=Rectangle(Point(30,30), Point(160,40))
rectc.draw(newWin)
rectc.setFill('SlateBlue')
center = Point(95,100)
yellowCircle = Circle(center,30)
yellowCircle.setFill('MistyRose')
yellowCircle.draw(newWin)
#roof for the house
roof=Polygon(Point(15,100), Point(179,100), Point(100,9))
roof.setFill('navy')
roof.setOutline("black")
roof.draw(newWin)
#add textbox(input1)
Text(Point(100,290), " Enter your name:").draw(newWin) 
message1=Text(Point(120,310), "(then click anywhere to continue)")
message1.setSize(8)
message1.draw(newWin)
input1=Entry(Point(240,290), 9)
input1.draw(newWin)
#add another textbox(output1) to display a message
output1 = Text(Point(100,350)," ")
#get the text entered and print a greeting
newWin.getMouse()
name = input1.getText()
greeting = ("Hello " + name + "!!"
)
output1.setText(greeting)
output1.draw(newWin)

#Quit after click
exitmessage= Text(Point(newWin.getWidth()/2,20),"Click anywhere to exit.")
exitmessage.setStyle("italic")
exitmessage.draw(newWin)
newWin.getMouse()
newWin.close()

















