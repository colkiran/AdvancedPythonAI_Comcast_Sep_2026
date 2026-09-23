
def outerFun(info):
    inf = "Mr." + info

    def innerFun():
        print(inf)
        print(info)
    innerFun()

outerFun("Virat")
