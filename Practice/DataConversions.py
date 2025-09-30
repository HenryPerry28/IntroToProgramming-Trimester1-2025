# Start by copying this code block into a new file called dataconversion.py in your unit 2 folder. This is an ungraded activity.

# Successfully convert all of the following variables to another type and print the result
# If the conversion prints without errors, you did the conversion correctly

a = 115         #int -> string
b = 3.14        #float -> string
c = "68"        #string -> int
d = "True"      #string -> boolean
e = True        #boolean -> string
f = False       #boolean -> string
g = '10110111'  #binary -> int
h = "2.54"      #string -> float
i = 100         #int -> float
j = 10.0        #float -> int
k = 254         #int -> byte

print(str(a))
print(float(b))
print(int(c))
print(bool(d))
print(str(e))
print(str(f))
print(int(g, 2))
print(float(h))
print(float(i))
print(int(j))
print(bin(k))