import sqlalchemy
from sqlalchemy import Column, VARCHAR, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

SQLITE = 'sqlite:///database/database.db'
engine = create_engine(SQLITE, echo=True, connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    name = Column(String, nullable=False)
    username = Column(String)
    join_date = Column(DateTime)
    warns = Column(Integer)
    pool_count = Column(Integer)

    def commit(self):
        session.add(self)
        session.commit()

    def warning(self):
        try:
            self.warns +=1
        except TypeError:
            self.warns = 1
        finally:
            return self.warns
        session.commit()
        

    @classmethod
    def get(cls, userid):
        user = session.query(cls).filter_by(user_id=userid).first()
        if user:
            return user
        else:
            return None
    @classmethod
    def create(cls, userid, name):
        user = cls(
            user_id=userid,
            name=name
            )
        session.commit()
        return user

    def delete(self):
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f"User {self.name} {self.user_id}"

# Base.metadata.create_all(engine)

