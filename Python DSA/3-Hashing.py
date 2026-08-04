numbers = [4, 7, 2, 9, 7, 3]
seen = set()

for x in numbers:
    if x in seen:
        print("Duplicate:", x)
        break

    seen.add(x)
#Yes — with one correction: using a set for membership checking is one of the most efficient approaches when your problem is "does this value exist?"