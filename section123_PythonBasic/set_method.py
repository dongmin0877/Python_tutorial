>>> s = {1,2,3,4,5}
>>> s
{1, 2, 3, 4, 5}
>>> s[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>> s.add(6)
>>> s
{1, 2, 3, 4, 5, 6}
>>> s.add(6)
>>> s
{1, 2, 3, 4, 5, 6}
>>> s.remove(6)
>>> s
{1, 2, 3, 4, 5}
>>> s.clear()
>>> s
set()
>>> a = {}
>>> type(a)
<class 'dict'>
>>> a
{}
>>>
