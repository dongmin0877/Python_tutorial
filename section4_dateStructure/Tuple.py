# >>> t = (1, 2,3,4,1,2)
# >>> t
# (1, 2, 3, 4, 1, 2)
# >>> type(t)
# <class 'tuple'>
# >>> t[0]=100
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# >>> t[0]
# 1
# >>> t[-2]
# 1
# >>> t[2:5]
# (3, 4, 1)
# >>> t
# (1, 2, 3, 4, 1, 2)
# >>> t.index(1)
# 0
# >>> t.index(1,1)
# 4
# >>> t.count(1)
# 2
# >>> t = ('データの上書きせずに読み取り専用に使う場合、')
# >>> t
# 'データの上書きせずに読み取り専用に使う場合、'
