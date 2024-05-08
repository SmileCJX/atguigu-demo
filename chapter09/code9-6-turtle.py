import time
import turtle
from my_package import my_tools
pen = turtle.Turtle()
pen.backward(100)
pen.speed(0)

times = my_tools.get_time()
while True:
    time.sleep(1)
    times = my_tools.get_time()
    pen.clear()
    pen.write(times, font=("Arial", 40, "normal"))

# pen.write('hello', font=("Arial", 40, "normal"))

# for i in range(100):
#     pen.forward(100 + i)
#     pen.right(89)

# pen.forward(100)
# pen.left(50)
# pen.forward(100)
input()