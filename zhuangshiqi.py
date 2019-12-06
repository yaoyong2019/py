def now():
    print('2019-9-28')
f = now
f()
print(f.__name__)
def log(func):
    def wrapper(*args,**kw):
        print('call %s()' % func.__name__)
        return fanc(*args,**kw)
    return wrapper
log(now)
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s()' %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print('2015-3-25')
now()