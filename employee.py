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

    # หาโบนัส
    def _getIncome(self, bonus=0, overtime=0):      # ถ้าไม่ได้กำหนดโบนัสเป็น 0
        return (self.__salary * 12) + bonus + overtime

    def __str__(self):
        return ("ชื่อพนักงาน = {0}, แผนก = {1}, เงินเดือน = {2}".format(self.__name, self._department, self.__salary, ))

# write by :sarunwit nontasean
# credit : kongraksiam