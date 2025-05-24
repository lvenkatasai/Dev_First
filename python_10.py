arr = [4, 2, 7, 1, 9]
x = int(input("Enter number to search: "))

found = False
for i in range(len(arr)):
    if arr[i] == x:
        found = True
        break

print("Found" if found else "Not found")
