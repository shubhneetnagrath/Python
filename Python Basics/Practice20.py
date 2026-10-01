def max_pyramid(B, R):
    def build(first):
        blue = B
        red = R
        height = 0
        row = 1

        while True:
            if first == "B":
                if row % 2 == 1:
                    if blue < row:
                        break
                    blue -= row
                else:
                    if red < row:
                        break
                    red -= row
            else:
                if row % 2 == 1:
                    if red < row:
                        break
                    red -= row
                else:
                    if blue < row:
                        break
                    blue -= row

            height += 1
            row += 1

        return height

    return max(build("B"), build("R"))