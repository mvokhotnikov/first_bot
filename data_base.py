import win32com.client
import pythoncom
import config


def free_dates(name_sheet):
    pythoncom.CoInitialize()
    excel = win32com.client.Dispatch("Excel.Application")
    wb = excel.Workbooks.Open(config.way_to_list)
    sheet = wb.Worksheets(name_sheet)
    date_list = []
    i = 2
    while len(date_list) < 7 and int(sheet.Cells(i, 4).value) != -1:
        if int(sheet.Cells(i, 4).value) > 0:
            date_list.append(
                (sheet.Cells(i, 1).value, sheet.Cells(i, 2).value, sheet.Cells(i, 3).value, i))
        i += 1
    wb.Save()
    wb.Close()
    excel.Quit()
    return date_list


def register_date(name_sheet, date, user_last_name, user_first_name, d_list):
    pythoncom.CoInitialize()
    excel = win32com.client.Dispatch("Excel.Application")
    wb = excel.Workbooks.Open(config.way_to_list)
    sheet = wb.Worksheets(name_sheet)
    d = 0
    for d in d_list:
        if d[0] == date:
            break
    sheet.Cells(d[3], 2).value = user_last_name
    sheet.Cells(d[3], 3).value = user_first_name
    sheet.Cells(d[3], 4).value = 0
    wb.Save()
    wb.Close()
    excel.Quit()


def finish(user_id):
    config.chat_id.pop(user_id)
