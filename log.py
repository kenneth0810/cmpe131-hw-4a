import time
def timestamp(function):
    def wrapper():
        print(time.ctime())
        function()
    return wrapper