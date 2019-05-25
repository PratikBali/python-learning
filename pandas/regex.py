import re

print('hi')

str = "Maharashtra chi language Marathi ahe ani mipan marathi ahe jay maharashtra"

x = re.findall('ma', str)
print('1',x)

x = re.findall('Ma', str)
print('2', x)

str = 'India is my country'
x = re.search('^India', str)
print('3', x)

str = 'Royal is always royal'
x = re.split('\s', str)
print('4', x)

str = 'Today is monday and udya is tuesday'
x = re.sub('udya', 'Tomorrow', str)
print('5', x)

