
from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

	@abstractstaticmethod
	def person_method():
		"""interface method"""


class Student(IPerson):

	def __init__(self):
		self.name = "Basic Student name"

	def person_method(self):
		print ("Student called")


class Teacher(IPerson):

	def __init__(self):
		self.name = "Basic Teacher name"

	def person_method(self):
		print ("Teacher called")



class PersonFactory():

	@staticmethod
	def build_person(choice):

		if choice == "Student":
			return Student()

		if choice == "Teacher":
			return Teacher()

		print ("Pass valid choice")


x = input("input choice\n")
person = PersonFactory.build_person(x)
person.person_method()

