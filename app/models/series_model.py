from app.models import DatabaseConnector


class Serie(DatabaseConnector):
    serie_columns = [
        "_id",
        "serie",
        "seasons",
        "released_date",
        "genre",
        "imdb_rating"
    ]

    def __init__(self, **kwargs):
        self.serie = kwargs["serie"]
        self.seasons = kwargs["seasons"]
        self.released_date = kwargs["released_date"]
        self.genre = kwargs["genre"]
        self.imdb_rating = kwargs["imdb_rating"]


    @classmethod
    def serialize(cls, data: tuple):
        return dict(zip(cls.serie_columns, data))


    def create_serie(self):
        self.create_table()
        self.get_conn_cur()
        query = """
            INSERT INTO ka_series
                (serie, seasons, released_date, genre, imdb_rating)
            VALUES
                (%s, %s, %s, %s, %s)
            RETURNING *;
        """

        query_values = tuple(self.__dict__.values())


        self.cur.execute(query, query_values)

        self.conn.commit()

        inserted_serie = self.cur.fetchone()

        self.cur.close()
        self.conn.close()

        return inserted_serie


    @classmethod
    def get_series(cls):
        cls.create_table()
        cls.get_conn_cur()

        query = "SELECT * FROM ka_series;"

        cls.cur.execute(query)

        series = cls.cur.fetchall()

        cls.cur.close()
        cls.conn.close()    

        return series

    @classmethod
    def get_serie_by_id(cls, id: int):
        cls.create_table()
        cls.get_conn_cur()

        query = """
            select * from ka_series where id = %s
        """

        cls.cur.execute(query, id)

        serie = cls.cur.fetchall()

        cls.cur.close()
        cls.conn.close()

        return serie

