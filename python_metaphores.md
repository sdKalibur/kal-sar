## Python core principles
python is protocol oriented language.

* Data model
* metaclasses
* decorators
* generators

# Data Model
* dunder methods:
    * __init__
    * __repr__
    * __add__
    * __len__


    class Polymomial:
        def __init__(self, *coeffs):
            self.coeffs = coeffs
        
        def __repr__(coeffs):
            return 
            
        def __add__(self, other):
            pass
    p1 = Polymonial()
    p1.coeeffs = 1,2,3
   
 # Metaclasses
 
 Classes that derive from type, have methods that  allow you to intercept the construction of derive types
 
 
    core infrastructure team: libray code
        enforce constraints on user code:
            * built class\
            * metaclasses - complexity is high, rarely used
            * __init_subclass__ - new simpler than above metaclasses
    vs 
    developers : user code
        assert baseattr(Base, 'foo') "You broke it."
 
    from dis import dis 
    dis : disassemble
        __build_class__
    dis(_)
      2           0 LOAD_CONST               0 (None)
                  2 RETURN_VALUE
 
     class BaseMeta(type):
        def __new__(cls, name, bases, body):
            if not 'bar' in body:
                raise TypeError("That method does not exist")
            return super().__new__(cls, name,bases,body)
    Use Assert to check if the mthod exists.
    
            
# Decorators
**wrapping** functions within functions

    Example:
    import time from time
        def timer()
            before = time()
            rv = fuction_to_time()
            after = time()
            print("duration : ", before - after)
            return rv
            
    To simplify tha above we would wrap the function like
    
    @timer
    def function_to_time():
        pass
        

    def add(x,y=10):
        return x + y
        
    add.__name__
    'add'
    add.__code__.co_code
    b'|\x00|\x01\x17\x00S\x00'
    add.__code__.co_cellvars
    ()
    add.__code__.co_varnames
    ('x', 'y')

    from inspect import getsource    
    from inspect import getfile
    getfile(add)
    '<input>'

# Generators

    def add1(x,y):
    return x + y
    
    class adder:
        def __call__(self, x ,y):
            return x + y
        
    add2 = adder(1,2)
 
    add2 = adder()
    add2(1,2)
    3
    
    Example:
    
    Def do_this():
        this_first()
        yeild
        This_second()
        yeild
        This_last()
        return