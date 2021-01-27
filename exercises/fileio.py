import os
import shutil
from datetime import datetime

# opening file (creating one) w+ mode to write
f = open('practice.txt', 'w+')
f.write('This is a text string')
f.close()

os.getcwd()

print(os.listdir('/Users/rubentrevino/python-exercises/exercises'))

# file target, destination
# shutil.move('practice.txt', '/Users/rubentrevino/desktop')

mytime = datetime.time(2, 30, 20)

print(mytime)

today = datetime.date.today()

print(today.ctime())