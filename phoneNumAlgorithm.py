phone = {'0': 'O', '1': 'I', '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO', '7': 'PQRS', '8': 'TUV',
         '9': 'WXYZ'}


def foo(number):
    if len(number) == 1:
        return [c for c in phone[number]]
    else:
        a = foo(number[0])
        sols = []
        for i in a:
            r = foo(number([1:]))
            sols.extend([i + rr for rr in r])
            return sols


a = sorted(foo('8182612'))
print(a)
print(len(a))
