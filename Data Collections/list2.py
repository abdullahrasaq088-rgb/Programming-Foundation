food = ["rice", "beans", "chicken", "beef", "pork", "fish", "vegetables", "fruits"]
names = ["John", "Mary", "Peter", "Jane", "Paul"]
#reading the content of the list
print(food[1])
#updating the content of the list
food[1] = "yam"
print(food[1])
print(food)
#removing an item from the list
food.remove("chicken")
print(food)
#appending an item to the list
food.append("eggs")
print(food)
print(len(food))
print(food.pop())
print(len(names))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(nums))