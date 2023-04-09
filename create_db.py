"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import inspect
import sqlite3
from faker import Faker 

def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    
    create_people= """
    CREATE TABLE IF NOT EXISTS people
    (
    ID INTEGERPRIMARY KEY,
    NAME TEXT NOT NULL,
    EMAIL ADDRESS TEXT NOT NULL,
    ADDRESS TEXt TEXT NOT NULL,
    CITY TEXT NOT NULL,
    PROVINCE TEXT NOT NULL,
    BIO TEXT,
    AGE INTEGER,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL,
    );
    """
    cur.execute(create_people)
    con.commit()
    con.close()
    return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    con=sqlite3.connect
    cur=con.cursor(cur)
    fake= Faker()
    populate_people="""
    INSERT INTO PEOPLE
    (
    NAME,
    EMAIL ADDRESS,
    ADDRESS,
    CITY,
    PROVINCE,
    BIO,
    AGE,
    CREATED_AT,
    UPDATED_AT
    )
    VALUES(?,?,?,?,?,?,?,?,?)
    """
    for _ in range(200):
        fake_ones =(
                    fake.NAME(),
                    fake.ADDRESS(),
                    fake.EMAIL ADDRESS(),
                    fake.CITY(),
                    fake.PROVINCE(),
                    fake.BIO(),
                    random.randint(1,100)
                    datetime.now,
                    datetime.now()
        )
    
        cur.execute(fake_ones,populate_people)
        
                 
    
    con.commit()
    con.close()
    return

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()