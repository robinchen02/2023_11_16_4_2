import random
import pyinputplus as pyip



with open("names.txt",mode="r",encoding="utf-8") as file:
    names:str = file.read()

nameslist:list[str] = names.split("\n")

student_nums:int = pyip.inputInt("請輸入學生的人數(1~50):",min=1,max=50)
scores_nums:int = pyip.inputInt("請輸入科目數(1~7)",min=1,max=7)

students:list[list] = []


names:list[str] = random.choices(nameslist,k=student_nums)
for name in names:
    stu:list[int|str] = []
    stu.append(name)
    for i in range(scores_nums):
        stu.append(random.randint(40,100))
    students.append(stu)

print(students)