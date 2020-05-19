s = 'My name is dongmin. hi dong.'
print(s)
is_start = s.startswith('My')

print(is_start)
is_start = s.startswith('X')
print(is_start)

print("#############")
print(s.find('dong'))
print(s.rfind('dong'))
print(s.count('dong'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('dong', 'Mike'))
