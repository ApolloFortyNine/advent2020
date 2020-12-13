f = open('input.txt')
test = f.readlines()
arr = []

for x in test:
    arr.append(int(x.strip()))

for idx, x in enumerate(arr):
    for idx2, y in enumerate(arr[idx+1::]):
        for z in arr[idx2+1::]:
            if x + y + z == 2020:
                print(x*y*z)
    