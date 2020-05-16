>>> a = { 1,2,3,4,4,4,5,6}
>>> a
{1, 2, 3, 4, 5, 6}
>>> type(a)
<class 'set'>
>>> b = {2,3,3,6,7}
>>> b
{2, 3, 6, 7}
>>> a
{1, 2, 3, 4, 5, 6}
>>> b
{2, 3, 6, 7}
>>> a- b
{1, 4, 5}
>>> b - a
{7}
>>> a & b
{2, 3, 6}
>>> a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> a | b
{1, 2, 3, 4, 5, 6, 7}
>>> a ^ b
{1, 4, 5, 7}
>>>
