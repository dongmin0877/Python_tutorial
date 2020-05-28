# say_something()
def say_something():
    # print('hi')
    s = 'hi'
    return s

result = say_something()
print(result)

# say_something()
# print(type(say_something()))

# f = say_something
# f()

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

    print(color)

result = what_is_this('green')
result = what_is_this('red')
result = what_is_this('yellow')
print(result)

