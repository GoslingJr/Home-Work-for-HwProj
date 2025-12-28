def curry(func, arity):
    if not callable(func):
        raise TypeError("First argument must be callable")
    
    if not isinstance(arity, int):
        raise TypeError("Arity must be an integer")
    
    if arity < 0:
        raise ValueError("Arity cannot be negative")
    
    def curried(*args):
        if len(args) > arity:
            raise TypeError(f"Function takes exactly {arity} arguments ({len(args)} given)")
        
        if len(args) == arity:
            return func(*args)
        
        def inner(*next_args):
            total_args = args + next_args
            if len(total_args) > arity:
                raise TypeError(f"Function takes exactly {arity} arguments ({len(total_args)} given)")
            
            if len(total_args) == arity:
                return func(*total_args)
            
            return curried(*total_args)
        
        return inner
    
    return curried


def uncurry(curried_func, arity):
    if not callable(curried_func):
        raise TypeError("First argument must be callable")
    
    if not isinstance(arity, int):
        raise TypeError("Arity must be an integer")
    
    if arity < 0:
        raise ValueError("Arity cannot be negative")
    
    def uncurried(*args):
        if len(args) != arity:
            raise TypeError(f"Function takes exactly {arity} arguments ({len(args)} given)")
        
        result = curried_func
        for i, arg in enumerate(args):
            if not callable(result):
                raise TypeError(f"Cannot apply argument {i+1}, function already fully applied")
            result = result(arg)
        
        return result
    
    return uncurried


def sum3(x, y, z):
    return x + y + z


def test_curry_uncurry():
    print("Testing curry/uncurry:")
    
    sum3_curry = curry(sum3, 3)
    sum3_uncurry = uncurry(sum3_curry, 3)
    
    print(f"sum3_curry(1)(2)(3) = {sum3_curry(1)(2)(3)}")      # 6
    print(f"sum3_uncurry(1, 2, 3) = {sum3_uncurry(1, 2, 3)}")  # 6
    
    test1 = sum3_curry(1)
    test2 = test1(2)
    print(f"sum3_curry(1)(2)(3) step by step = {test2(3)}")   # 6
    
    def multiply4(a, b, c, d):
        return a * b * c * d
    
    multiply4_curry = curry(multiply4, 4)
    print(f"multiply4_curry(2)(3)(4)(5) = {multiply4_curry(2)(3)(4)(5)}")  # 120
    
    multiply4_uncurry = uncurry(multiply4_curry, 4)
    print(f"multiply4_uncurry(2, 3, 4, 5) = {multiply4_uncurry(2, 3, 4, 5)}")  # 120
    
    def add2(x, y):
        return x + y
    
    add2_curry = curry(add2, 2)
    print(f"add2_curry(10)(20) = {add2_curry(10)(20)}")  # 30
    
    add2_uncurry = uncurry(add2_curry, 2)
    print(f"add2_uncurry(10, 20) = {add2_uncurry(10, 20)}")  # 30
    
    try:
        sum3_curry(1)(2)(3)(4)
    except TypeError as e:
        print(f"Correctly caught error: {e}")
    
    try:
        sum3_uncurry(1, 2)
    except TypeError as e:
        print(f"Correctly caught error: {e}")
    
    try:
        curry(sum3, -1)
    except ValueError as e:
        print(f"Correctly caught error: {e}")


if __name__ == "__main__":
    test_curry_uncurry()
