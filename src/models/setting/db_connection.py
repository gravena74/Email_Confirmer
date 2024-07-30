import psycopg2

class DbConnectionHandler:
    def __init__(self) -> None:
        self.__database = "notification"
        self.__host = "localhost"
        self.__user = "postgres"
        self.__password = "postgres"
        self.__port = "5432"
    
    def connect(self) -> None:
        conn = psycopg2.connect(dbname=self.__database,
                        host=self.__host,
                        user=self.__user,
                        password=self.__password,
                        port=self.__port)
        
        return conn
    

db_connection_handler = DbConnectionHandler()


