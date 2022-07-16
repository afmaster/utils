import sqlite3
from prettytable import from_db_cursor

# Ajust dict to be used in sqlite functions

def ajust_to_sql(par):
    str_par = str(par)
    parsed_par = str_par.replace("'", '"')
    return parsed_par

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


# RETRIEVE ALL THE LINES CONTAINING A CRITERIA INSIDE A COLUMN

def search_entire_db(db_file: str, db: str, field: str, criteria: str) -> list or None:
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    try:
        c.execute(f"SELECT * FROM {db} WHERE {field} LIKE '%{criteria}%'")
        results = c.fetchall()
        #item = results[0]
        c.close()
        conn.close()
        return results
    except:
        c.close()
        conn.close()
        return None


# FETCH AN ENTIRE TABLE

def fetch_entire_table(db_file: str, db: str) -> str or None:
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    try:
        c.execute(f'SELECT * FROM {db}')
        output = c.fetchall()
        c.close()
        conn.close()
        return output
    except:
        c.close()
        conn.close()
        return None

    
# FETCH ENTIRE TABLE ORDER BY column

def fetch_ordered_table(db_file: str, db: str, field: str) -> str or None:
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    try:
        c.execute(f'SELECT * FROM {db} ORDER BY {field} ASC')
        output = c.fetchall()
        c.close()
        conn.close()
        return output
    except:
        c.close()
        conn.close()
        return None
    
# return an entire row
    
def search_row(db_file: str, db: str, field: str, criteria: str) -> str or None:
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    try:
        table = list(c.execute(f"SELECT * FROM {db}").description)
        c.execute(f"SELECT * FROM {db}")
        results = c.fetchall()
        for col in table:
            if col[0] == field:
                i = table.index(col)
                for row in results:
                    if row[i] == criteria:
                        return row
                    else:
                        continue
            else:
                continue
        return None
    except:
        c.close()
        conn.close()
        return None
    

# Return an entire row with two criteria

def search_row_with_two_criteria(db_file: str, db: str, field1: str, criteria1: str, field2: str, criteria2: str) -> str or None:
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    try:
        table = list(c.execute(f"SELECT * FROM {db}").description)

        c.execute(f"SELECT * FROM {db}")
        results = c.fetchall()
        table_criteria_1 = []
        for col in table:
            if col[0] == field1:
                i = table.index(col)
                for row in results:
                    if row[i] == criteria1:
                        table_criteria_1.append(row)
                    else:
                        continue
            else:
                continue

        for col in table:
            if col[0] == field2:
                i = table.index(col)
                for item in table_criteria_1:
                    if item[i] == criteria2:
                        return item
                    else:
                        continue
            else:
                continue
        return None
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


# Delete entry with one criteria

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

    
# Delete one entry with two criteria

def delete_entry_with_two_criteria(db_file: str, db: str, field1: str, criteria1: str, field2: str, criteria2: str) -> None:
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    try:
        # c.execute(f"SELECT * FROM destination WHERE id='{chat_id}'")
        # results = cur.fetchone()
        c.execute(f"DELETE from {db} where {field1}= ? AND {field2}= ?", (criteria1, criteria2))
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

    
# DELETE ENTIRE TALBE
def delete_table(db_file: str, db: str) -> None:
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    try:
        c.execute(f"DROP TABLE IF EXISTS {db}")
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


# CREATE DB AND/OR ADD ROW IN A TABLE WITH ID

def create_db_with_id(db_file: str, db: str, id_name: str, dic: dict) -> None:
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # define columns
    columns_length = len(list(dic.items()))

    # Creating string for sql command for creating bd
    part_1_create_table_sql = f"CREATE TABLE IF NOT EXISTS {db} ({id_name} INTEGER PRIMARY KEY AUTOINCREMENT,"
    for r in range(0, columns_length):
        part_1_create_table_sql = part_1_create_table_sql + str(list(dic.keys())[r]) + " TEXT"
        if r < (columns_length - 1):
            part_1_create_table_sql = part_1_create_table_sql + ", "

    create_table_sql = part_1_create_table_sql + ");"

    # criar BD
    c.execute(create_table_sql)

    # Inserir linha
    keys = str(tuple(dic.keys())).replace("'", "")
    sqlite_insert_row = f"INSERT INTO {db}{keys} VALUES ("
    for r in range(0, columns_length):
        sqlite_insert_row = sqlite_insert_row + "?"
        if r < (columns_length - 1):
            sqlite_insert_row = sqlite_insert_row + ", "
    sqlite_insert_row = sqlite_insert_row + ")"
    print(sqlite_insert_row)


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

        
# Change an entire row

def change_row(db_file: str, db: str, field: str, criteria: str, dic: dict) -> None:
    try:
        delete_entry(db_file, db, field, criteria)
    except:
        pass
    add_entry(db_file, db, dic)


# change an entire row based on two criteria

def change_row_with_two_criteria(db_file: str, db: str, field1: str, criteria1: str, field2: str, criteria2: str, dic: dict) -> None:
    try:
        delete_entry_with_two_criteria(db_file, db, field1, criteria1, field2, criteria2)
    except:
        pass
    add_entry(db_file, db, dic)

    
# CHANGE ROW BASED ON ID

def change_row_with_id(db_file: str, db: str, id_field: str, id_num: int, dic: dict) -> None:
    try:
        delete_entry(db_file, db, id_field, id_num)
    except:
        pass
    create_db_with_id(db_file, db, id_field, dic)
    
    
# UPDATE VALUE OF A CELL

def update_cell(db_file: str, db: str, field: str, criteria: str, column_name: str, new_value: str) -> None:
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        sql_query = f"Update {db} {column_name} = {new_value} where {field} = {criteria}"
        c.execute(sql_query)
        conn.commit()
        c.close()
    except sqlite3.Error as err:
        print("Error in sqlite: ", err)
    finally:
        if conn:
            conn.close()

            
# VISUALIZE DATA BASE AS PREATTY TABLE

def visualize_db(db_file: str, db: str) -> str:
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {db}")
    mytable = from_db_cursor(cursor)
    mystring = mytable.get_string()
    print(mystring)
    return mystring
