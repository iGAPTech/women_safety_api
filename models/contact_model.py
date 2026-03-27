from database.db import get_db_connection

class ContactModel:

    @staticmethod
    def add_contact(user_id,name,mobile,relation):

        conn=get_db_connection()
        cursor=conn.cursor()

        query="""
        INSERT INTO emergency_contacts(user_id,contact_name,contact_mobile,relation)
        VALUES(%s,%s,%s,%s)
        """

        cursor.execute(query,(user_id,name,mobile,relation))
        conn.commit()

        cursor.close()
        conn.close()

        return True


    @staticmethod
    def get_contacts(user_id):

        conn=get_db_connection()
        cursor=conn.cursor(dictionary=True)

        query="SELECT * FROM emergency_contacts WHERE user_id=%s"
        cursor.execute(query,(user_id,))
        contacts=cursor.fetchall()

        cursor.close()
        conn.close()

        return contacts


    @staticmethod
    def delete_contact(contact_id):

        conn=get_db_connection()
        cursor=conn.cursor()

        query="DELETE FROM emergency_contacts WHERE id=%s"
        cursor.execute(query,(contact_id,))

        conn.commit()

        cursor.close()
        conn.close()

        return True
    

    @staticmethod
    def update_contact(contact_id,name,mobile,relation):

        conn=get_db_connection()
        cursor=conn.cursor()

        query="""
        UPDATE emergency_contacts
        SET contact_name=%s,
            contact_mobile=%s,
            relation=%s
        WHERE id=%s
        """

        cursor.execute(query,(name,mobile,relation,contact_id))
        conn.commit()

        cursor.close()
        conn.close()

        return True