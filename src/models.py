import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

# Definición de la clase Character
class Character(Base):
    __tablename__ = 'characters'
    uid = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)

# Definición de la clase Planet
class Planet(Base):
    __tablename__ = 'planets'
    uid = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)

class Starship(Base):
    __tablename__ = 'starships'
    uid = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)

# Asumiendo que ya has instalado SQLAlchemy e importado los módulos necesarios

# Tabla User
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    subscription_date = Column(String, nullable=False)
    birth_date = Column(Integer)
    country = Column(String)

# Tabla User_Character
class Favorite_Character(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    character_uid = Column(Integer, ForeignKey('characters.uid'), nullable=False)

# Tabla User_Planet
class Favorite_Planet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    planet_uid = Column(Integer, ForeignKey('planets.uid'), nullable=False)

# Tabla User_Starship
class Favorite_Starship(Base):
    __tablename__ = 'favorite_starships'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    starship_uid = Column(Integer, ForeignKey('starships.uid'), nullable=False)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
