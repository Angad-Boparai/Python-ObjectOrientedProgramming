from turtle import Turtle

#Turtle 1
turtle1=Turtle()
turtle1.color('red')
turtle1.shape('turtle')

turtle1.penup()
turtle1.goto(-160,10)
turtle1.pendown()


#Turtle 2
turtle2=Turtle()
turtle2.shape('turtle')
turtle2.color('blue')

turtle2.penup()
turtle2.goto(-160,30)
turtle2.pendown()


#Turtle 3
turtle3=Turtle()
turtle3.color('green')
turtle3.shape('turtle')

turtle3.penup()
turtle3.goto(-160,50)
turtle3.pendown()


#Turtle 4
turtle4=Turtle()
turtle4.color('purple')
turtle4.shape('turtle')

turtle4.penup()
turtle4.goto(-160,70)
turtle4.pendown()


from random import randint

for movement in range(100):
	turtle3.forward(randint(1,5))
	turtle2.forward(randint(1,5))
	turtle1.forward(randint(1,5))
	turtle4.forward(randint(1,5))