
class Employee:

    def __init__(self, employee_id, first_name, last_name, birth_day, birth_month, birth_year, position, graduation):

        self.employeeid = employee_id
        self.firstname = first_name
        self.lastname = last_name
        self.birthday = birth_day
        self.birthmonth = birth_month
        self.birthyear = birth_year
        self.employee_position = position
        self.graduation_status = graduation

    def print_employee_data(self):
        print(f"Employee's ID is {self.employeeid}")
        print(f"Employee's First Name is {self.firstname}")
        print(f"Employee's Last Name is {self.lastname}")
        print(f"Employee's Day of Birth is {self.birthday}")
        print(f"Employee's Month of Birth is {self.birthmonth}")
        print(f"Employee's Year of Birth is {self.birthyear}")
        print(f"Employee's Position of Responsibility is {self.employee_position}")
        print(f"Has Employee Graduated From University? {self.graduation_status}")

    def update_employeeid(self, new_employee_id):
        if new_employee_id > 0:
            self.employeeid = new_employee_id
            print(f"Employee's Updated ID is {self.employeeid}")
        else:
            return print("The Updated Employee ID is Invalid")

    def update_firstname(self, new_first_name):
        if len(new_first_name.strip()) >= 2:
            self.firstname = new_first_name
            print(f"Employee's Updated First Name is {self.firstname}")
        else:
            return print("Employee's Updated First Name  is Invalid")

    def update_lastname(self, new_last_name):
        if len(new_last_name.strip()) >= 2:
            self.lastname = new_last_name
            print(f"Employee's Updated Last Name is {self.lastname}")
        else:
            return print("Employee's Updated Last Name  is Invalid")

    def update_birthday(self, new_birth_day):
        if 1 <= new_birth_day <= 31:
            self.birthday = new_birth_day
            print(f"Employee's Updated Day of Birth is {self.birthday}")
        else:
            return print("Employee's Updated Day of Birth is Invalid")

    def update_birthmonth(self, new_birth_month):
        if 1 <= new_birth_month <= 12:
            self.birthmonth = new_birth_month
            print(f"Employee's Updated Month of Birth is {self.birthmonth}")
        else:
            return print("Employee's Updated Month of Birth is Invalid")

    def update_birthyear(self, new_birth_year):
        if 1900 <= new_birth_year <= 2004:
            self.birthyear = new_birth_year
            print(f"Employee's Updated Month of Year is {self.birthyear}")
        else:
            return print("Employee's Updated Year of Birth is Invalid")

    def update_employee_position(self, new_position):
        if len(new_position.strip()) > 0:
            self.employee_position = new_position
            print(f"Employee's Updated Position of Responsibility is {self.employee_position}")
        else:
            return print("Employee's Updated Position of Responsibility is Invalid")

    def update_graduation_status(self, new_graduation):
        if new_graduation == "yes" or "no":
            self.graduation_status = new_graduation
            print(f"Has Employee Graduated From University {self.graduation_status}")
        else:
            return print("Answer must be either 'yes' or 'no'!")

def read_employee_id():
    while True:
        employee_id_str = input("Please Enter Your Employee ID: ")
        if employee_id_str.isdigit():
            employee_id = int(employee_id_str)
            return employee_id
        else:
            print("WARNING: Please Enter a Valid Employee ID")

#First Name
def read_first_name():
    while True:
        first_name = input("Please Enter Your First Name: ")

        if len(first_name.strip()) >= 2:
            return first_name

        else:
            print("WARNING: Your First Name Should Be At Least 2 Characters")



#Last Name
def read_last_name():
    while True:
        last_name = input("Please Enter Your Last Name: ")

        if len(last_name.strip()) >= 2:
            return last_name

        else:
            print("WARNING: Your Last Name Should Be At Least 2 Characters")



#Birthyear
def read_birth_year():
    while True:
        birth_year_str = input("Please Enter Your Year of Birth: ")
        if birth_year_str.isdigit():
            birth_year = int(birth_year_str)
            if (birth_year >= 1900) and (birth_year <= 2004):
                return birth_year
            else:
                print("WARNING: Please Enter a Valid Year of Birth")

        else:
            print("WARNING: Please Enter a Valid Year of Birth")



#Birthmonth
def read_birth_month():
    while True:
        birth_month_str = input("Please Enter Your Month of Birth, as a Number: ")
        if birth_month_str.isdigit():
            birth_month = int(birth_month_str)
            if (birth_month >= 1) and (birth_month <= 12):
                return birth_month
            else:
                print("WARNING: Please Enter a Valid Month of Birth")

        else:
            print("WARNING: Please Enter a Valid Month of Birth")



#Birthday
def read_birth_day():
    while True:
        birth_day_str = input("Please Enter Your Day of Birth: ")
        if birth_day_str.isdigit():
            birth_day = int(birth_day_str)
            if (birth_day >= 1) and (birth_day <= 31):
                return birth_day
            else:
                print("WARNING: Please Enter a Valid Day of Birth")

        else:
            print("WARNING: Please Enter a Valid Day of Birth")



#Postion
def read_position():
    position = input("Please State Your Position in This Company: ")
    if len(position.strip()) > 0:
        return position

    else:
        print("Please Enter a Valid Position of Responsibility")



