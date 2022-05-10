num = 99
desc = 98
while num <= 99 and num >= 0:
    print("No more" if num == 0 else num,"bottles of beer on the wall,","no more" if num == 0 else num,"bottles of beer.", end="\n")
    print("Go to the store and buy some more," if num == 0 else "Take one down and pass it around,","no more" if desc == 0 else "99","bottles of beer on the wall.")
    num -= 1
    desc -= 1
    print("\n")
