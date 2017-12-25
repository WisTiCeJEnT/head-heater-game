import os

upper = ['ข', 'ช', 'บ', 'ย', 'น', 'พ', 'ฟ', 'ห', 'ฆ', 'ฑ', 'ษ', 'ซ', 'ง', 'ผ', 'ป', 'ท', 'ม', 'ฬ', 'ใ', 'ฝ']
middle = ['ค', 'ต', 'จ', 'ฅ', 'ด', 'ศ', 'ฒ', 'ฮ', 'อ', 'ฉ', 'ฐ']
lower = ['ภ', 'ถ', 'ล', 'ญ', 'ณ', 'ฎ', 'ไ', 'ฤ', 'ฏ', 'โ', 'เ', 'ฌ', 'ส', 'ว', 'ฦ', 'ใ', 'ม']
while True:
    os.system('clear')
    print("============================================================")
    print("พิมพ์ \"เลิกเล่น\" เพื่อจบเกม | \"ใบ้\" เพื่อขอคำใบ้")
    print("============================================================")
    print("พ่ออยู่ข้างบน\nแม่อยู่ข้างล่าง\nคนอยู่ตรงกลาง\nธรรมชาติไม่มีในโลก\n")
    word = input("ใส่คำที่จะถามได้เลย : ")
    print("------------------------------------------------------------")
    if word == "เลิกเล่น":
        break
    elif word == "ใบ้":
        os.system('clear')
        print("\nเกมนี้ต้อง \"ใช้ หัว คิด\" :)\n")
        input("Press ENTER to continue . . .")
        continue
    if word[0] in upper:
        print("\n"+word+"อยู่ข้างบน")
    elif word[0] in middle:
        print("\n"+word+"อยู่ตรงกลาง")
    elif word[0] in lower:
        print("\n"+word+"อยู่ข้างล่าง")
    else:
        print("\n"+word+"ไม่มีอยู่ในโลก")
        
    input("\nPress ENTER to continue . . .\n")
