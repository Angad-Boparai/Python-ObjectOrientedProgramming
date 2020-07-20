from shapes import Rectangle,Triangle,Paper,Oval

paper=Paper()

rect=Rectangle()
rect.set_width(200)
rect.set_height(50)
rect.set_color('red')

rect.set_x(10)
rect.set_y(10)
rect.draw()


rect1=Rectangle()
rect1.set_width(200)
rect1.set_height(50)
rect1.set_color('purple')

rect1.set_x(80)
rect1.set_y(80)
rect1.draw()

paper.display()