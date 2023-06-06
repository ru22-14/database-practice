from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Favourite destinations" table
class Country(base):
    __tablename__ = "Country"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    capital = Column(String)
    language = Column(String)
    famous_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records for favourite destinations
Turkey = Country(
    name="Turkey",
    capital="Istambul",
    language="Turkish",
    famous_for="sea, landscapes, food, historic places"
)

session.add(Turkey)
session.commit()

countries = session.query(Country)
for country in countries:
    print(
        country.id,
        country.name,
        country.capital,
        country.language,
        country.famous_for,
        sep=" | "
    )
