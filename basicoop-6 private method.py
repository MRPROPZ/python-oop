# part 6
# การห่อหุ้ม

# การสร้าง class
try:
    #Encapsulation
    class Employee:

        def __init__(self, name, money, job):    # 1) __init__ เป็น privated
            #public attribute
            self._name = name                    # 1) _name เป็น privated
            self.__money = money                # 1) _money เป็น privated
            self.__job = job                     # 1) __job เป็น private
            self.__showData()                   # <-- การรันข้อความได้เฉพาะ class แม่เท่านั้น

        #public method
        def __showData(self):
            print('ชื่อขอบคุณ = {}'.format(self._name))               # 2) การเปลี่ยนจาก public เป็น protected
            print('เงินเดือนของคุณ = {:,} บาท'.format(self.__money))     # 2) การเปลี่ยนจาก public เป็น protected
            print('อาชีพของคุณคือ = {}'.format(self.__job))            # 2) การเปลี่ยนจาก public เป็น private
            print()


    obj1 = Employee("keng", 100, 'engineer network')
    obj1.__money = 1000000           # 3) ไม่สามารถแก้ไขได้เลยเพราะเป็น private
    obj1.__job = 'it consaltant'    # 3) ตำแหน่งงานไม่สามารถขอสิทธิ์แก้ได้เลย เพราะเป็น private
    #obj1.__showData()                 # 3) บรรทัดนี้ สังเกตจะ error เพราะหาไม่เจอ เราทำการเปลี่ยน method showdata เป็น private

except AttributeError:
    print('เรียกใช้ method ไม่สำเร็จ กรุณาลองใหม่')
else:
    print('โปรแกรมไม่มีปัญหา')
finally:
    print('จบการทำงาน')

# write by :sarunwit nontasean
# credit : kongraksiam

