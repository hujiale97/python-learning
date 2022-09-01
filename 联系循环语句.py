# conding:utf-8
count = 0
flage = True
str_num = input("请输入要比较的数字:")
print("进入循环")
while flage:
  while count < 5:
    if "3" > str_num:
       print("在执行循环")
       count = count + 1
       print(count)
    else:
      print("要终止循环")
      flage = False
      break
  else:
      print(count)
      break
print("退出循环")
