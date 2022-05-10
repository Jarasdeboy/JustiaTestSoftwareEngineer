input = "This is the first line and this is the second line, which is longer."
ok = round(len(input) / 2) -2
for x in input[0:ok:1]:
    print(x, end = '')
print('\t')
for x in input[ok:len(input):1]:
    print(x, end = '')
# print(round(len(input) / 2))
# x = input.split(" ")
# s = round(len(x) / 2)
# arr1 = x[0:s]
# arr2 = x[s:len(x)]
# print(arr1)
# print(arr2)