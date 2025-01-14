def print_params(a=1, b='калык', c=True):
    print(a,b,c)

values_list = [65.5, 'пире', False]

values_dict = {'a': 118, 'b': 'мутер','c': None}

values_list_2 = [25.25, 'рывыж']



print_params()

print_params(1)

print_params(b='мари')

print_params(c=[1,2,3])

print_params(1,25,[1,2,3])



print_params(values_list_2)

print_params(*values_list_2)


print_params(values_dict)

print_params(**values_dict)



print_params(*values_list_2, True)

