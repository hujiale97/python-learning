name = input('请输入姓名:')
age = input('请输入年龄:')
job = input('请输入职业:')
hobby = input('请输入爱好:')
msg = '''
------------ info of Alex Li ----------
Name  : %s
Age   : %s 
job   : %s 
Hobbie: %s 
------------- end ----------------

'''
print(msg%(name,age,job,hobby))