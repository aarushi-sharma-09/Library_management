import datetime
import mysql.connector as mycon
mydb=mycon.connect(host="localhost",user="root",password="#NCTzen_neo_9")
mycr=mydb.cursor()
mycr.execute("use library_management")
count=0
def menu():
    while True:
        print(" LIBRARY MANAGEMENT SYSTEM")
        print(" P U B L I C L I B R A R Y")
        print(" *****************************")
        print(" 1- BOOKS")
        print(" 2- MEMBERS")
        print(" 3- TRANSACTION")
        print(" 4- ANALYTICS/QUERY")
        print(" 5- E X I T")
        ch = int(input(" Enter your choice [1-5] :"))
        if ch == 1:
            books()
        elif ch == 2:
            members()
        elif ch == 3:
            transaction()
        elif ch == 4:
            analytics()
        elif ch==5:
            print("THANK YOU VERY MUCH FOR USING LIBRARY MANAGEMENT SYSTEM.")
        break

def books():
    while True:
        print(" B O O K S M E N U")
        print(" **********************")
        print()
        print(" 1- Add New Books")
        print(" 2- Delete old Books")
        print(" 3- Edit book details ")
        print(" 4- B A C K")
        ch = int(input(" Enter your choice [1-3] :"))
        if ch == 1:
            add_books()
        elif ch == 2:
            del_books()
        elif ch == 3:
            edit_book()
        else:
            print("Going back to Main Menu")
            menu()
            break

def add_books():
    book_id=eval(input("Enter book_id"))
    book_name=input("Enter book name")
    date=datetime.date.today()
    author=input("Enter authors name")
    copies=eval(input("Enter no. of copies"))
    cost=eval(input("Enter cost"))
    sql = "insert into books(book_id,book_name,author,cost,date_entry,copies) values(%s,%s,%s,%s,%s,%s)"
    data=(book_id,book_name,author,cost,date,copies)
    mycr.execute(sql,data)
    mydb.commit()
    print("Books added")

def del_books():
    id=input("Enter books id:")
    data=(id,)
    q="delete from books where book_id=%s"
    mycr.execute(q,data)
    mydb.commit()
    print("BOOK deleted")

def edit_book():
    book_id=eval(input("Enter book id:-"))
    while True:
        print("1.Book_NAME")
        print("2.Author")
        print("3.Cost")
        print("4.copies")
        ch = eval(input("Enter your choice(field to be edited)"))
        if ch == 1:
            q = "update books set book_name=%s where book_id=%s"
            d= input("Enter new name")
            break
        elif ch == 2:
            q = "update books set author=%s where book_id=%s"
            d = input("Enter author")
            break
        elif ch == 3:
            q = "update books set cost=%s where book_id=%s"
            d= input("Enter cost")
            break
        elif ch == 4:
            q = "update books set copies=%s where book_id=%s"
            d = input("Enter no. of copies")
            break
        else:
            print("invalid choice")
    data=(d,book_id)
    mycr.execute(q,data)
    mydb.commit()
    print("UPDATED")


def members():
    while True:
        print(" M E M B E R S M E N U")
        print(" *************************")
        print(" 1- Add Members")
        print(" 2- Delete Members")
        print(" 3- Edit detail of the Memebers")
        print(" 4- B A C K")
        ch = int(input(" Enter your choice [1-4] :"))
        if ch == 1:
            add_member()
        elif ch == 2:
            del_member()
        elif ch == 3:
            edit_member()
        else:
            print("Going back to Main Menu")
            menu()
            break
def add_member():
    m_id=eval(input("Enter member id:-"))
    m_name=input("Enter name:-")
    age=eval(input("Enter age"))
    con=eval(input("Enter contact"))
    add=input("Enter address")
    mem="y"
    sql = "insert into members(M_ID,m_name,age,contact,address,membership) values(%s,%s,%s,%s,%s,%s)"
    data=(m_id,m_name,age,con,add,mem)
    mycr.execute(sql, data)
    mydb.commit()
    print("Memeber added")

def del_member():
    id=input("Enter memeber id")
    q="delete from members where m_id=%s"
    data=(id,)
    mycr.execute(q, data)
    mydb.commit()
    print("Member deleted")

def edit_member():
    m_id=eval(input("Enter member id:-"))
    while True:
        print("1.M_NAME")
        print("2.Age")
        print("3.Contact")
        print("4.Address")
        ch = eval(input("Enter your choice(field to be edited)"))
        if ch == 1:
            q = "update members set m_name=%s where m_id=%s"
            d= input("Enter new name")
            break
        elif ch == 2:
            q = "update members set age=%s where m_id=%s"
            d= input("Enter age")
            break
        elif ch == 3:
            q = "update members set contact=%s where m_id=%s"
            d = input("Enter contact")
            break
        elif ch == 2:
            q = "update members set address=%s where m_id=%s"
            d = input("Enter new address")
            break
        else:
            print("invalid choice")
    data=(d,m_id)
    mycr.execute(q,data)
    mydb.commit()
    print("UPDATED")

