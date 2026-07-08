def Divisible(no):
    if no % 5 == 0:
        return True
    else:
        return False

def main():
    no = int(input("Enter the number you want:"))
    ret = Divisible(no)
    print(ret)
    

if __name__ == "__main__":
    main()
