import colorama
import inspect

print(dir(colorama))

for name, obj in inspect.getmembers(colorama):
    print(name, ":", obj.__doc__)