#Graduated from university?
def read_graduation():
    while True:
        graduation = input("Did You Graduate From a University? (yes/no) ")
        if graduation == "yes":
            return graduation
        elif graduation == "no":
            return graduation
        else:
            print("WARNING: Please Enter Either yes or no")

if __name__ == "__main__":
    employees = {}

    employee_id = read_employee_id()
    first_name = read_first_name()
    last_name = read_last_name()
    birth_day = read_birth_day()
    birth_month = read_birth_month()
    birth_year = read_birth_year()
    position = read_position()
    graduation = read_graduation()

    employee = Employee(employee_id, first_name, last_name, birth_day, birth_month, birth_year, position, graduation)

    print(employee)




"""
    employee1 = Employee(3, "John", "Smith", 2, 8, 1988, "Engineer", "no")

    employee1.print_employee_data()

    employee1.update_employeeid(23)

    employee1.update_firstname("Abishake")

    employee1.update_lastname("Ratnavel")

    employee1.update_birthday(23)

    employee1.update_birthmonth(8)

    employee1.update_birthyear(1998)

    employee1.update_employee_position("Junior DevOps Engineer")

    employee1.update_graduation_status("yes")

    employee1.print_employee_data()


#Employee ID
def read_employee_id():
    while True:
        employee_id_str = input("Please Enter Your Employee ID: ")
        if employee_id_str.isdigit():
            employee_id = int(employee_id_str)
            return employee_id
        else:
            print("WARNING: Please Enter a Valid Employee ID")

#employee_id = read_employee_id()

#First Name
def read_first_name():
    while True:
        first_name = input("Please Enter Your First Name: ")

        if len(first_name.strip()) >= 2:
            return first_name

        else:
            print("WARNING: Your First Name Should Be At Least 2 Characters")

#first_name = read_first_name()

#Last Name
def read_last_name():
    while True:
        last_name = input("Please Enter Your Last Name: ")

        if len(last_name.strip()) >= 2:
            return last_name

        else:
            print("WARNING: Your Last Name Should Be At Least 2 Characters")

#last_name = read_last_name()

#Birthyear
def read_birth_year():
    while True:
        birth_year_str = input("Please Enter Your Year of Birth: ")
        if birth_year_str.isdigit():
            birth_year = int(birth_year_str)
            if (birth_year >= 1900) and (birth_year <= 2004):
                return birth_year
            else:
                print("WARNING: Please Enter a Valid Year of Birth")

        else:
            print("WARNING: Please Enter a Valid Year of Birth")

#birth_year = read_birth_year()

#Birthmonth
def read_birth_month():
    while True:
        birth_month_str = input("Please Enter Your Month of Birth, as a Number: ")
        if birth_month_str.isdigit():
            birth_month = int(birth_month_str)
            if (birth_month >= 1) and (birth_month <= 12):
                return birth_month
            else:
                print("WARNING: Please Enter a Valid Month of Birth")

        else:
            print("WARNING: Please Enter a Valid Month of Birth")

#birth_month = read_birth_month()

#Birthday
def read_birth_day():
    while True:
        birth_day_str = input("Please Enter Your Day of Birth: ")
        if birth_day_str.isdigit():
            birth_day = int(birth_day_str)
            if (birth_day >= 1) and (birth_day <= 31):
                return birth_day
            else:
                print("WARNING: Please Enter a Valid Day of Birth")

        else:
            print("WARNING: Please Enter a Valid Day of Birth")

#birth_day = read_birth_day()

#Postion
def read_position():
    position = input("Please State Your Position in This Company: ")
    if len(position.strip()) > 0:
        return position

    else:
        print("Please Enter a Valid Position of Responsibility")

#position = read_position()

#Graduated from university?
def read_graduation():
    while True:
        graduation = input("Did You Graduate From a University? (yes/no) ")
        if graduation == "yes":
            return graduation
        elif graduation == "no":
            return graduation
        else:
            print("WARNING: Please Enter Either yes or no")

#graduation = read_graduation()

def add_employee():
    first_name = read_first_name()
    last_name = read_last_name()
    birth_day = read_birth_day()
    birth_month = read_birth_month()
    birth_year = read_birth_year()
    position = read_position()
    graduation = read_graduation()
    employee = {"Employee First Name" : first_name,
                "Employee Last Name" : last_name,
                "Birth Day" : birth_day,
                "Birth Month" : birth_month,
                "Birth Year" : birth_year,
                "Position of Responsibility" : position,
                "Graduated?" : graduation}

    return employee

def read_remove_employee_id():
    while True:
        remove_id_str = input("Which Employee ID Would You Like to Remove From the System? ")
        if remove_id_str.isdigit():
            remove_id = int(remove_id_str)
            return remove_id
        else:
            print("WARNING: Enter a Valid Employee ID")

def read_view_employee_id():
    while True:
        view_id_str = input("Which Employee ID Would You Like to View From the System? ")
        if view_id_str.isdigit():
            view_id = int(view_id_str)
            return view_id
        else:
            print("WARNING: Enter a Valid Employee ID")

def read_modify_employee_id():
    while True:
        modify_id_str = input("Which Employee ID Would You Like to Modify From the System? ")
        if modify_id_str.isdigit():
            modify_id = int(modify_id_str)
            return modify_id
        else:
            print("WARNING: Enter a Valid Employee ID")

"""
