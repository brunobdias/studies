name = 'Zed A. Shaw'
age = 35
height_inc = 74 # inches
weight_lbs = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_cm = 74.0 * 2.54
weight_kg = 180.0 / 2.20462262

print ""

print "Let's talk about %s." % name
print "He's %d inches tall." % height_inc
print "He's %d pounds heavy." % weight_lbs
print "He's %d centimeters tall." % height_cm
print "He's %d kilograms heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s dependin on the coffee." % teeth

# Conversion table
# lbs to Kg
    # Divide the number of pounds by 2.20462262 to convert it to kilograms.
# inches to Cm
    # Multiple Inches by 2.54 to get the number of centimeters or
    # Divide the number of centimeters by 2.54 to get the number of inches.

# this is a trick line

print ""

print "If I add %d, %dinc, and %dlbs I get %d." % (
    age, height_inc, weight_lbs, age + height_inc + weight_lbs
)

print ""

print "If I add %d, %dcm, and %dkg I get %d." % (
    age, height_cm, weight_kg, age + height_cm + weight_kg
)

print ""
