def fn(self,name = 'World'):
    print("Hello,%s." % name)
Hello = type('Hello',(object,),dict(hello = fn))
h = Hello()
h.hello()
print(type(Hello))
print(type(h))
print(type(fn))