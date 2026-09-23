def outerFun(greet):

    def innerFun(name):

        print(greet + " " + name)

    return innerFun


# simple curry
outerFun("Welcome")("Virat")
engfun = outerFun("Welcome")

namefun = outerFun("Vanakam")
namefun("Srikanth")
namefun("Sundar")
engfun("Rohit")