print "How old are you?"
age = raw_input()
print "How tall are you?"
height = raw_input()
#height = height * 100
#For this adjust on top we need convert the input to float number
print "How much do you weight?"
weight = raw_input()

print "So, you're %r years old, %r cm tall and %r kg heavy." % (
    age, height, weight)
