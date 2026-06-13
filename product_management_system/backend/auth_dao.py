def login_user(connection, username, password):
    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT * FROM users
    WHERE username = %s AND password = %s
    """

    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    cursor.close()

    return user