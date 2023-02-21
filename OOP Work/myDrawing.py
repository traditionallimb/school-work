from shapes import Paper, Triangle, Rectangle, Oval
paper = Paper()

House = Rectangle(200, 200, 200, 200, "blue")
House.draw()

door = Rectangle(40, 100, 280, 300, "brown")
door.draw()

window1 = Rectangle(50,50, 215, 225, "white")
window1.draw()

window2 = Rectangle(50,50, 325, 225, "white")
window2.draw()

window3 = Rectangle(50,50, 215, 325, "white")
window3.draw()

window4 = Rectangle(50,50, 325, 325, "white")
window4.draw()

roof = Triangle(200, 200, 400, 200, 300, 150, "yellow")
roof.draw()

knob = Oval(20,20, 285, 330, "yellow")
knob.draw()

paper.display()