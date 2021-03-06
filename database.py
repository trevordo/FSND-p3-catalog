import sys

# used for JSON serialization of date and time
import json

# for mapper code
from sqlalchemy import Column, ForeignKey, Integer, String, Date

# declarative_base used configuration and class code 
from sqlalchemy.ext.declarative import declarative_base

# used in foreign key and mapper
from sqlalchemy.orm import relationship

# used in configuration
from sqlalchemy import create_engine

# help setup class code lets sqlalch know its special classes
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String)

class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    # JSON
    @property
    def serialize(self):
        # Returns object data in easily serializable format
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }

class Seminar(Base):
    __tablename__ = 'seminars'

    id = Column(Integer, primary_key = True)
    title = Column(String(80), nullable = False)
    speaker = Column(String(250))
    abstract = Column(String) 
    date_time = Column(Date)
    building = Column(String(80))
    room = Column(String(25))
    department = relationship(Department)
    department_id = Column(Integer, ForeignKey('departments.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    # JSON
    @property
    def serialize(self):
        # Returns object data in easily serializable format
        return {
            'title': self.title,
            'speaker': self.speaker,
            'abstract': self.abstract,
            'date': json.dumps(self.date_time.isoformat()),
            'building': self.building,
            'room': self.room,
        }

####### insert at end of file #######

engine = create_engine('sqlite:///departmentalseminar.db')

# goes into database, adds classes as tables in db
Base.metadata.create_all(engine)