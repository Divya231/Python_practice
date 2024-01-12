def fin():
    try :
        l=[1,2,4,5,7]
        i=int(input("Enter index"))
        print(l[i])
        return 1
    except Exception as e:
        print(e)
        return 0
    finally:
        print("I'm always executed")
c=fin()
print(c)
    
