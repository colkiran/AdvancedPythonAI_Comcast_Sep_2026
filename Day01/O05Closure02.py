def outerFun(info): # HOF - Higher Order Function
    inf = "Mr." + info

    def innerFun():
        print(inf)

    return innerFun

outerFun("Rohit")
print("-" * 60)

print(outerFun.__name__)
print(outerFun("Rohit").__name__)
print("-" * 60)

outerFun("Rohit")()
print("-" * 60)

inref = outerFun("Rohit")
inref()
