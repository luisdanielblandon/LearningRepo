class Person:
      def __init__(self, name, age, occupation):
            self.name = name
            self.age = age
            self.occupation = occupation

      #functions to get/return parameters
      def get_name(self):
            return self.name
      
      def get_age(self):
            return self.age
      
      def get_occupation(self):
            return self.occupation
      
class Student(Person):
      def __init__(self, name, age, occupation, subjects):
            Person.__init__(self, name, age, occupation)
            self.subjects = subjects

      def get_subjects(self):
            return self.subjects

      
person1 = Student('Greg',35,'Plumber',['Math','English','Music'])
person2 = Student('Steve',21,'Bartender',['Science','Math','Art'])
person3 = Student('Mark',26,'Gigolo',['English','French','German'])

print("There are 3 people currently defined. Below are their names, ages, and occupations.")

print(person1.name, person1.age, person1.occupation, person1.subjects)
print(person2.name, person2.age, person2.occupation, person2.subjects)
print(person3.name, person3.age, person3.occupation, person3.subjects)
