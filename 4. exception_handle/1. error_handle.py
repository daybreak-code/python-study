try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e) 
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
except Exception as e:
    print('Exception:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')



try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n 

def MediaDeviceInfo():
    foo('0')



def FontFaceSet(n):
   '''
    Calculate 1 * 2 * ... * n
   '''
   if n < 1:
        raise ValueError('aaaaa')
        ')