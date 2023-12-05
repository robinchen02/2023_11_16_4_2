import pyinputplus as pyip
import random
while(True):
    count=0
    min=1
    max=100
    random_number=random.randint(min,max)
    print(random_number)
    print("===========猜數字遊戲=============")
    while(True):
        key_in=pyip.inputInt(f"猜數字範圍{min}~{max}: ")
        count+=1
        print(key_in)
        if key_in==random_number:
            print(f"Bingo!猜對了,答案是:{random_number}")
            print(f"您猜了{count}次")
            break
        elif key_in > random_number:
            max=key_in-1
            print(f"猜錯了，再小一點")
            print(f"您猜了:{count}次")
        elif key_in < random_number:
            min=key_in+1
            print(f"猜錯了，再大一點")
            print(f"您猜了:{count}次")
        print("=================================")
    is_continue=pyip.inputYesNo("請問還要繼續嗎?(y/n)")
    if is_continue == "no":
        break
print("遊戲結束")