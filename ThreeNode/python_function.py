#coding=utf-8
def people(age):
    #函数体
    if age>0:
        print("这个人是正常的")
        name = get_name()
        print(name)
    else:
        print("这个人是不正常的")
    
def get_name():
    return "张三"

people(10)