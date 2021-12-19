# part 6
# การห่อหุ้ม

# การสร้าง class
try:
    #Encapsulation
    class Employee:


        def __init__(self, name, money, job):    # 1) __init__ เป็น privated
            #public attribute
            self.name = name                    # 1) _name เป็น privated
            self.money = money                # 1) _money เป็น privated
            self.job = job                     # 1) __job เป็น private

        #public method ทุกคนสามารถแก้ไขได้
        def showData(self):
            print('ชื่อขอบคุณ = {}'.format(self.name))
            print('เงินเดือนของคุณ = {:,} บาท'.format(self.money))
            print('อาชีพของคุณคือ = {}'.format(self.job))
            print()


    obj1 = Employee("keng", 100, 'engineer network')
    obj1.money = 1000000
    obj1.job = 'it consaltant'
    obj1.showData()
except AttributeError:
    print('เรียกใช้ method ไม่สำเร็จ กรุณาลองใหม่')
else:
    print('โปรแกรมไม่มีปัญหา')
finally:
    print('จบการทำงาน')

# write by :sarunwit nontasean
# credit : kongraksiam

