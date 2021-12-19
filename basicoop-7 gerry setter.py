# part 7
# Getter & Setter Method

# การสร้าง class
try:
    class Employee:

        # การสร้าง method
        def __init__(self, name, money, job):    #  __init__ เป็น privated
            self.__name = name                    # _name เป็น privated
            self.__money = money                  # _money เป็น privated
            self.__job = job                     # __job เป็น private
            #self._showData()                    # เฉพาะคลาสแม่ที่แสดงค่าได้


        def _showData(self):
            print('ชื่อขอบคุณ = {}'.format(self.getName()))               # การเปลี่ยนจาก public เป็น protected
            print('เงินเดือนของคุณ = {:,} บาท'.format(self.getMoney()))    # การเปลี่ยนจาก public เป็น protected
            print('อาชีพของคุณคือ = {}'.format(self.getJob()))          # การเปลี่ยนจาก public เป็น private
            print()

        # 1) getter method การกำหนดค่าผ่าน method
        def setName(self, newname):
            self.__name = newname

        def setMoney(self, newmoney):
            self.__money = newmoney

        def setJob(self, newjob):
            self.__job = newjob

        # 2) getter method การนำค่าไปใช้งานผ่าน method
        def getName(self):
            return self.__name

        def getJob(self):
            return self.__job

        def getMoney(self):
            return self.__money
    #การสร้างวัตถุ ( object )

    obj1 = Employee("name", 0, 'no job')
    obj1.setName('John')                                 # การเปลี่ยนค่า name ผ่าน method
    obj1._showData()

except AttributeError:
    print('เรียกใช้ method ไม่สำเร็จ กรุณาลองใหม่')
else:
    print('โปรแกรมไม่มีปัญหา')
finally:
    print('จบการทำงาน')

# write by :sarunwit nontasean
# credit : kongraksiam


