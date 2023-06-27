import pickle

class ToDo:
	def __init__(self, title, important, category = "Normal"):
		self.title = title
		self.important = important
		self.category = category

todos = [ToDo("Walk Dog", True), ToDo("Eat Cheese", False), ToDo("Learn Python", True, category = "Work")]

age = [33,25,3,23,45,67]

file = open("test.txt", "wb")
pickle.dump(todos, file)
file.close()

file = open("test.txt", "rb")
new_todos = pickle.load(file)
file.close()

print(new_todos)


