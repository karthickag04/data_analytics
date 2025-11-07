import mysql.connector
from mysql.connector import Error




def connect_db(host='localhost', database='', user='', password='', port=3306):
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        if connection.is_connected():
            print("Successfully connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None





def execute_query(connection, query, params=None):
    try:
        cursor = connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results
    except Error as e:
        print(f"Error executing query: {e}")
        return None

def execute_update(connection, query, params=None):
    try:
        cursor = connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        connection.commit()
        rowcount = cursor.rowcount
        cursor.close()
        return rowcount
    except Error as e:
        print(f"Error executing update: {e}")
        connection.rollback()
        return 0

def close_db(connection):
    if connection and connection.is_connected():
        connection.close()
        print("MySQL connection closed")

# Example usage
if __name__ == "__main__":
    conn = connect_db(
        host='localhost',
        database='team03',
        user='test01',
        password='Test@123p'
    )
    
    if conn:
        results = execute_query(conn, "SELECT * FROM users LIMIT 5")
        print(results)
        close_db(conn)
