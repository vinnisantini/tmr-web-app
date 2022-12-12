import pandas as pd
import datetime as dt


def import_tmrs():
    imported_tmrs = {}
    # reading excel
    df1 = pd.read_excel('tmr submitted bin.xls')

    # creating a temporary list to store data
    temp_list = [v for v in df1.values]
    temp_list.pop(0)
    temp_list.pop()

    # adding to dictonary for better organization & cleaning up the information
    for index, i in enumerate(temp_list):
        name = i[9]
        num = i[1]
        start_dt = i[3]
        end_dt = i[5]
        pu_location = i[2]
        do_location = i[4]
        support_unit = i[8]
        status = i[10]

        # breaking down date and time into seperate variables
        s_year, s_date, s_time = start_dt[6:10], start_dt[:10], start_dt[11:16]
        e_year, e_date, e_time = end_dt[6:10], end_dt[:10], end_dt[11:16]

        # start date conversion
        a_s, b_s = int(start_dt[6:10]), int(start_dt[:2])
        start_month = dt.datetime(a_s, b_s, 1).strftime("%B")
        s_date = f'{s_date[3:5]} {start_month[:3]} {s_year}'
        # end date conversion
        a_e, b_e = int(end_dt[6:10]), int(end_dt[:2])
        end_month = dt.datetime(a_e, b_e, 1).strftime("%B")
        e_date = f'{e_date[3:5]} {end_month[:3]} {e_year}'

        imported_tmrs[index] = [name, num, '', f'{s_time} {s_date}', pu_location, f'{e_time} {e_date}',
        do_location, support_unit, status, '']

    return imported_tmrs