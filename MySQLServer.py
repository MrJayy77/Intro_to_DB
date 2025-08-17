# MySQLServer.py

import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (update with your credentials)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",            
            password="JayTech@123#" 
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database (safe if it already exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # Close connections properly
        try:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection closed.")
        except NameError:
            # connection or cursor was never created
            pass

if __name__ == "__main__":
    create_database()
