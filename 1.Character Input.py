import datetime


name = input('Type your name:')


age = input('Type your age:')

now = datetime.datetime.now()


diff = 100 - int(age)


print('Hi '+name+" you will complete 100 years in ",(now.year+diff))
