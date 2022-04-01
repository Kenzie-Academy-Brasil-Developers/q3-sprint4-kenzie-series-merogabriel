import psycopg2
import os


configs = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}


class DatabaseConnector:
    @classmethod
    def get_conn_cur(cls):
        cls.conn = psycopg2.connect(**configs)
        cls.cur = cls.conn.cursor()

        
    @classmethod
    def commit_and_close(cls):
        cls.conn.commit()
        cls.cur.close()
        cls.conn.close()

    
    @classmethod
    def create_table(cls):
        cls.get_conn_cur()

        query = """
            create table if not exists ka_series(
                id            BIGSERIAL primary key,
                serie         VARCHAR(100) not null unique,
                seasons       integer not null,
                released_date date not null,
                genre         VARCHAR(50) not null,
                imdb_rating   float not null
            );
        """

        cls.cur.execute(query)
        cls.commit_and_close()

