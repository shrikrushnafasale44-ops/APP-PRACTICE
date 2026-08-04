def student():
    yield "Shrikrushna"
    yield "MIT ADT"
    yield "Python"

g = student()

print(next(g))
print(next(g))
print(next(g))
