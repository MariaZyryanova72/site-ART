import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Articles(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'articles'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    main_image = sqlalchemy.Column(sqlalchemy.String)

    artist_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("artist.id"))

    title = sqlalchemy.Column(sqlalchemy.String)
    preview = sqlalchemy.Column(sqlalchemy.String)
    text = sqlalchemy.Column(sqlalchemy.Text)

    attach_image = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    video_1 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    video_2 = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    create_date = sqlalchemy.Column(sqlalchemy.DateTime)

    artist = orm.relation('Artist')

    # articles = orm.relation("Comment", back_populates='articles')
    # artist = orm.relation("User")
