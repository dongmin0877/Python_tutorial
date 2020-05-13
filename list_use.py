>>> seat = []
>>> min = 0
>>> max = 5
>>> min <= len(seat) < max
True
>>> seat.append('p')
>>> min <= len(seat) < max
True
>>> len(seat)
1
>>> seat.append('p')
>>> min <= len(seat) < max
True
>>> len(seat)
2
>>> seat.append('p')
>>> seat.append('p')
>>> min <= len(seat) < max
True
>>> len(seat)
4
>>> seat.append('p')
>>> min <= len(seat) < max
False
>>> len(seat)
5
>>> seat.pop(0)
'p'
>>> min <= len(seat) < max
True
