import re

n = input()
p = input()

result = re.search(p, n, re.IGNORECASE)
if result:
    print("{} contains {}".format(n, p))
else:
    print("{} does not conatin {}".format(n, p))