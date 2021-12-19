from accounting import Accounting
from programmer import Programmer
from sale import Sale

account = Accounting("ก้อง", 10000, 30)     # 1) เพิ่มอายุ
print(account.__str__())
print("บัญชี รายได้ต่อปี = {0:,}".format(account._getIncome(20))) # <- # ใส่โบนัส และ ค่าทำงานนอกเวลาใน getIncome()
print()
programmer = Programmer("โจโจ้", 40000, 2, "เขียนโค้ด")     # 1) เพิ่มประสบการณ์ทำงาน 2 ปี และ ทักษะพิเศษ เขียนโค้ด
print(programmer.__str__())
print("บัญชี รายได้ต่อปี = {0:,}".format(programmer._getIncome(20)))
print()
sale = Sale("นัท", 35000, "อุบลราชธานี")       # 1) เพิ่มเขตพื้นที่รับผิดชอบ
print(sale.__str__())
print("บัญชี รายได้ต่อปี = {0:,}".format(sale._getIncome(20)))
print()

# write by :sarunwit nontasean
# credit : kongraksiam