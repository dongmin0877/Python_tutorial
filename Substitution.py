# >>> 'a is {}' .format('a')
# 'a is a'
#
# >>> 'a is {}' .format('test')
# 'a is test'
#
# >>> 'a is {} {} {}' .format(1, 2, 3)
# 'a is 1 2 3'
#
# >>> 'a is {0} {1} {2}' .format(1, 2, 3)
# 'a is 1 2 3'
#
# >>> 'a is {2} {1} {0}' .format(1, 2, 3)
# 'a is 3 2 1'
#
# >>> 'My name is {0} {1}' .format('Jun', 'Sakai')
# 'My name is Jun Sakai'
#
# >>> 'My name is {0} {1}'.format('Dong', 'min')
# 'My name is Dong min'
#
# >>> 'My name is {0} {1}. Watashi ha {1} {0}'.for
# mat('Dong', 'Min')
# 'My name is Dong Min. Watashi ha Min Dong'
#
# >>> 'My name is {name} {family}. Watashi ha {fam
# ily} {name}'.format(name='Dong', family='Min')
#
# 'My name is Dong Min. Watashi ha Min Dong'
#
# >>> 1
# 1
#
# >>> '1'
# '1'
#
# >>> str(1)
# '1'
#
# >>> x = str(1)
#
# >>> type(x)
# <class 'str'>
#
# >>> str(3.14)
# '3.14'
#
# >>> str(True)
# 'True'
#
# # format >>>> f-strings 可能
#
# a = 'a'
# print(f'a is {a}')
#
# x, y, z = 1, 2, 3
# print(f'a is {x}, {y}, {z}')
# print(f'a is {z}, {y}, {x}')
#
# name = 'Dong'
# family = 'Min'
# print(f'My name is {name} {family}. I am {family} {name}')
