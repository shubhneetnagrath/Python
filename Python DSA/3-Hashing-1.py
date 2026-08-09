numbers = [4, 7, 2, 9, 7, 3]
seen = set()

for x in numbers:
    if x in seen:
        print("Duplicate:", x)
        break

    seen.add(x)
