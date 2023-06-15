class Books:
    def __init__(self):
        self.name=''
        self.author=''
        self.price=0.0
        self.isbn=''
    def inputBookDetials(self):
        self.name=input("Enter Book name:-")
        self.author=input("Enter Author name:-")
        self.price=input("Enter Book Price:-")
        self.isbn=input("Enter Book ISBN Number:-")
        print(f"{self.name}BOOK added successfully....")
    def bookDisplay(self):
        print(f"Book Name:-{self.name}")    
        print(f"Book Author:-{self.author}")    
        print(f"Book Price:-{self.name}")    
        print(f"Book ISBN:-{self.isbn}")
book_list=[]
while True:
    choice=int(input("Enter your Choice:- \n 1.Add book \n 2.Display book \n 3.Stop \n"))
    if choice==1:  
        b=Books()
        b.inputBookDetials()
        book_list.append(b)
    elif choice==2:
        if len(book_list)==0:
            print('BOOK Is NOT AVAIlable')
        else:
            for i in book_list:
                i.bookDisplay()
    elif choice==3:
        print("Thank for using Application......")
    else:
        print("Enter a valid option")    