class Student:
   MAX_LENGTH = 20

   @classmethod
   def validate_length(cls, name):
       return len(name) <= cls.MAX_LENGTH

   @staticmethod
   def validate_name(name):
       return name.isalpha()


name = input()
print(Student.validate_length(name))
print(Student.validate_name(name))