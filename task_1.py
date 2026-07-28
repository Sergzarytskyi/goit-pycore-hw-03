#_______________________Task_1_____________________

from datetime import datetime


def get_days_from_today(date):
 
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - date).days
    except ValueError:
        return (f"Невірний формат дати: {date}. Введіть дату у форматі 'YYYY-MM-DD'.")
           
get_days_from_today("2026-02-01")