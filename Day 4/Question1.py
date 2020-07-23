import re

a="we are what we are. we are python programmers"
l=[m.start() for m in re.finditer("we",a )]
print(l)
