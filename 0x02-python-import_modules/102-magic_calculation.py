def magic_calculation(a, b):
    add, sub = __import__('magic_calculation_102', globals(), locals(), ('add', 'sub'), 0)
    c = add(a, b)
    for i in range(4, 7):
        c = add(c, i)
    return c if a < b else sub(a, b)
