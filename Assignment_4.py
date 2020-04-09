# # List of string
# list2 = [1, 1, 3]

# # List of string
# list1 = [1, 3, 2, 5, 1, 2 ]

# result = all(elem in list1 for elem in list2)

# if result:
#     print("It's a match")
# else:
#     print("It's gone")


find = list(map(int, input().split()))

listy = list(map(int, input().split()))

le = len(find)
f = 0
for i in range(le):

    try:
        ind = listy.index(find[i])
        # print(ind)
        listy = listy[ind+1:]
    except ValueError:
        f = 1
        break

if(f == 0):
    print("its a match")
else:
    print("its gone")
