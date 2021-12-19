# part 5
# การเรียกใช้งาน ฟังก์ชั่นเสริม

# การสร้าง class
class Employee:

    # การสร้าง method

    #1) ทำงานทุกครั้งเมื่อมีการสร้าง object
    def __init__(self, name, display, band):    # <- constructor
        self.name = name                        # <- ค่าที่ส่งมาจะทำให้ผลลัพธ์เปลี่ยนไป
        self.display = display                  # <- ค่าที่ส่งมาจะทำให้ผลลัพธ์เปลี่ยนไป
        self.band = band

    def showData(self):
        print('ชื่อนายก = {}'.format(self.name))
        print('การคาดการณ์ = {}'.format(self.display))
        print('พรรค = {}'.format(self.band))
        print()

#การสร้างวัตถุ ( object )

obj1 = Employee("x", "นายกคนที่ 1", "y")
obj2 = Employee("สุดารัตน์", "นายกคนที่ 2", "ไทยสร้างไทย")
obj3 = Employee("ทักษิณ", "นายกคนที่ 3", "ยังอยู่ต่างประเทศ")

# 1) ใช้งาน isinstance
print(isinstance(obj1,Employee))      # คือ ถ้าถูกสร้างจากคลาส employee จริงหรือเปล่า อธิบาย obj1 เป็นสมาชิกของ Employee ไหม ถ้าเป็น = True , ไม่เป็น = False
print()

# 2) ต่อมาคือ dir
print(dir(obj1))                      # คือ การ list ออกมา ของ method ที่ใช้งาน
print()

# 3) อันสุดท้ายคือ __class__
print(obj1.__class__)                 # คือ การตรวจสอบว่า obj1 สร้างมาจากคลาสชื่ออะไร
print()

# write by :sarunwit nontasean
# credit : kongraksiam

