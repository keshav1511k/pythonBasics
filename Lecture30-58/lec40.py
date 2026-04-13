# variable scope = where a variable is visible and accessible 
# scope resolution = (LEGB) Local -> enclosed -> global -> built in 

# Local scope example

def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

func1()
func2()


# enclosed example

def func1():
    x = 1

    def func2():
        print(x)
    func2()

func1()


# Global example

def func1():
    print(x)

def func2():
    print(x)

x = 2
func1()
func2()


# built-in example

import math

def func1():
    print(math.e)

func1()