# #Code implementation API for academic advisor software. \
#The first design pattern is behavioral 'Observer' pattern.\
\
\
\
class Observer:\
    def update(self):\
        pass\
\
class Student(Observer):\
    def update(self):\
        print("Schedule updated")\
\
class Advisor(Observer):\
    def update(self):\
        print("Schedule updated")\
\
class Schedule:\
    def __init__(self):\
        self.observers = []\
\
    def add_observer(self, observer):\
        self.observers.append(observer)\
\
    def remove_observer(self, observer):\
        self.observers.remove(observer)\
\
    def notify_observers(self):\
        for observer in self.observers:\
            observer.update()\
\
    def update_schedule(self):\
        # code implementation to update schedule\
        self.notify_observers()\
}
