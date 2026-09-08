# Program 30
# Tuple Comparison

tuple1 = (10, 20, 30)
tuple2 = (5, 25, 30)

if tuple1 > tuple2:
    print("Tuple1 is Greater")
else:
    print("Tuple2 is Greater")

if tuple1 == tuple2:
    print("Both Tuples are Identical")
else:
    print("Tuples are Different")

combined = tuple(set(tuple1 + tuple2))

print("Combined Tuple :", combined)