from database.db import get_db_connection
import bcrypt

class UserModel:

    @staticmethod
    def register(name, email, mobile, password):

        conn = get_db_connection()
        cursor = conn.cursor()

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        query = """
        INSERT INTO users (name,email,mobile,password)
        VALUES (%s,%s,%s,%s)
        """

        cursor.execute(query, (name, email, mobile, hashed_password))
        conn.commit()

        cursor.close()
        conn.close()

        return True


    @staticmethod
    def login(email, password):

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM users WHERE email=%s"
        cursor.execute(query,(email,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
                return user

        return None
    

    @staticmethod
    def get_all_users():

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT id,name,email,mobile FROM users ORDER BY id DESC"
        cursor.execute(query)

        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return data