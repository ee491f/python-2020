list_of_fruits = [
    "apple",
    "banana",
    "cherry",
]

for fruit in list_of_fruits:
    if fruit == "banana":
        #continue
        #break
        pass
    print(fruit)
else:
    print("at the end")

for number in range(2,5):
    print(number)


count = 10
while count < 15:
    print(count)
    count += 1  # This is the same as count = count + 1