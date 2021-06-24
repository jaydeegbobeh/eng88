from mysql.connector import connect, Error


try:
  with connect(host="localhost", user="root", password="my_secret_password", database="common_pw") as connection:
    print(connection)      
    with connection.cursor() as cursor:
      with open('10000_common_pw.txt', 'r') as file:
        for line in file:
          command= f"INSERT INTO `common_pw_final_table`  (`id`, `password`) VALUES (NULL, '{line}');"
          cursor.execute(command)
          connection.commit()
      for item in cursor:
        print(item)

except Error as e:
  print(e)
