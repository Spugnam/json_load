#!/usr/bin/python
import psycopg2
import json

with open('./config.json') as f:
    config = json.load(f)  # returns a dictionary

# test copy from table results to csv - works
# note: no headers

file_path =   # file path
f = open(file_path, 'r')

command_tmp = (
        """
        CREATE TEMP TABLE tmp_table
        ON COMMIT DROP
        AS
        SELECT *
        FROM results
        WITH NO DATA;
        """)

command_results = (
        """
        INSERT INTO results
        SELECT *
        FROM tmp_table
        ON CONFLICT DO NOTHING;
        """)

conn = None
try:
    # connect to the PostgreSQL server
    conn = psycopg2.connect(**config)
    print(conn)
    cur = conn.cursor()
    # commands
    cur.execute(command_tmp)
    # cur.copy_from(f, 'results', sep=',')
    cur.copy_from(f, 'tmp_table', sep=',')
    cur.execute(command_results)
    conn.commit()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        print("closing connection")
        conn.close()
        f.close()
