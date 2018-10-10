nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        continue  # Allows a loop iteration to be skipped
    print(num)
    if num == 4:
        print('Quitting')
        break  # Breaks out of the loop completely

for num in nums[:3]:
    for letter in 'abc':
        print(num, letter)

for i in range(3):
    print(i)

for i in range(1, 4):  # Up to, but not including, second bound
    print(i)

x = 0
while True:  # Interrupt via ctrl + F2 in Pycharm (other IDE maybe ctrl + c)
    print(x)
    if x == 3:
        break
    x += 1
