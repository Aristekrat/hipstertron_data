import psycopg2

conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='412909AB'")

cur = conn.cursor()

cur.execute('''INSERT INTO first (name) VALUES('Cheese')''')

cur.close()

conn.commit()

conn.close()