def main():
    print("Welcome to the number system converter!!!")
    s = input("What number system do you want to convert from? ").strip().lower()
    e = input("To? ").strip().lower()
    result = 0

    if s == "binary":
        nbit = int(input("Think your number first and type how many bits does that number have? ").strip())
        b = input("Type your binary number: ").strip()

        if len(b) == nbit:
            if e == "decimal":
                j = nbit - 1
                for i in b:
                    result += int(i)*(2**(j))
                    j -= 1
                
                print(result)
    elif s == "decimal":
        d = int(input("Type your decimal number: ").strip())
        l = []

        if e == "binary":
            while d >= 1:
                l.append(d%2)
                d = d//2
            l.reverse()
            l = list(map(str,l))

            print("".join(l))
        elif e == "hexadecimal":
            while d > 0:
                l.append(d%16)
                d = d//16
            l.reverse()
            l = list(map(str,l))

            print("".join(l))

main()
