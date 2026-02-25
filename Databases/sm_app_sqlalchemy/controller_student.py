
import sqlalchemy as sa
import sqlalchemy.orm as so

from sm_app_sqlalchemy.models import User, Post, Comment, likes_table


class Controller:
    def __init__(self, db_location='sqlite:///social_media.db'):
        self.current_user_id: int | None = None
        self.viewing_post_user_id: int | None = None
        self.engine = sa.create_engine(db_location)

    def set_current_user_from_name(self, name: str) -> User | None:
        with so.Session(bind=self.engine) as session:
            user = session.scalars(
                sa.select(User).where(User.name == name)
            ).one_or_none()

            if user is None:
                self.current_user_id = None
                return None

            self.current_user_id = user.id
            return True

    def get_user_name(self, user_id: int | None = None) -> str:
        if user_id is None:
            user_id = self.current_user_id

        with so.Session(bind=self.engine) as session:
            user = session.get(User, user_id)
            return user.name if user else None

    def get_user_names(self) -> list[str]:
        with so.Session(bind=self.engine) as session:
            user_names = session.scalars(
                sa.select(User.name).order_by(User.name)
            ).all()
        return list(user_names)

    def get_user_posts(self, user_id: int):
        with so.Session(bind=self.engine) as session:
            posts = session.scalars(
                sa.select(Post).where(Post.user_id == user_id)
            ).all()
            user_dict = []
            for post in posts:
                like_total = session.scalar(
                    sa.select(sa.func.count(likes_table.c.user_id))
                    .where(likes_table.c.post_id == post.id)
                )
                user_dict.append({'id': post.id,
                         'title': post.title,
                         'description': post.description,
                         'likes': like_total,
                         'user_id': post.user_id})
        return user_dict

    def get_all_posts(self):
        with so.Session(bind=self.engine) as session:
            posts = session.scalars(
                sa.select(Post)
                .order_by(Post.id)
            ).all()
            post_dict = []
            for post in posts:
                like_total = session.scalar(
                    sa.select(sa.func.count(likes_table.c.user_id))
                    .where(likes_table.c.post_id == post.id)
                )
                post_dict.append({'id': post.id,
                     'title': post.title,
                     'description': post.description,
                     'likes': like_total,
                     'user_id': post.user_id})
        return post_dict


    #def get_user_comments(self, user_id: int):
    #    with so.Session(bind=self.engine) as session:
    #        comments = session.scalars(
    #            sa.select(Comment).where(Comment.user_id == user_id)
    #        ).all()

    #    return [(comment.comment, comment.post_id) for comment in comments]

    def add_user_to_db(self, name, age, gender, nationality):
        with so.Session(bind=self.engine) as session:
            new_user = User(
                name=name,
                age=age,
                gender=gender,
                nationality=nationality
            )
            session.add(new_user)
            session.commit()

    #def remove_user_from_db(self, user_id: int):
    #    with so.Session(bind=self.engine) as session:
    #        user = session.get(User, user_id)
    #        if user:
    #            session.delete(user)
    #            session.commit()

    def add_user_comment(self, user_id: int, post_id: int, comment: str):
        with so.Session(bind=self.engine) as session:
            new_comment = Comment(
                user_id=user_id,
                post_id=post_id,
                comment=comment
            )
            session.add(new_comment)
            session.commit()

    def create_user_post(self, user_id: int, title: str, description: str):
        with so.Session(bind=self.engine) as session:
            new_post = Post(
                title=title,
                description=description,
                user_id=user_id
            )
            session.add(new_post)
            session.commit()

    def user_likes_post(self, user_id: int, post_id: int):
        with so.Session(bind=self.engine) as session:
            user = session.get(User, user_id)
            post = session.get(Post, post_id)

            if not user or not post:
                return 'User or Post not found'

            if post not in user.liked_posts:
                user.liked_posts.append(post)
                session.commit()
            else:
                return 'Already liked this post'
            return 'Liked post'

    def view_post(self, post_id: int):
        with so.Session(bind=self.engine) as session:
            post = session.get(Post, post_id)
            if not post:
                return False
            return {'title': post.title,
                    'description': post.description,
                    'user_id': post.user_id,
                    'likes': post.number_of_likes}

    def view_post_comments(self, post_id: int):
        with so.Session(bind=self.engine) as session:
            comments = session.scalars(
                sa.select(Comment)
                .where(Comment.post_id == post_id)
            ).all()
            if not comments:
                return ''
            return [{'user_name': comment.user.name,
                     'comment': comment.comment}
                    for comment in comments]



if __name__ == '__main__':
    controller = Controller()
    controller.set_current_user_from_name('Alice')
