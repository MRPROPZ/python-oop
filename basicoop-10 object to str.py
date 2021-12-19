# part 10
# object to string

class Employee:
    # class variable
    __minSalary = 12000
    maxSalary = 50000
    companyName = "บริษัท XYZ จำกัด"

    def __init__(self, name, salary, department):
        # instance variable
        self.__name = name
        self.__salary = salary
        self._department = department

    def _showData(self):
        print("ชื่อพนักงาน = " + self.__name)
        print("เงินเดือน = ", format(self.__salary))
        print("ตำแหน่ง = " + self._department)

    # รายได้ต่อปี
    def _getIncome(self):
        return self.__salary * 12

    def __str__(self):
        return ("ชื่อพนักงาน = {0}, แผนก = {1}, เงินเดือน = {2}, รายได้ต่อปี = {3}".format(self.__name, self._department, self.__salary, self._getIncome()))

class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)


class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)

class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)

account = Accounting("ก้อง", 12000)
print(account.__str__())
print()
programmer = Programmer("โจโจ้", 40000)
print(programmer.__str__())
print()
sale = Sale("นัท", 35000)
print(sale.__str__())
print()

# write by :sarunwit nontasean
# credit : kongraksiam