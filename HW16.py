# Создать классы Employee (сотрудник) и Company (компания).
# Классы должны содержать:
# минимум два поля экземпляров и одно поле класса
# минимум два метода экземпляра
# минимум один метод класса
# минимум один статический метод
# Методы должные быть НЕ get/set поле, а что-то оригинальнее:) (но если надо их, тоже можно добавить)
# Написать код который создает несколько экземпляров и взаимодействует с объектами
# Задание в том числе и на фантазию


class Employee:
    empAmount = 0

    'Constructor'
    def __init__(self, name, years, specialty, salary, ):
        self.name = name
        self.years = years
        self.specialty = specialty
        self.salary = salary
        Employee.empAmount += 1

    'The method shows the employee`s salary'
    def show_emp_salary(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    'The method shows the employee`s specialty'
    def show_emp_specialty(self):
        print("Name : ", self.name, ", Specialty: ", self.specialty)

    'The method shows the employee`s overtime bonus'
    def show_overtime_bonus(self):
        print("Bonus amount for overtime: ", self.overtime_bonus)

    'The class method sets the overtime bonus'
    @classmethod
    def overtime_bonus(cls, overtime_bonus):
        cls.overtime_bonus = overtime_bonus

    'The method shows the number of all employees'
    @staticmethod
    def show_emp_amount():
        print("Total Employee %d" % Employee.empAmount)

    'The method shows the assigned tasks by specialties'
    @staticmethod
    def assigned_task(specialty):
        print('Your assigned tasks:')
        if specialty == 'Dev':
            requirement = ['dev_task_1', 'dev_task_2', 'dev_task_3']
        elif specialty == 'QA':
            requirement = ['qa_task_1', 'qa_task_2']
        elif specialty == 'BA':
            requirement = ['ba_task_1', 'ba_task_3']
        else:
            requirement = ['other_task_1']
        return requirement


emp_Alex = Employee("Alex", 31, "Dev", 5000)
emp_Alex.show_emp_amount()
emp_Alex.show_emp_salary()
emp_Alex.show_emp_specialty()
print(emp_Alex.assigned_task("Dev"))
Employee.overtime_bonus(500)
Employee.show_emp_amount()
emp_Alex.show_overtime_bonus()


class Company:
    all_revenue = 0

    'Constructor'

    def __init__(self,company_name, dep_name, emp_number, profit, expenses ):
        self.company_name = company_name
        self.dep_name = dep_name
        self.emp_number = emp_number
        self.profit = profit
        self.expenses = expenses
        Company.all_revenue += profit

    'The method shows the company name'
    def show_company_name(self):
            print("Company name : ", self.company_name)

    'The method shows the department profit'
    def show_dep_profit(self):
        print("Department name : ", self.dep_name, ", Profit: ", self.profit)

    'The method shows the department expenses'
    def show_dep_expenses(self):
        print("Department name : ", self.dep_name, ", Expenses: ", self.expenses)

    'The method shows the general annual department bonus'
    def show_annual_dep_bonus(self):
        print("General annual department bonus: ", self.annual_dep_bonus)

    'The class method sets the annual department bonus'
    @classmethod
    def set_annual_dep_bonus(cls, profit):
        if profit < 100000:
            cls.annual_dep_bonus = 5000
        elif profit > 100000:
            cls.annual_dep_bonus = 15000
        elif profit > 500000:
            cls.annual_dep_bonus = 30000

    'The method shows the all companies revenue'
    @staticmethod
    def show_all_companies_revenue():
        print("Total Companies revenue %d" % Company.all_revenue)

    'The method shows the current client by departments'
    @staticmethod
    def current_clients(dep_name):
        print('Your current clients:')
        if dep_name == 'Logistic':
            clients = ['Nexxiot', 'ZIM', 'Transporeon']
        elif dep_name == 'HealthCare':
            clients = ['AstraZeneca', 'Pfizer']
        elif dep_name == 'Finance':
            clients = ['Revolut', 'Monobank']
        return clients


my_company = Company("FTX", "Finance", 100 , 500000,10000)
my_company2 = Company("Binance", "Finance", 1000 , 2500000,20000)
my_company.show_company_name()
my_company.show_dep_profit()
my_company.show_dep_expenses()
print(my_company.current_clients("Finance"))
Company.set_annual_dep_bonus(500000)
my_company.show_annual_dep_bonus()
Company.show_all_companies_revenue()
