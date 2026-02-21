import pyinputplus as pyip

from controller_student import Controller


class CLI:
    def __init__(self):
        self.controller = Controller()
        self.current_menu = self.login
        self.running = True
        self.run_menus()

    @staticmethod
    def show_title(title):
        print('\n' + title)
        print('-' * len(title) + '\n')

    def run_menus(self):
        while self.running:
            self.current_menu = self.current_menu()

    def exit_menus(self):
        self.running = False
        print("Goodbye")

    def login(self):
        self.show_title('Login Screen')
        users = self.controller.get_user_names()

        menu_items = [
            'Login',
            'Create a new account',
            'Exit',
        ]

        menu_choice = pyip.inputMenu(
            menu_items,
            prompt='Select option:\n',
            numbered=True,
        )

        if menu_choice.lower() == 'create a new account':
            next_menu = self.create_account

        elif menu_choice.lower() == 'exit':
            next_menu = self.exit_menus

        else:
            user_name = input('Enter your name: ')
            if user_name in users:
                self.controller.set_current_user_from_name(user_name)
                next_menu = self.user_home
            else:
                print(f'Name: "{user_name.title()}" not recognised')
                next_menu = self.login

        return next_menu

    def create_account(self):
        self.show_title('Create Account')

        user_name = input('Enter a name: ')
        while user_name == '':
            user_name = input('Enter a name: ')

        user_age = input('Enter your age: ')
        user_gender = input('Enter your gender: ')
        user_nationality = input('Enter your nationality: ')

        self.controller.add_user_to_db(
            user_name,
            user_age,
            user_gender,
            user_nationality
        )

        return self.login

    def user_home(self):
        user_name = self.controller.get_user_name()
        self.show_title(f'User Home - {user_name.title()}')

        choice = input('Do you want to:\n1. View Posts\n2. Create Post\n3. View Specific Post')

        if choice == '1':
            return self.view_posts
        elif choice == '2':
            return self.create_post
        elif choice == '3':
            return self.view_specific_post
        else:
            return self.user_home

    def view_posts(self):
        self.show_title('View Posts')
        posts = self.controller.get_all_posts()
        if not posts:
            print('No posts found.')
        else:
            for post in posts:
                print('PostID: ' , post.id)
                print('Title: ' , post.title)
                print('Description: ' , post.description)
                print('Number of likes: ' , post.number_of_likes)

        input("\nPress Enter to return...")
        return self.user_home

    def create_post(self):
        self.show_title('Create Post')
        user_id = self.controller.current_user_id
        title = input('Enter a title: ')
        description = input('Enter a description: ')
        self.controller.create_user_post(user_id, title, description)
        print('Post made')
        input("\nPress Enter to return...")
        return self.user_home

    def view_specific_post(self):
        self.show_title('View Specific Post')
        post_id = int(input('Enter a post ID: '))
        post = self.controller.view_post(post_id)
        if not post:
            print('No post found.')
            input("\nPress Enter to return...")
            return self.user_home
        print('Title:', post[0])
        print('Description:', post[1])
        print('User ID:', post[2])
        print('Number of likes:', post[3])
        state = 1
        while state in (1,2,3):
            state = input("\nPress 1 to add a comment. Press 2 to like the post. Press 3 to view comments. Press anything else to return to the main menu")
            user_id = self.controller.current_user_id
            if state == '1':
                comment = input('Enter a comment: ')
                self.controller.add_user_comment(user_id ,post_id, comment)
            elif state == '2':
                print(self.controller.user_likes_post(user_id, post_id))
            elif state == '3':
                comments = self.controller.view_post_comments(post_id)
                if comments:
                    print('Comments:')
                    for comment in comments:
                        print(f'{comment.user.name}: {comment.comment}')
                else:
                    print('No comments found.')
        return self.user_home



if __name__ == '__main__':
    cli = CLI()
