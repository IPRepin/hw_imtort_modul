from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
from bs_4 import link_downloads

def main():
    data = datetime.datetime.now()
    print(str(data))
    print()
    calculate_salary()
    get_employees()
    print()
    link_downloads()

if __name__ == '__main__':
    main()
