def main():
    try:
        n = int(input("Enter the Number : "))
        print(n)
        return
        
    except Exception as e:
        print(e)
        return
        
    finally:
        print("I am Inside Finally") # It Will Execute all Time 

main()