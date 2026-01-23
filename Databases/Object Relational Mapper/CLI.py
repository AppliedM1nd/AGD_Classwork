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

    def add_activities(self):
        activity = input('Enter activity name: ')
        self.controller.activity_names.append(activity)

    def add_user_activity(self, first_name, last_name):
        new_activity = input('Enter activity name: ')
        self.controller.user.activities.append(new_activity)





if __name__ == '__main__':
    cli = CLI()