#!/usr/bin/python3

""" This module is a test for sqlalchemy practice """

import sqlalchemy as db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = db.create_engine(
        'mysql+mysqldb://vagrant:PASS@localhost/ua_high_alchemy',
        echo=True)

Base = declarative_base()

class User(Base):
	""" User class for base object """

	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, unique=True, nullable=False)
	name  = Column(String(40), unique=True)
	quirk = Column(String(35))

	def __repr__(self):
		""" Replaces the default __str__(ing) behavior """

		return f"<User(name='{self.name}', quirk='{self.quirk}')>"


Base.metadata.create_all(engine)

num_one = User(name='Zuko', quirk='Firebending')

# print(num_one.name)

Session = sessionmaker(bind=engine)

session = Session()

# num_one

session.add(num_one)
# our_user = session.query(User).filter_by(name='Zuko').first()
# our_user
# num_one is our_user

num_two = User(name='Boss', quirk='Mafia Lead')
num_three = User(name='Crook', quirk='Weakening')

session.add_all([num_two, num_three])
# session.dirty
# session.new

session.commit()

# num_one.id
# num_two.id
# num_three.id

# for instance in session.query(User).order_by(User.id):
# 	print(instance.name, instance.quirk)

# for name, quirk in session.query(User.name, User.quirk):
# 	print(name, quirk)

# for name, quirk in session.query(User.name, User.quirk).order_by(name):
# 	print(name, quirk)

# for name, quirk in session.query(User.name, User.quirk).order_by(User.name):
#	print(name, quirk)

# import readline
# readline.write_history_file('/home/vagrant/my_practice/ua_high/sql_alchemy.py')
