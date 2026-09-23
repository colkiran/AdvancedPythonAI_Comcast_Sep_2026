"""
install emojis
 pip install emojis
"""
def outerFun(greet):
    def innerFun(sep):
        def innermostFun(name):
            from emojis import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + name)
            print(emojized)
        return innermostFun
    return innerFun


engGrt = outerFun("Welcome")
tgrEmj = engGrt("tiger")
tgrEmj("Sheroff")

linEmj = engGrt("lion")
linEmj("Jack")

"""
outerFun("Welcome")("------>")("Sachin")

print("-" * 60)

engGrt = outerFun("Welcome")
tmlGrt = outerFun("Vanakam")

sngln = engGrt("----->")
dblln = engGrt("=====>")

sngln("Sachin")
dblln("Rahul")
"""