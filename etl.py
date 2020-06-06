import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    print('Connected to redshift server')
    cur = conn.cursor()
    
    print('Loading the staging tables')
    load_staging_tables(cur, conn)
    
    print('Transforming from staging')
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()