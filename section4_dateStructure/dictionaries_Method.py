>>> d = {'x': 10, 'y': 20}
>>> d
{'x': 10, 'y': 20}
>>> d.keys()
dict_keys(['x', 'y'])
>>> d.values()
dict_values([10, 20])
>>> d2 = {'x': 1000, 'j': 500}
>>> d
{'x': 10, 'y': 20}
>>> d2
{'x': 1000, 'j': 500}
>>> d.update(d2)
>>> d
{'x': 1000, 'y': 20, 'j': 500}
>>> d['x']
1000
>>> d.get('x')
1000
>>> d['z']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'z'
>>> d.get('z')
>>> r = d.get('z')
>>> r
>>> type(r)
<class 'NoneType'>
>>> d
{'x': 1000, 'y': 20, 'j': 500}
>>> d.get('x')
1000
>>> d
{'x': 1000, 'y': 20, 'j': 500}
>>> d.pop('x')
1000
>>> d
{'y': 20, 'j': 500}
>>> del d['y']
>>> d
{'j': 500}
>>> del d
>>> d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'd' is not defined
>>> d = {'a':100, 'b':200}
>>> d.clear()
>>> d
{}
>>> d = {'a':100, 'b':200}
>>> d
{'a': 100, 'b': 200}
>>> 'a' in d
True
>>> 'j' in d
False
>>>