def transaction():
    while True:
        print(" T R A N S A C T I O N.... M E N U")
        print(" **********************************")
        print()
        print(" 1- Issue a Book")
        print(" 2- Return a Book")
        print(" 3- B A C K")
        ch = int(input(" Enter your choice [1-3] :"))
        if ch == 1:
            issue_book()
        elif ch == 2:
            return_book()
        elif ch==3:
            print("Going back to Main Menu")
            menu()
            break
        else :
            print("invalid choice")

def issue_book():
    m_id=eval(input("Enter member id"))
    book_id=eval(input("Enter book id"))
    date=datetime.date.today()
    sql="insert into transaction(m_id,book_id,dt_issue) values (%s,%s,%s)"
    data=(m_id,book_id,date)
    mycr.execute(sql,data)
    q="update members set ISSUE_STATUS='y' where m_id=%s"
    d=(m_id,)
    mycr.execute(q,d)
    mydb.commit()
    print("Book issued")

def return_book():
    m_id = eval(input("Enter member id"))
    book_id = eval(input("Enter book id"))
    date = datetime.date.today()
    sql = "update transaction set dt_return=%s where m_id=%s and book_id=%s "
    data = (date,m_id, book_id)
    mycr.execute(sql, data)
    q = "update members set ISSUE_STATUS='n' where m_id=%s"
    d=(m_id,)
    mycr.execute(q, d)
    mydb.commit()
    mycr.execute("select * from transaction")
    records=mycr.fetchall()
    for i in records:
        for x in i:
            l=(int(i[-1].day-i[-2].day))
            if l>20:
                L=(20-l)*5
                print("FINE TO BE PAID IS ",L)
            else:
                break
    print("Book returned")

def analytics():
    while True:
        print(" A N A L Y S I S  M E N U")
        print(" ***************************")
        print()
        print(" 1- All Books")
        print(" 2- ALL Members")
        print(" 3- Search Books (Code wise)")
        print(" 4- Search Books (Name wise)")
        print(" 5- Search Member ( Code wise)")
        print(" 6- Search Member (Name wise)")
        print(" 7- Search book issued by member")
        print(" 8- EXIT")
        ch = int(input(" Enter your choice [1-8] :"))
        while True:
            if ch == 1:
                mycr.execute("select book_name,author,copies from books ")
                records = mycr.fetchall()
                for i in records:
                    print(i)
                break
            elif ch == 2:
                mycr.execute("select m_name,age from members")
                records = mycr.fetchall()
                for i in records:
                    print(i)
                break
            elif ch ==3:
                book_id=eval(input("Enter book_id"))
                data = (book_id,)
                try:
                    sql = "select * from books where book_id=%s"
                    mycr.execute(sql, data)
                    records = mycr.fetchall()
                    for i in records:
                        print(i)
                    break
                except:
                    print("Invalid input")
                    break

            elif ch == 4:
                book_name = input("Enter book_name")
                data=(book_name,)
                try:
                    sql = "select * from books where book_name=%s"
                    mycr.execute(sql, data)
                    records = mycr.fetchall()
                    for i in records:
                        print(i)
                    break
                except:
                    print("Inavlid input")
                    break

            elif ch == 5:
                m_id = eval(input("Enter member_id"))
                data=(m_id,)
                try:
                    sql = "select * from members where m_id=%s"
                    mycr.execute(sql,data)
                    records = mycr.fetchall()
                    for i in records:
                        print(i)
                    break
                except:
                    print("Invalid input")
                    break
            elif ch == 6:
                m_name = input("Enter Member_name")
                data=(m_name,)
                try:
                    sql = "select * from members where m_name=%s"
                    mycr.execute(sql, data)
                    records = mycr.fetchall()
                    for i in records:
                        print(i)
                    break
                except:
                    print("Inavlid input")
                    break
            elif ch == 7:
                m_id = eval(input("Enter Memebr id"))
                data=(m_id,)
                try:
                    sql = "SELECT members.m_name, books.book_name, transaction.dt_issue,transaction.dt_return FROM books,members,transaction where members.m_id=transaction.m_id and members.m_id=%s "
                    mycr.execute(sql, data)
                    records = mycr.fetchall()
                    for i in records:
                        print(i)
                    break
                except:
                    print("Inavlid input")
                    break
            if ch == 8:
                menu()


menu()
