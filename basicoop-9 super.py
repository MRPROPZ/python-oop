# part 9
# super

# Super
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
        super()._showData() #เรียกใช้ method ของคลาสแม่

account = Accounting("ก้อง", 12000)
account._showData()         # เรียกใช้ method ของคลาสแม่
print()
programmer = Programmer("โจโจ้", 40000)
programmer._showData()      # เรียกใช้ method ของคลาสแม่
print()
sale = Sale("นัท", 35000)
print()

# write by :sarunwit nontasean
# credit : kongraksiam