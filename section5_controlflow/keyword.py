# def menu(entree='beef', drink='wine'):
#     print(entree, drink)

# def menu(**kwargs):
#     for k, v in kwargs.items():
#         print(k,v)

# d = {
#     'entree': 'beef',
#     'drink': 'ice coffee',
#     'dessert': 'ice'
# }
#
# menu(entree='beef', drink='coffee')

def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)
menu('banana', 'apple', 'orange', entree='beef', drink='coffee')

