import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('haha')
        return func(*args, **kw)
    return wrapper

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('heiehie')
            return func(*args, **kw)
        return wrapper
    return decorator


# 不带参数装饰器
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('calss %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 带参数装饰器
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s()" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log2('你好')
def add(x, y):
    return x + y
# 先调用log2('你好')返回decorator函数，再调用decorator(func)函数返回wrapper函数
# log('nihao')(func)(1,2)
sum = add(1, 2)