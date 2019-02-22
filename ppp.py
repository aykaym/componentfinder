from pcpartpicker import API
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbjank import Motherboard, GPU, PSU, RAM, CPU, Case, Drive, Base

api = API()
part_data = api.retrieve_all()

engine = create_engine('sqlite:///parts.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

def get_motherboards(part_data):
    for part in part_data['motherboard']:
        model = str(part.model)
        price = str(part.price)
        socket = str(part.socket)
        form_factor = str(part.form_factor)
        max_ram = str(part.max_ram.gb)
        ram_slots = str(part.ram_slots)

        #insert
        new_part = Motherboard(model=model, price=price, socket=socket,
                               form_factor=form_factor, max_ram=max_ram, ram_slots=ram_slots)
        session.add(new_part)
        session.commit()
        print("Motherboard info for "+model+" has been added to the DB")


def get_gpu(part_data):
    for part in part_data['video-card']:
        model = str(part.model)
        model_line = str(part.model_line)
        chipset = str(part.chipset)
        memory_amount = str(part.memory_amount.gb)
        if part.core_clock is None:
            core_clock = "N/A"
        else:
            core_clock = str(part.core_clock.mhz)
        price = str(part.price)

        #insert
        new_part = GPU(model=model, model_line=model_line, chipset=chipset,
                       memory_amount=memory_amount, core_clock=core_clock, price=price)
        print("GPU info for "+model+" has been added to the DB")
        session.add(new_part)
        session.commit()


def get_cpu(part_data):
    for part in part_data['cpu']:
        model = str(part.model)
        if type(part.clock_speed) == "NoneType":
            clock_speed = "N/A"
        else:
            clock_speed = str(part.clock_speed.ghz)
        cores = str(part.cores)
        tdp = str(part.tdp)
        price = str(part.price)

        #insert
        new_part = CPU(model=model, clock_speed=clock_speed, cores=cores, tdp=tdp, price=price)
        session.add(new_part)
        session.commit()
        print("CPU info for "+model+" has been added to the DB")


def get_memory(part_data):
    for part in part_data['memory']:
        model = str(part.model)
        module_type = str(part.module_type)
        form_factor = str(part.form_factor)
        clock_speed = str(part.speed.ghz)
        num_of_modules = str(part.number_of_modules)
        module_size = str(part.module_size.gb)
        total_size = str(part.total_size.gb)
        price_per_gb = str(part.price_per_gb)
        price = str(part.price)

        new_part = RAM(model=model, module_type=module_type, form_factor=form_factor, clock_speed=clock_speed,
                       num_of_modules=num_of_modules, module_size=module_size, total_size=total_size,
                       price_per_gb=price_per_gb, price=price)

        #insert
        session.add(new_part)
        session.commit()
        print("RAM info for "+model+" has been added to the DB")


def get_powersupply(part_data):
    for part in part_data['power-supply']:
        model = str(part.model)
        model_line = str(part.model_line)
        form_factor = str(part.form_factor)
        efficiency = str(part.efficiency_rating)
        watts = str(part.watt_rating)
        modular = str(part.modular)
        price = str(part.price)

        #insert
        new_part = PSU(model=model, model_line=model_line, form_factor=form_factor, efficiency=efficiency, watts=watts, modular=modular, price=price)
        session.add(new_part)
        session.commit()
        print("PSU info for "+model+" has been added to the DB")


def get_cases(part_data):
    for part in part_data['case']:
        model = str(part.model)
        form_factor = str(part.form_factor)
        internal_bays = str(part.internal_bays)
        external_bays = str(part.external_bays)
        price = str(part.price)

        #insert
        new_part = Case(model=model, form_factor=form_factor, internal_bays=internal_bays, external_bays=external_bays, price=price)
        session.add(new_part)
        session.commit()
        print("Computer Case info for "+model+" has been added to the DB")

def get_drives(part_data):
    for part in part_data['internal-hard-drive']:
        model = str(part.model)
        model_line = str(part.model_line)
        form_factor = str(part.form_factor)
        platter_rpm = str(part.platter_rpm)
        capacity = str(part.capacity.gb)
        cache_amount = str(part.cache_amount)
        price_per_gb = str(part.price_per_gb)
        price = str(part.price)

        new_part = Drive(model=model, model_line=model_line, form_factor=form_factor, platter_rpm=platter_rpm, capacity=capacity,
                         cache_amount=cache_amount, price_per_gb=price_per_gb, price=price)
        session.add(new_part)
        session.commit()


get_motherboards(part_data)
get_gpu(part_data)
get_powersupply(part_data)
get_cases(part_data)
get_memory(part_data)
get_cpu(part_data)
get_drives(part_data)