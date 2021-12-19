# part 2
# ต้องการการสร้าง Attribute
# เพื่อเก็บค่า ชื่อพนักงาน และ เงินเดือน

# 1) การสร้าง class
class Employee:
    # 3) การสร้าง method
    def detail(self):
        self.name = 'Tranatorn'
        self.display = 'นายกคนถัดไป'
        print('ชื่อนายก = {}'.format(self.name)) # การเปลี่ยน {} -> self.name
        print('การคาดการณ์ = {}'.format(self.display)) # การเปลี่ยน {} -> self.display

# 2) การสร้างวัตถุ( object )
emp1 = Employee()

# 4)การเรียกใช้งาน method detail
emp1.detail()

# write by :sarunwit nontasean
# credit : kongraksiam
