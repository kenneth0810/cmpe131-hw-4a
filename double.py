def double(function):
    def wrapper():
        function()
        print("Let's try that again!")
        function()
    return wrapper

@double
def test():
    print("hi")