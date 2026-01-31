import sqlalchemy as sa
import sqlalchemy.orm as so

from models import Base, Person, Activity


class Controller:
    def __init__(self, db_location = 'sqlite:///activities.sqlite'):
        self.engine = sa.create_engine(db_location)
        Base.metadata.create_all(self.engine)

    def get_person_activities(self, first_name, last_name):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Person).where(Person.first_name == first_name and Person.last_name == last_name)
            user = session.scalar(stmt)
            if user is None:
                return []
            activities = user.activities
            activities = user.activities
            activity_names = [activity.name for activity in activities]
        return activity_names

    def get_person_names(self):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Person)
            persons = session.scalars(stmt).all()
            person_names = [(person.first_name, person.last_name) for person in persons]
        return person_names

    def get_activity_names(self):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Activity)
            activities = session.scalars(stmt).all()
            activity_names = [activity.name for activity in activities]
        return activity_names

    def get_activity_persons(self, name):
        with so.Session(bind=self.engine) as session:
            stmt = sa.select(Activity).where(Activity.name == name)
            activity = session.scalar(stmt)
            attendees = activity.attendees
            attendee_names = [(attendee.first_name, attendee.last_name) for attendee in attendees]
        return attendee_names

    def insert_person(self, first_name, last_name):
        with so.Session(bind=self.engine) as session:
            person = Person(first_name=first_name, last_name=last_name)
            session.add(person)
            session.commit()

    def insert_activity(self, name):
        with so.Session(bind=self.engine) as session:
            activity = Activity(name = name)
            session.add(activity)
            session.commit()

    def remove_person(self, first_name, last_name):
        with so.Session(bind=self.engine) as session:
            stmt = sa.delete(Person).where(Person.first_name == first_name and Person.last_name == last_name)
            session.execute(stmt)
            session.commit()

    def remove_activity(self, name):
        with so.Session(bind=self.engine) as session:
            stmt = sa.delete(Activity).where(Activity.name == name)
            session.execute(stmt)
            session.commit()

    def add_person_to_activity(self, first_name, last_name, activity_name):
        with so.Session(bind=self.engine) as session:
            person = session.scalar(sa.select(Person).where(Person.first_name == first_name and Person.last_name == last_name))
            activity = session.scalar(sa.select(Activity).where(Activity.name == activity_name))

            if person is None or activity is None:
                return False

            if activity not in person.activities:
                person.activities.append(activity)
                session.commit()

            return True




if __name__ == '__main__':
    controller = Controller()
