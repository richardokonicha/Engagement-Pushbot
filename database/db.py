
import sqlalchemy
from sqlalchemy import Column, VARCHAR, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import exists
import datetime

SQLITE = 'sqlite:///database/database.db'
engine = create_engine(SQLITE, echo=True, connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Users(Base):
    """User class"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)
    name = Column(String, nullable=False)
    username = Column(String)
    join_date = Column(DateTime)
    warns = Column(Integer)
    pool_count = Column(Integer)

    def commit(self):
        """commits query object to db"""
        session.add(self)
        session.commit()

    def warning(self):
        """increament warn by 1 everytime its called"""
        try:
            self.warns +=1
        except TypeError:
            self.warns = 1
        finally:
            session.commit()
            return self.warns
        
    def engaged(self):
        try:
            self.pool_count +=1
        except TypeError:
            self.pool_count=1
        finally:
            session.commit()
            return self.pool_count

    @classmethod
    def get(cls, userid):
        """retrive user from id"""
        user = session.query(cls).filter_by(user_id=userid).first()
        if user:
            return user
        else:
            return None
    @classmethod
    def create(cls, userid, name):
        """create new users by passing user id and name"""
        user = cls(
            user_id=userid,
            name=name
            )
        session.add(user)
        session.commit()
        return user

    def delete(self):
        """delete user object"""
        session.delete(self)
        session.commit()

    def __repr__(self):
        return f"User {self.name} {self.user_id}"


class Rounds(Base):
    __tablename__="rounds"
    id = Column(Integer, primary_key=True)
    start_time = Column(DateTime)
    memberlist = relationship("MemberList", uselist=True, backref="round")

    def __init__(self, start_time):
        """initializes rounds and set start time"""
        if type(start_time) == str:
            self.start_time = datetime.datetime.fromisoformat(start_time)
        else:
            self.start_time = start_time

    @classmethod
    def create(cls, start_time):
        """create round function by passing in time"""
        rounds = cls(
            start_time
            )
        session.add(rounds)
        session.commit()
        return rounds

    @classmethod
    def create_now(cls):
        """create round function immediately"""
        start_time = datetime.datetime.now()
        rounds = cls(
            start_time
            )
        session.add(rounds)
        session.commit()
        return rounds

    def start(self):
        """retrieve the start time of round"""
        return self.start_time

    def end(self):
        """retrieve the end time of round"""
        return self.start_time + datetime.timedelta(minutes=20)

    def drop_duration(self):
        """returns time left time drop username period ends and returns false after it ends"""
        delta = self.start_time + datetime.timedelta(seconds=30)
        now = datetime.datetime.now()
        if now > delta:
            return False
        else:
            return (delta-now).seconds

    def join(self, user):
        """adds user to round by passing in the user object"""
        user_id = user.user_id
        # if MemberList.exist(user_id):
        #     self.memberlist
        #     return True
        # else:
        entry = MemberList(
            round_id=self.id,
            user=user
            )
        session.add(entry)
        session.commit()
    
    @classmethod
    def get_round(cls, id):
        """get round object by id"""
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def get_memberList(cls, id):
        """get list of all members in that round"""
        return session.query(MemberList).all()

    @classmethod
    def get_lastRound(cls):
        """get last round"""
        return session.query(Rounds).all()[-1]

    def commit(self):
        """add and commit session changes to db"""
        session.add(self)
        session.commit()

    def __repr__(self):
        """string representation of object"""
        return f"Round {self.id} {str(self.start_time)}"


class MemberList(Base):
    """member list class"""
    __tablename__="memberlist"
    id = Column(Integer, primary_key=True)
    round_id = Column(Integer, ForeignKey("rounds.id"))
    #userinfo
    user_id = Column(Integer)
    name = Column(String)
    username = Column(String)

    def __init__(self, round_id, user):
        self.round_id = round_id
        self.user_id = user.user_id
        self.name = user.name
        self.username = user.username

    @classmethod
    def all(cls):
        return session.query(cls).all()

    @classmethod
    def exist(cls,user_id):
        """checks if user is on the list returns boolean"""
        return session.query(exists().where(cls.user_id==user_id)).scalar()

    def __repr__(self):
        return f"MemberList {self.name} round{self.round_id}"


# Base.metadata.create_all(engine)


# import pdb; pdb.set_trace()
