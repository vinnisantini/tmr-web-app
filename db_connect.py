import mysql.connector
import little_tracker as lt


def connect_to_db():
    my_db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'rootpass',
        database = 'tmr_tracker_DB'
    )
    cursor = my_db.cursor()

    print('\nConnected made...\n')
    return my_db, cursor


def importing_tmrs():
    penis = lt.import_tmrs()
    return penis


def inserting_into_db(my_db, cursor, penis):
    cursor.execute('SELECT num FROM tmrs')
    result = cursor.fetchall()

    num_list = [x[0] for x in result]

    for ind, tmr in penis.items():
        name = tmr[0]
        num = tmr[1]
        pu = tmr[3]
        sd = tmr[4]
        do = tmr[6]
        ed = tmr[5]
        unit = tmr[7]
        status = tmr[8]

        if num in num_list:
            print(f'suck my dick {num} is in the database already!!!\n')
        else:
            print(f'{num} not in database, inserting my cok!!\n')
            sql = 'INSERT INTO tmrs (account_id, name, num, pickup, sd, dropoff, ed, unit, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            val = (1, name, num, pu, sd, do, ed, unit, status)

            cursor.execute(sql, val)
            my_db.commit()

    print(cursor.rowcount, "penises, nice and massive dude!")


def print_db(cursor):
    # grabing all the items
    cursor.execute('SELECT * FROM tmrs')
    result_all = cursor.fetchall()

    for x in result_all:
        print(f'{x[1:]}\n')


def delete_item(my_db, cursor, tmr_num):
    # deleting items
    sql = f"DELETE FROM tmrs WHERE num = '{tmr_num}'"
    cursor.execute(sql)

    my_db.commit()
    print('\ndeleted... 8===D\n')


def update_item(my_db, cursor, tmr_num):
    # updating items
    sql = f"UPDATE tmrs SET name = 'Massive Cock' WHERE num = '{tmr_num}'"
    cursor.execute(sql)
    my_db.commit()
    print(f'\nedited {tmr_num}\n')


while True:
    user_input = input("Enter the following\n'C' to connect to database\n'I' to inport tmrs\n'P' to print all tmrs in database\n'D' to delete a tmr\n'U' to update a tmr\n'E' to exit: ").upper()

    if user_input == 'C':
        db, cur = connect_to_db()
    elif user_input == 'I':
        tmrs = importing_tmrs()
        inserting_into_db(db, cur, tmrs)
    elif user_input == 'P':
        print(f'\n{print_db(cur)}\n')
    elif user_input == 'D':
        delete_item(db, cur, 'T210811-0164')
    elif user_input == 'U':
        update_item(db, cur, 'T210811-0164')
    elif user_input == 'E':
        print('exiting program little cok')
        break