from database.db import get_db_connection

class SOSModel:

    @staticmethod
    def send_sos(user_id,latitude,longitude):

        conn=get_db_connection()
        cursor=conn.cursor()

        query="""
        INSERT INTO sos_alerts(user_id,latitude,longitude,status)
        VALUES(%s,%s,%s,'active')
        """

        cursor.execute(query,(user_id,latitude,longitude))
        conn.commit()

        sos_id = cursor.lastrowid

        sos_id = cursor.lastrowid

        # 🔥 INSERT FIRST LOCATION
        query2 = """
        INSERT INTO location_tracking(sos_id,latitude,longitude)
        VALUES(%s,%s,%s)
        """
        cursor.execute(query2,(sos_id,latitude,longitude))
        conn.commit()

        cursor.close()
        conn.close()

        return sos_id


    @staticmethod
    def update_location(sos_id,latitude,longitude):

        conn=get_db_connection()
        cursor=conn.cursor()

        query="""
        INSERT INTO location_tracking(sos_id,latitude,longitude)
        VALUES(%s,%s,%s)
        """

        cursor.execute(query,(sos_id,latitude,longitude))
        conn.commit()

        

        cursor.close()
        conn.close()

        return True


    @staticmethod
    def stop_sos(sos_id):

        conn=get_db_connection()
        cursor=conn.cursor()

        query="""
        UPDATE sos_alerts
        SET status='closed'
        WHERE id=%s
        """

        cursor.execute(query,(sos_id,))
        conn.commit()

        cursor.close()
        conn.close()

        return True


    @staticmethod
    def get_active_sos():

        conn=get_db_connection()
        cursor=conn.cursor(dictionary=True)

        query="""
        SELECT s.*,u.name,u.mobile
        FROM sos_alerts s
        JOIN users u ON s.user_id=u.id
        WHERE status='active'
        """

        cursor.execute(query)
        sos=cursor.fetchall()

        cursor.close()
        conn.close()

        return sos
    

    @staticmethod
    def get_tracking(sos_id):

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT latitude, longitude
        FROM location_tracking
        WHERE sos_id=%s
        ORDER BY recorded_at ASC
        """

        cursor.execute(query,(sos_id,))
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data
    
    @staticmethod
    def get_user_sos(user_id):

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT * FROM sos_alerts
        WHERE user_id=%s
        ORDER BY id DESC
        """

        cursor.execute(query,(user_id,))
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data
    

    @staticmethod
    def pause_sos(sos_id):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("UPDATE sos_alerts SET status='paused' WHERE id=%s",(sos_id,))
        conn.commit()

        cursor.close()
        conn.close()


    @staticmethod
    def resume_sos(sos_id):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("UPDATE sos_alerts SET status='active' WHERE id=%s",(sos_id,))
        conn.commit()

        cursor.close()
        conn.close()