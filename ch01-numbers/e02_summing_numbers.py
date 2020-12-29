from typing import List, Union, Tuple


def bespoke_sum(*args: Union[List, Tuple, int, float]) -> Union[int, float]:
    tot = 0
    for arg in args:
        if isinstance(arg, List) or isinstance(arg, Tuple):
            for _ in arg:
                tot += _
        elif type(arg) in (float, int):
            tot += arg
        else:
            print('ignoring this arg...')
            pass
    return tot


print(bespoke_sum((1, 2, 3, 4, 5), 10, 20, 't'))
