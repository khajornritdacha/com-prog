mname = ["Jan", "Feb","Mar","Apr",
 "May","Jun","Jul","Aug",
 "Sep","Oct","Nov","Dec"]

def read_date(): # อ่านวันเดือนปีคั่นด้วยช่องว่าง เดือนเป็นชื่อเดือน คืนลิสต์ เลขวัน เดือน ปี
    date1 = input().split()
    d1 = int(date1[0])
    m1 = mname.index(date1[1][:3]) + 1
    y1 = int(date1[2])
    return [d1, m1, y1]


def zodiac(d,m): # คืนชื่อราศีของวัน d เดือน m
    if d >= 22 and m==3 or d <=21 and m==4 : z2 = "Aries"
    elif d >= 22 and m==4 or d <=21 and m==5 : z2 = "Taurus"
    elif d >= 22 and m==5 or d <=21 and m==6 : z2 = "Gemini"
    elif d >= 22 and m==6 or d <=21 and m==7 : z2 = "Cancer"
    elif d >= 22 and m==7 or d <=21 and m==8 : z2 = "Leo"
    elif d >= 22 and m==8 or d <=21 and m==9 : z2 = "Virgo"
    elif d >= 22 and m==9 or d <=21 and m==10 : z2 = "Libra"
    elif d >= 22 and m==10 or d <=21 and m==11 : z2 = "Scorpio"
    elif d >= 22 and m==11 or d <=21 and m==12 : z2 = "Sagittarius"
    elif d >= 22 and m==12 or d <=20 and m==1 : z2 = "Capricorn"
    elif d >= 21 and m==1 or d <=20 and m==2 : z2 = "Aquarius"
    elif d >= 21 and m==2 or d <=21 and m==3 : z2 = "Pisces"
    return z2

def days_in_feb(y): # คืนจ านวนวันของเดือนกุมภาพันธ์ในปี y
    days_in_feb1 = 28
    if y % 400 == 0 or y % 100 != 0 and y%4 == 0 :
        days_in_feb1 = 29
    return days_in_feb1
   
def days_in_month(m,y): # คืนจ านวนวันของเดือน m ในปี y
    days_in_m1 = 31
    if m==4 or m==6 or m==9 or m==11 :
        days_in_m1 = 30
    elif m==2 :
        days_in_m1 = days_in_feb(y)
    return days_in_m1

def days_in_between(d1,m1,y1,d2,m2,y2):
 # คืนจ านวนวันตั้งแต่วันเดือนปีd1,m1,y1 ถึง d2,m2,y2 
    days = 0
    for m in range(2, 13):
        if m1  < m:
            days += days_in_month(m, y1)

    for m in range(1, 12):
        if m2 > m:
            days += days_in_month(m, y2)
   
    days += (days_in_month(m1, y1) - d1 + 1) + int((y2 - y1 - 1)*365.25) + (d2 - 1)

    return days

def main() :
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date() 
    # แสดง ราศีของ d1,m1,y1 กับ ของ d2,m2,y2 บรรทัดเดียกัน คั่นด้วยช่องว่าง
    # แสดงจ านวนวันตั้งแต่ d1,m1,y1 ถึง d2,m2,y2
    print(zodiac(d1, m1), zodiac(d2, m2))
    print(days_in_between(d1, m1, y1, d2, m2, y2))

exec(input().strip()) # ต้องมีบรรทัดนี้เมื่อส่งไป grader