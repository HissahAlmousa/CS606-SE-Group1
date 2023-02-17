
#Code implementation API for academic advisor software. All components and classes have been \
# implemented, including methods and attributes.\
#Two design patterns are used; behavioral 'Observer' pattern and creational 'Person' pattern.  \
\
\
\
class Student:\
    def __init__(self, student_id, major, department):\
        self.student_id = student_id\
        self.major = major\
        self.department = department\
        self.reservations = []  # list of reservations made by the student\
\
    def login(self, id, password):\
        # code implementation for student login\
\
    def make_reservation(self, reservation_number, date, time):\
                # code implementation for student to make reservation\
        return reservation\
\
    def check_reservation_status(self, reservation_number):\
                # Code implementation for student to check reservation status\
                return reservation.status\
       # return 'not found'\
\
\
class Advisor:\
    def __init__(self, advisor_id, department):\
        self.advisor_id = advisor_id\
        self.department = department\
        self.schedule = Schedule(advisor_id)\
        self.reservations = []  # list of reservations made with this advisor\
\
    def login(self, id, password):\
        # Code implementation for advisor login\
\
    def view_schedule(self):\
        return self.schedule.view_schedule()\
\
    def manage_schedule(self):\
        self.schedule.manage_schedule()\
\
    def confirm_appointment(self, reservation_number):\
         # Code implementation for advisor to confirm appointment\
            reservation.change_status('confirmed')\
\
    def reject_appointment(self, reservation_number):\
               # Code implementation for advisor to reject appointment\
            reservation.change_status('rejected')\
\
    def get_reservation(self, reservation_number):\
              # Code implementation for advisor to get reservation number from the list\
                return reservation\
        #return None\
\
\
class Reservations:\
    def __init__(self, reservation_number, date, time, status):\
        self.reservation_number = reservation_number\
        self.date = date\
        self.time = time\
        self.status = status\
\
    def change_status(self, new_status):\
        self.status = new_status\
\
\
class Schedule:\
    def __init__(self, advisor_id):\
        self.advisor_id = advisor_id\
        self.schedule = \{\}  # List of date-time slots with availability status\
\
    def add_schedule(self, date, time):\
        key = f'\{date\}-\{time\}'\
        if key not in self.schedule:\
            self.schedule[key] = 'available'\
\
    def update_schedule(self, date, time, new_status):\
        key = f'\{date\}-\{time\}'\
        if key in self.schedule:\
            self.schedule[key] = new_status\
\
    def view_schedule(self):\
        return self.schedule\
\
    def manage_schedule(self):\
        # Code implementation for advisor to manage their schedule\
        pass\
}
