import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List, Optional

class Base(so.DeclarativeBase):
    pass

likes_table = sa.Table(
    'likes',
    Base.metadata,
    sa.Column('user_id', sa.Integer, sa.ForeignKey(column = 'users.id', ondelete='CASCADE'),
              primary_key=True),
    sa.Column('post_id', sa.Integer, sa.ForeignKey(column = 'posts.id', ondelete='CASCADE'),
              primary_key=True),
)


class User(Base):
    def __repr__(self):
        return f"User(name='{self.name}', age = '{self.age}', gender = '{self.gender}', nationality = '{self.nationality}')"

    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    age: Mapped[Optional[int]]
    gender: Mapped[Optional[str]]
    nationality: Mapped[Optional[str]]
    liked_posts: Mapped[list['Post']] = relationship(
        secondary=likes_table,
        back_populates='liked_by_users',
    )

class Post(Base):
    def __repr__(self):
        return f"Post(title='{self.title}', content = '{self.content}', user = '{self.user}')"

    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(index=True)
    content: Mapped[str] = mapped_column(index=True)
    user: Mapped[User] = relationship(User,)

class Comment(Base):
    def __repr__(self):
        return f"User(post_id='{self.post_id}', user_id = '{self.user_id}')"

    __tablename__ = 'comments'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    post_id: Mapped[int] = mapped_column(unique=True, index=True)
    user_id: Mapped[int] = mapped_column(
        sa.ForeignKey('users.id', ondelete = 'CASCADE'), nullable=False
    )
    post_id: Mapped[int] = mapped_column(
        sa.ForeignKey('posts.id', ondelete = 'CASCADE'), nullable=False
    )
    user: Mapped['User'] = so.relationship(back_populates='comments_made')

    comments_made: Mapped[list['Comment']] = relationship(
        back_populates='user',
        cascade='all, delete-orphan',
    )