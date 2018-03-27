import pymysql.cursors

connection = pymysql.connect(host='be-dev.internal.timipc.com', user='root', password='qpJ-hr9-R6U-YLZ', db='ucenter',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = 'select * from uc_admin_menu'
        cursor.execute(sql)
        result = cursor.fetchall()
        for line in result:
            print(line)

    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

finally:
    connection.close()
