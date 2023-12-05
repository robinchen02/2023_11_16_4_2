import pyinputplus as pyip
import random
count=0
min=1
max=100
random_number=random.randint(min,max)
print("===========猜數字遊戲=============")
while(True):
    key_in=pyip.inputInt(f"猜數字範圍{min}~{max}")
    count+=1
    print(key_in)
    if key_in==random_number:
        print(f"Bingo!猜對了,答案是{random_number}")
        print(f"您猜了{count}次")
        break
    elif key_in > random_number:
        max=key_in-1
        print(f"猜錯了，再小一點")
        print(f"您猜了{count}次")
    elif key_in < random_number:
        min=key_in+1
        print(f"猜錯了，再大一點")
        print(f"您猜了{count}次")
    print("=================================")
print("遊戲結束")