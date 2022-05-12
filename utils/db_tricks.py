import sqlite3

def search_db(db_file: str, db: str, field: str, criteria: str) -> str or None:
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    try:
        c.execute(f"SELECT destination FROM {db} WHERE {field}='{criteria}'")
        results = c.fetchone()
        item = results[0]
        c.close()
        conn.close()
        return item
    except:
        c.close()
        conn.close()
        return None


def fetch_all(db_file: str, db: str, field: str) -> str or None:
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    try:
        c.execute(f'SELECT {field} FROM {db}')
        itens = c.fetchall()
        c.close()
        conn.close()
        return itens
    except:
        c.close()
        conn.close()
        return None


def delete_entry(db_file: str, db: str, field: str, criteria: str) -> None:
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    try:
        # c.execute(f"SELECT * FROM destination WHERE id='{chat_id}'")
        # results = cur.fetchone()
        c.execute(f"DELETE from {db} where {field}= ?", (criteria,))
    except:
        pass
    conn.commit()
    c.close()
    conn.close()


def delete_all_rows(db_file: str, db: str) -> None:
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    try:
        c.execute(f"DELETE from {db}")
    except:
        pass
    conn.commit()
    c.close()
    conn.close()


def create_db(db_file: str, db: str,  dic: dict) -> None:
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    #define columns
    columns_length = len(list(dic.items()))

    #Creating string for sql command for creating bd
    part_1_create_table_sql = f"CREATE TABLE IF NOT EXISTS {db} ("
    for r in range(0, columns_length):
        part_1_create_table_sql = part_1_create_table_sql + str(list(dic.keys())[r]) + " TEXT"
        if r < (columns_length - 1):
            part_1_create_table_sql = part_1_create_table_sql + ", "

    create_table_sql = part_1_create_table_sql + ");"

    # criar BD
    c.execute(create_table_sql)

    # Inserir linha

    sqlite_insert_row = f"INSERT INTO {db} VALUES ("
    for r in range(0, columns_length):
        sqlite_insert_row = sqlite_insert_row + "?"
        if r < (columns_length - 1):
            sqlite_insert_row = sqlite_insert_row + ", "
    sqlite_insert_row = sqlite_insert_row + ")"

    params = tuple(dic.values())
    c.execute(sqlite_insert_row, params)
    conn.commit()
    c.close()
    conn.close()


def update_db(db_file: str, db: str, field: str, criteria: str, dic: dict) -> None:
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    try:
        # c.execute(f"SELECT * FROM destination WHERE id='{chat_id}'")
        # results = cur.fetchone()
        c.execute(f"DELETE from {db} where {field}= ?", (criteria,))
        conn.commit()
    except:
        pass

    #define columns
    columns_length = len(list(dic.items()))

    #Creating string for sql command for creating bd
    part_1_create_table_sql = f"CREATE TABLE IF NOT EXISTS {db} ("
    for r in range(0, columns_length):
        part_1_create_table_sql = part_1_create_table_sql + str(list(dic.keys())[r]) + " TEXT"
        if r < (columns_length - 1):
            part_1_create_table_sql = part_1_create_table_sql + ", "

    create_table_sql = part_1_create_table_sql + ");"

    # criar BD
    c.execute(create_table_sql)

    # Inserir linha

    sqlite_insert_row = f"INSERT INTO {db} VALUES ("
    for r in range(0, columns_length):
        sqlite_insert_row = sqlite_insert_row + "?"
        if r < (columns_length - 1):
            sqlite_insert_row = sqlite_insert_row + ", "
    sqlite_insert_row = sqlite_insert_row + ")"

    params = tuple(dic.values())
    c.execute(sqlite_insert_row, params)
    conn.commit()
    c.close()
    conn.close()

# The 'dic' variable is a dictionary with title of the column and the variable to be stored


def add_entry(db_file: str, db: str, dic: dict) -> None:
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    #define columns
    columns_length = len(list(dic.items()))

    #Creating string for sql command for creating bd
    part_1_create_table_sql = f"CREATE TABLE IF NOT EXISTS {db} ("
    for r in range(0, columns_length):
        part_1_create_table_sql = part_1_create_table_sql + str(list(dic.keys())[r]) + " TEXT"
        if r < (columns_length - 1):
            part_1_create_table_sql = part_1_create_table_sql + ", "

    create_table_sql = part_1_create_table_sql + ");"
    print('command: ', create_table_sql)
    # criar BD
    c.execute(create_table_sql)

    # Inserir linha

    sqlite_insert_row = f"INSERT INTO {db} VALUES ("
    for r in range(0, columns_length):
        sqlite_insert_row = sqlite_insert_row + "?"
        if r < (columns_length - 1):
            sqlite_insert_row = sqlite_insert_row + ", "
    sqlite_insert_row = sqlite_insert_row + ")"

    params = tuple(dic.values())
    print(params)
    c.execute(sqlite_insert_row, params)
    conn.commit()
    c.close()
    conn.close()
