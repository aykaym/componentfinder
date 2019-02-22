from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbjank import Motherboard, GPU, PSU, RAM, CPU, Case, Base


engine = create_engine('sqlite:///parts.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

for mobo in session.query(Motherboard).filter():
     print(mobo.model)
