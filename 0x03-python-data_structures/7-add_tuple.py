#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 and len(tuple_b) < 2:
        print(tuple_a, tuple_b, len(tuple_a), len(tuple_b))
        return (0, 0)
    return (
        (
            (tuple_a[0] if len(tuple_a) >= 1 else 0) +
            (tuple_b[0] if len(tuple_b) >= 1 else 0)),
        ((tuple_a[1] if len(tuple_a) >= 2 else 0) +
         (tuple_b[1] if len(tuple_b) >= 2 else 0))
    )
