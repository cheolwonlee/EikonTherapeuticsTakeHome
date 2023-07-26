import pandas as pd
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from collections import Counter

Base = declarative_base()

engine = create_engine('postgresql://robin:lee123@localhost:5432/postgres_db')

class Users(Base):
    __tablename__ = 'users' 
    user_id = db.Column(db.INT,
                           primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    signup_date = db.Column(db.DATE)

class Compounds(Base):
    __tablename__ = 'compounds' 
    compound_id = db.Column(db.INT,
                           primary_key=True)
    compound_name = db.Column(db.String(50))
    compound_structure = db.Column(db.String(50))

class User_Experiments(Base):
    __tablename__ = 'user_experiments' 
    experiment_id = db.Column(db.INT,
                           primary_key=True)
    user_id = db.Column(db.INT)
    experiment_compound_ids = db.Column(db.ARRAY(db.INT))
    experiment_run_time = db.Column(db.INT)

def get_experiments_for_user(user):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(
        Users,User_Experiments
    ).filter(
        Users.user_id == User_Experiments.user_id
    ).filter(
        Users.name == user
    ).all()
    return len(result)

def get_average_amount_per_user(user):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(
        User_Experiments.experiment_run_time
    ).filter(
        Users.user_id == User_Experiments.user_id
    ).filter(
        Users.name == user
    ).all()
    sum = 0
    for res in result:
        sum+=res[0]
    avg = sum/len(result)
    return avg

def get_users_most_commonly_used_compound(user):
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(
        User_Experiments.experiment_compound_ids
    ).filter(
        Users.user_id == User_Experiments.user_id
    ).filter(
        Users.name == user
    ).all()

    flat_list = []
    for res in result:
        for c in res[0]:
            if c.isnumeric():
                flat_list.append(c)
    counts = Counter(flat_list)
    max_count = counts.most_common(1)[0][1]
    most_compound_ids = [value for value, count in counts.most_common() if count == max_count]

    compound_names = []
    for most_compound_id in most_compound_ids:
        compount_res = session.query(
            Compounds.compound_name
        ).filter(
            Compounds.compound_id == most_compound_id
        ).first()
        compound_names.append(compount_res[0])

    return compound_names

def import_from_file(file,tbl_name):
    data = pd.read_csv(file)
    try:
        data.columns = data.columns.str.strip()
        sanitize_data(data)
        data.to_sql(tbl_name, engine)
    except ValueError:
        print("Table (",tbl_name,") already exists")

def sanitize_data(dataframe):
    for i in dataframe.columns:
        if dataframe[i].dtype == 'object':
            dataframe[i] = dataframe[i].map(str.strip)
        else:
            pass