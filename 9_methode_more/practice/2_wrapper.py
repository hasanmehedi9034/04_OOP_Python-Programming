def do_something():
    # print("Inside the do_something")

    def inner_function():
        # print('Inside the')
        return 1
    
    return inner_function

x = do_something()()

print(x)