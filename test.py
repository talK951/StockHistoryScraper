import re
a = "11111.09\n3445556.22\n-12.3"
print(re.findall("([0-9]+.[0-9]*|-[0-9]+.[0-9])", a))
