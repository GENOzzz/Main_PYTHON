import turtle as t

t.shape("turtle")
'''
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

##반복문을 이용한 사각형 그리기
for i in range(1,5,1):
    t.forward(100)
    t.right(90)

i=0
while i<100:
    t.forward(i)
    t.right(i)
    i+=1
'''
angle = 83
t.bgcolor("black")
t.color("yellow")
t.speed(0)
for x in range(400):
    t.forward(x*2)
    t.left(angle)
