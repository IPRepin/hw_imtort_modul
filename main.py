from application.salary import calculate_salary
from application.db.people import get_employees
import datetime

def main():
    data = datetime.datetime.now()
    print(str(data))
    print()
    calculate_salary()
    get_employees()

if __name__ == '__main__':
    main()
