from employee import Employee

class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"
    def __init__(self, name, salary, expereince, skill):   # เพิ่มประสบการณ์ทำงาน และ ทักษะพิเศษ
        super().__init__(name, salary, self.__departmentName)
        self.__exp = expereince
        self.__skill = skill

    # overwriting เพื่อแสดงในส่วนที่เหมือนกับคลาสแม่
    def _showData(self):
        super()._showData()                       # นำข้อมูลของคลาสแม่ มาแสดง
        print("ประสบการ์ณ = " + str(self.__exp))   # แปลงเป็น str ก่อน
        print("ทักษะ = " + self.__skill)

    def __str__(self):
        return (super().__str__() + ', ประสบการณ์ = {} ปี, ทักษะ = {}'.format(self.__exp, self.__skill))

# write by :sarunwit nontasean
# credit : kongraksiam