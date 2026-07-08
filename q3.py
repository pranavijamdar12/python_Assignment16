def Addition(No1,No2):
    Sum = No1 + No2
    return Sum

def main():
    No1 = int(input("Enter the first number you want:"))
    No2 = int(input("Enter the second number you want:"))
    Ans=Addition(No1,No2)
    print("The addition of two number is:",Ans)

if __name__ == "__main__":
    main()
