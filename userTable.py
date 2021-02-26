# Load the postgres module
import psycopg2

# Create a connection object
con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")

# Create a cursor via the connection
cur = con.cursor()

# Query
cur.execute("DROP SCHEMA if exists users CASCADE")
cur.execute("CREATE SCHEMA users")
con.commit()

sql = '''CREATE TABLE users.userdetails(
   first_name VARCHAR(20) NOT NULL,
   last_name VARCHAR(20) NOT NULL,
   address VARCHAR(225),
   city VARCHAR(20),
   country VARCHAR(20),
   state VARCHAR(20),
   zip VARCHAR(20),
   phone1 VARCHAR(20),
   phone2 VARCHAR(20)
)'''
cur.execute('ROLLBACK')
