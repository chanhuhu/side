# Else and Finally clause handler error in python

```python3
try:
    # do something
    f = open(filename, mode='w')
    f.read()[9999]

except ValueError:
    # handing exception

except IndexError as e:
    # handing exception

except:
    # handing exception

else:
    # excuted when no exception
finally:
    # always excute
    f.close()
```

else และ finally จะใช้ร่วมกับคำสั่ง try ... except โดยความแตกต่างของการทำงานของมัน
นั้นจะแตกต่างจาก else คือจะทำงานในบล็อคคำสั่งนี้เสมอ ไม่ว่าจะเกิดข้อผิดพลาดหรือไม่ก็ตาม
ส่วน else จะทำงานเมื่อไม่เกิดข้อผิดพลาดขึ้น
