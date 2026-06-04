try:
    text=input("enter string")

    file=open("data.txt","w")
    file.write(text)
    file.close()

    file=open("data.txt","r")
    content=file.read()
    file.close()

    print (" f content",content)
     
except FileNotFoundError:
    print("not found")

except Exception as e:
    print("error",e)