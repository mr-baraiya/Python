def myfunc():
    print("Hello World!")

myfunc()
print(__name__) # It is __main__ File if Run by It Self


if __name__ == "__main__":
    print("We Are directly Call The MyFunc()")