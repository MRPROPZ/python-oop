# part 6
# การห่อหุ้ม

# การสร้าง class
try:
    #Encapsulation
    class Employee:


        def __init__(self, name, money, job):    # 1) __init__ เป็น privated
            #public attribute
            self._name = name                    # 1) _name เป็น protected
            self._money = money                # 1) _money เป็น protected
            self._job = job                     # 1) __job เป็น protected

        #protected method
        def _showData(self):
            print('ชื่อขอบคุณ = {}'.format(self._name))               # 2) การเปลี่ยนจาก public เป็น protected
            print('เงินเดือนของคุณ = {:,} บาท'.format(self._money))     # 2) การเปลี่ยนจาก public เป็น protected
            print('อาชีพของคุณคือ = {}'.format(self._job))            # 2) การเปลี่ยนจาก public เป็น protected
            print()


    obj1 = Employee("keng", 100, 'engineer network')
    # obj1.money = 1000000            # 3) สังเกตว่าพยายามเปลี่ยนค่าแต่ ไม่คำตอบไม่เปลี่ยนแปลง แสดงว่าข้อมูลเป็น protected แล้วไม่สามารถแก้ได้
    obj1._money = 1000000
    obj1._job = 'it consaltant'
    print(obj1._showData())
    print()
except AttributeError:
    print('เรียกใช้ method ไม่สำเร็จ กรุณาลองใหม่')
else:
    print('โปรแกรมไม่มีปัญหา')
finally:
    print('จบการทำงาน')

# write by :sarunwit nontasean
# credit : kongraksiam

