from employee import Employee

class Sale(Employee):
    __departmentName = "ฝ่ายขายสินค้า"
    def __init__(self, name, salary, area):     # เพิ่มเขตพื้นที่รับผิดชอบ
        super().__init__(name, salary, self.__departmentName)
        self.__area = area

    # overwriting เพื่อแสดงในส่วนที่เหมือนกับคลาสแม่
    def _showData(self):
        super()._showData()     # นำข้อมูลของคลาสแม่ มาแสดง
        print("เขตพื้นที่รับผิดชอบ = " + self.__area)

    def __str__(self):
        return (super().__str__()+', พื้นที่รับผิดชอบ = {}'.format(self.__area))

# write by :sarunwit nontasean
# credit : kongraksiam