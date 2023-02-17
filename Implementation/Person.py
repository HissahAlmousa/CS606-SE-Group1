# #Code implementation API for academic advisor software. \
#The second design pattern is creational 'Person' pattern.\
\
\
from abc import ABC, abstractmethod\
\
class Person(ABC):\
    @abstractmethod\
    def login(self, ID, Password):\
        pass\
\
class Student(Person):\
    def login(self, ID, Password):\
        # Implementation to check student login credentials\
        pass\
\
class Advisor(Person):\
    def login(self, ID, Password):\
        # Implementation to check advisor login credentials\
        pass\
\
class PersonFactory:\
    def create_person(ID, Password):\
        if is_student(ID, Password):\
            return Student()\
        elif is_advisor(ID, Password):\
            return Advisor()\
        else:\
            raise ValueError("Invalid login credentials")\
}
