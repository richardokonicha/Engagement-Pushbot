import os
import sqlalchemy
from sqlalchemy import Column, VARCHAR, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import exists
import datetime
from dotenv import load_dotenv
load_dotenv()

DEBUG = (os.getenv("DEBUG") == 'True')
SQLITE = 'sqlite:///database/database.db'
POSTGRES = "postgres://rforqrdhlqmfxx:b14d546ae3987101caf9f8b854a8112aff3289f541e8b8e2e41f1608d7f358bf@ec2-35-171-31-33.compute-1.amazonaws.com:5432/dck7k613k9q79l"

if DEBUG == True:
    engine = create_engine(SQLITE, echo=True, connect_args={'check_same_thread': False})
if DEBUG == False:
    engine = create_engine(POSTGRES, echo=True)
    

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
    blocked = Column(Boolean)
    lang = Column(String)


    def __init__(self, user_id, name, username=None, join_date=None, warns=0, pool_count=0, blocked=False, lang="de"):
        self.user_id = user_id
        self.name = name
        self.lang = lang
        self.username = username
        self.join_date = join_date
        self.warns = warns
        self.pool_count = pool_count
        self.blocked = blocked

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
            if self.warns>=3:
                self.blocked=True
            session.commit()
            return self.warns
        
    # def blocked(self):
    #     if self.warns >= 3:
    #         return True
    #     else:
    #         return False
        
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
    def get_username(cls, username):
        """retrive user from username"""
        user = session.query(cls).filter_by(username=username).first()
        if user:
            return user
        else:
            return None


    @classmethod
    def get_ids(cls):
        userall = session.query(cls).all()
        users = [i.user_id for i in userall]
        return users
    
    @classmethod
    def get_users(cls):
        userall = session.query(cls).all()
        users = [i for i in userall]
        return users

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

    @classmethod
    def delete_user(cls, userid):
        """retrive user from id"""
        user = session.query(cls).filter_by(user_id=userid).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        else:
            return None

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

    def check_time(self):
        t = self.end() - datetime.timedelta(seconds=10)
        return t 

    def end(self):
        """retrieve the end time of round"""
        return self.start_time + datetime.timedelta(seconds=60)

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


Base.metadata.create_all(engine)


# import pdb; pdb.set_trace()
