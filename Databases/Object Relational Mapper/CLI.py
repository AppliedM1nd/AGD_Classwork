# import pyinputplus as pyip

from controller import Controller

class CLI:
    def __init__(self):
        self.controller = Controller()

    def show_person_activities(self):
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        activities = self.controller.get_person_activities(first_name, last_name)
        for activity in activities:
            print(activity)


    def show_activity_persons(self):
        activity_name = input('Enter activity name: ')
        persons = self.controller.get_activity_persons(activity_name)
        for person in persons:
            print(person)

    def add_activity(self):
        activity = input('Enter activity name: ')
        self.controller.insert_activity(activity)

    def add_person(self):
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        self.controller.insert_person(first_name, last_name)

    def remove_activity(self):
        activity_name = input('Enter activity name: ')
        self.controller.remove_activity(activity_name)

    def remove_person(self):
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')
        self.controller.remove_person(first_name, last_name)
        
if __name__ == '__main__':
    cli = CLI()
