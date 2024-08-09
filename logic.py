def converter(num):
    code = []
    while num > 0:
        kalan = num%2
        code.append(kalan)
        num = num//2
    code.reverse()
    return code

while True:
    num = input("sayı giriniz: ")
    try:
        num = int(num)
        print("sayı girildi")
        binary= converter(num)
        print("binary: ", binary)
        break
    except ValueError:
        print("Lütfen bir sayı giriniz")


