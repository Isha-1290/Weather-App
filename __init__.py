from API.utils.DBConnection import DBConnection

try:
    dbconnection=DBConnection()
    print(f"Connection successful:{dbconnection.get_client()}")
except Exception as e:
    print(f"Connection failed:{e}")    