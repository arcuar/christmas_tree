space_str = " "
star = "* "

space = 0


for i in range(1, 10):
    if i < 4:
        print(space_str * (5 - i), star * i)
    elif 4 <= i < 9:
        print(space_str * (8 - i), star * (i - 3))
    else:
        print(space_str * 4, "|")
        