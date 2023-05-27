#!/usr/bin/python3

fruits = ["apple", "banana", "mango", "orange", "mango", "grape", "mango", "pear", "kiwi", "mango"]

for fruit in fruits:
    if fruit == "mango":
        print("Found a mango!")
        break
else:
    print("Mango not found in the basket.")

for apollo in fruits:
    print(apollo)
    if apollo == "banana":
        print("I love banana and I am happy it is in the basket")

        break
# Break is used to terminate the loop on the first occasion it finds the
# the fruit banana
