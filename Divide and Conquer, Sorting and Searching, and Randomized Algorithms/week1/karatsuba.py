# /**
#  * @author Kotoz
#  * @email mohamed.t.elshetry@mail.com
#  * @create date 2020-04-30 11:31:02
#  * @modify date 2020-04-30 11:31:02
#  * @desc [description]
#  */

def karatsuba(x ,y):
    lx = len(str(x))
    ly = len(str(y))
    a = x // 10**(lx//2)
    b = x % 10**(lx-(lx//2))
    c = y // 10**(ly//2)
    d = y % 10**(ly-(ly//2))

    ac = a*c
    bd = b*d
    cb = c*b
    ad = a*d

    if len(str(x)) == 1 or len(str(y)) == 1:
        return ac+cb+bd+ad
    karatsuba(cb, ad)
n = karatsuba(23, 56)
print(n)