def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

while True:
    print("\nketik salah satu karakter pada keyboard utk kalkulator")
    print("q for quit")
    pil = input("Ketik: ")
    n = 0
    ans = 0
    rec = []
    if pil != 'q':
        n = float(input("Masukan angka: "))
        ans = n
        o = ""
        t = 0
        rec.append(n)
        while o != '=':
            list_op = ('+','-','x','/','=')
            e = ""
            for i, op in enumerate(list_op):
                e += str(op) + " "
            print(e)
            o = input("Pilih operator: ")
            rec.append(o)
            if o != '=' :
                if o in list_op:
                    n = float(input("Masukan angka berikutnya: "))
                    rec.append(n)
            if o == list_op[0]:
                ans = add(ans, n)
            elif o == list_op[1]:
                ans = subtract(ans, n)
            elif o == list_op[2]:
                ans = multiply(ans, n)
            elif o == list_op[3]:
                ans = divide(ans, n)
            elif o == list_op[4]:
                break    
            else:
                print("Pilihan tidak ada dalam daftar!")
            t+=1
            
        print("\nHasil = ", ans)
        r = ""
        for a in rec:
            r += str(a) + " "
        print("Record: ", r, ans)
        
    else:
        print("\nAnda telah keluar!")
        break
