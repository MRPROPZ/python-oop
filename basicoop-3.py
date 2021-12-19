# part 3
# ทำการสร้างวัตถุเพิ่มขึ้น การกำหนด attributeเพิ่มเติม
# การสร้าง methods สำหรับแสดงผลแยก และ การกำหนดค่าใหม่ด้วย

# การสร้าง class
class Employee:

    # การสร้าง method

    def detail(self, name, display, band):       # <- การกำหนด attribute ชื่อ band(พรรค) เพิ่ม
        self.name = name                         # <- ค่าที่ส่งมาจะทำให้ผลลัพธ์เปลี่ยนไป
        self.display = display                   # <- ค่าที่ส่งมาจะทำให้ผลลัพธ์เปลี่ยนไป
        self.band = band

    def showData(self):
        print('ชื่อนายก = {}'.format(self.name))
        print('การคาดการณ์ = {}'.format(self.display))
        print('พรรค = {}'.format(self.band))
        print()

# การสร้างวัตถุ ( object )

# การสร้างวัตถุ ชิ้นที่ 1 (object 1)
obj1 = Employee()
obj1.detail("ธนาธร", "นายกคนที่ 1", "อนาคตใหม่")
# การแสดงข้อมูลวัตถุที่ 1
obj1.showData()

# การสร้างวัตถุ ชิ้นที่ 2 (object 2)
obj2 = Employee()
obj2.detail("สุดารัตน์", "นายกคนที่ 2", "ไทยสร้างไทย")
# การแสดงข้อมูลวัตถุที่ 2
obj2.showData()

# การสร้างวัตถุ ชิ้นที่ 3 (object 3)
obj3 = Employee()
obj3.detail("ทักษิณ", "นายกคนที่ 3", "ยังอยู่ต่างประเทศ")
# การแสดงข้อมูลวัตถุที่ 3
obj3.showData()

# write by :sarunwit nontasean
# credit : kongraksiam

