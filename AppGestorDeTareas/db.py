from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///database/tareas.db',
connect_args = {'check_same_thread': False})

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
