# part 4
# การกำหนด method -> constructor & destructor
# การแก้ไขข้อมูล

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

    def __del__(self):                          # <- destructor
        print('Call Destrcutor')

#การสร้างวัตถุ ( object )

# 2) สร้างวัตถุชิ้นที่ 1 (object 1) >> constructor ทำงาน
obj1 = Employee("x", "นายกคนที่ 1", "y")
obj1.name = "ธนาธร"                             # <- การแก้ไขไฟล์ที่ส่งให้ method ธนาธร มา แทน x
obj1.band = "อนาคตใหม่"                         # <- การแก้ไขไฟล์ที่ส่งให้ method อนาคตใหม่มาแทน y
# การแสดงข้อมูลวัตถุที่ 1
obj1.showData()

# 2) สร้างวัตถุชิ้นที่ 2 (object 2) >> constructor ทำงาน
obj2 = Employee("สุดารัตน์", "นายกคนที่ 2", "ไทยสร้างไทย")
# การแสดงข้อมูลวัตถุที่ 2
obj2.showData()

# 2) สร้างวัตถุชิ้นที่ 3 (object 3) >> constructor ทำงาน
obj3 = Employee("ทักษิณ", "นายกคนที่ 3", "ยังอยู่ต่างประเทศ")
# การแสดงข้อมูลวัตถุที่ 3
obj3.showData()

# write by :sarunwit nontasean
# credit : kongraksiam

