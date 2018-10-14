import pymysql


class DB:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.db = "temperature"
        self.connection = None

    ###########
    # Basic functions
    ###########

    # Open connection to the database
    def connect(self):
        if self.connection is None:
            self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db,
                                              charset="utf8", cursorclass=pymysql.cursors.DictCursor)

    # Close connection to the database
    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    ###########
    # CRU Functions
    ###########

    # Writes a data point to the database
    def write_data_point(self, item, data_point, time_stamp, sensor=1):
        with self.connection.cursor() as cursor:
            sql_write = "INSERT INTO datapoints (dataPoint, timeStamp, item, sensor) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_write, (data_point, time_stamp.strftime('%Y-%m-%d %H:%M:%S'), item, sensor))
            cursor.close()
        self.connection.commit()

    def get_data_points(self, item, start, end):
        with self.connection.cursor() as cursor:
            sql_read = "SELECT dataPoint, timeStamp, item FROM datapoints WHERE timeStamp<%s AND timeStamp>%s and" \
                       " item = %s order by timeStamp "
            cursor.execute(sql_read, (start.strftime('%Y-%m-%d %H:%M:%S'), end.strftime('%Y-%m-%d %H:%M:%S'), item))
            if cursor.rowcount != 0:
                self.disconnect()
                return False
            ret = cursor.fetchall()
            return ret
