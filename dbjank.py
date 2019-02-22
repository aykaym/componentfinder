from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Motherboard(Base):
    __tablename__ = 'Motherboard'
    id = Column(Integer, primary_key=True)
    model = Column(String(250))
    form_factor = Column(String(250))
    socket = Column(String(250))
    ram_slots = Column(String(250))
    max_ram = Column(String(250))
    price = Column(String(250))


class GPU(Base):
    __tablename__ = 'GPU'
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable = True)
    model_line = Column(String(250))
    chipset = Column(String(250))
    memory_amount = Column(String(250))
    core_clock = Column(String(250))
    price = Column(String(250))


class PSU(Base):
    __tablename__ = "PSU"
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable = False)
    model_line = Column(String(250))
    form_factor = Column(String(50))
    efficiency = Column(String(50))
    watts = Column(String)
    modular = Column(String(250))
    price = Column(String(250))


class RAM(Base):
    __tablename__ = "RAM"
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    module_type = Column(String(50))
    form_factor = Column(String(50))
    clock_speed = Column(String(50))
    num_of_modules = Column(String(50))
    module_size = Column(String(250))
    total_size = Column(String(250))
    price_per_gb = Column(String(250))
    price = Column(String(250))


class CPU(Base):
    __tablename__ = "CPU"
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    price = Column(String(250))
    clock_speed = Column(Integer)
    cores = Column(Integer)
    tdp = Column(Integer)


class Case(Base):
    __tablename__ = "Case"
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    form_factor = Column(String(250))
    internal_bays = Column(Integer)
    external_bays = Column(Integer)
    price = Column(String(250))

class Drive(Base):
    __tablename__ = "Drive"
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    model_line = Column(String(250))
    form_factor = Column(String(250))
    platter = Column(String(250))
    capacity = Column(String(250))
    cache_amount = Column(String(250))
    price_per_gb = Column(String(250))
    price = Column(String(250))

engine = create_engine('sqlite:///parts.db')

Base.metadata.create_all(engine)