import pyinputplus as pyip
import math
#1個參數，有傳出值
def circle_area(radius):
    area=radius**2*math.pi
    return area
radius=pyip.inputFloat("請輸入半徑:")
print(radius)
area=circle_area(10)
print(f"半徑{radius},園面積是{area}")