def find_apple(fruits):
    for fruit in fruits:
        if fruit == "apple":
            print("Found an apple!")
            break
    else:
        print("No apple found.")

fruits_a = ["apple", "banana", "cherry"]
fruits_b = ["banana", "cherry"]

find_apple(fruits_a)
find_apple(fruits_b)