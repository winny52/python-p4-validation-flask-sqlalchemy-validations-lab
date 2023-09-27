import sqlalchemy

from sqlalchemy import CheckConstraint

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

connection = "sqlite:///database.db"
db   = create_engine(connection)
base = declarative_base()

class Patient(base):
    __tablename__ = 'patient'
    name = Column(String(length=50), primary_key=True)
    birth_year = Column(Integer,
                         CheckConstraint('birth_year < 2023'),
                        nullable=False)
    death_year = Column(Integer)
        # Constraint defined at the Table level

    __table_args__ = (
        CheckConstraint('(death_year is NULL) or (death_year >= birth_year)'),
    )


Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)

p1 = Patient(name="Steve", birth_year=2000, death_year=2022)
session.add(p1)
session.commit()


p3 = Patient(name="Brad", birth_year=2025, death_year=2066)
session.add(p3)
session.commit()

p2 = Patient(name="Max", birth_year=2010, death_year=1950)
session.add(p2)



try:
    session.commit()
    print('Success!')
except sqlalchemy.exc.IntegrityError as e:
    print('Invalid ages: integrity violation blocked')
    session.rollback()