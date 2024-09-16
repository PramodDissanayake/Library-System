class Books:
    def __init__(self, isbn_number, title, format, subject, rental_price_per_day, number_of_copies):
        self.isbn_number = isbn_number
        self.title = title
        self.format = format
        self.subject = subject
        self.rental_price_per_day = rental_price_per_day
        self.number_of_copies = number_of_copies

    def intro():
        print("********************************")
        print("""    1. View all the books
    2. Add a new resource to the system.
    3. Remove a resource from the system.
    4. View currently available resources.
    5. View currently unavailable resources.
    6. View all resources (any type) filtered by subject.
    7. Lend a resource.
    8. Update resource.
    9. Go to menu
    10. Exit""")
        print("********************************")


class booklist(Books):
    def __init__(self):
        self.book_L = []
        self.append1()

    def append1(self):

        book_1 = Books(isbn_number='ISBN1234', title='The Solar System', format='Hardcover', subject='Science',
                       rental_price_per_day=15.00, number_of_copies=5)
        self.book_L.append(book_1)
        book_2 = Books(isbn_number='ISBN9979', title='Types of Body Species', format='Paperback', subject='Science',
                       rental_price_per_day=10.00, number_of_copies=8)
        self.book_L.append(book_2)
        book_3 = Books(isbn_number='ISBN5290', title='Second World War', format='Hardcover', subject='History',
                       rental_price_per_day=12.50, number_of_copies=1)
        self.book_L.append(book_3)

    def all_list(self):
        for l in self.book_L:
            print(
                f"ISBN Number:{l.isbn_number}, Title:{l.title}, Format:{l.format}, Subject:{l.subject}, Rental price per day:{l.rental_price_per_day}, Number of copies:{l.number_of_copies} ")

    def add(self):
        isbn_number1 = input("ISBN Number: ").strip().upper()
        title1 = input("Title of the book: ").strip().capitalize()
        format1 = input("Format of the book: ").strip().capitalize()
        subject1 = input("Subject Name: ").strip().capitalize()
        rental_price_per_day1 = float(input("Rental price per day: "))
        number_of_copies1 = int(input("Number of Copies: "))
        books1 = Books(isbn_number=isbn_number1, title=title1, format=format1, subject=subject1,
                       rental_price_per_day=rental_price_per_day1, number_of_copies=number_of_copies1)
        self.book_L.append(books1)

    def remove(self):
        delete = input("Enter the ISBN number: ").upper()
        y = [l for l in self.book_L if l.isbn_number == delete]
        for l in y:
            self.book_L.remove(l)
        self.all_list()

    def lend(self):
        isbmn1 = input("Enter the ISBN number: ").upper()
        copy = int(input("Enter number of copies need to lend: "))
        y = list(l for l in self.book_L if l.isbn_number == isbmn1)
        for l in y:
            l.number_of_copies -= copy
        self.all_list()

    def give(self):
        isbmn1 = input("Enter the ISBN number: ").upper()
        copy = int(input("Enter number of copies need to Update: "))
        y = list(l for l in self.book_L if l.isbn_number == isbmn1)
        for z in y:
            z.number_of_copies += copy
        self.all_list()

    def zero(self):
        y = [l for l in self.book_L if l.number_of_copies == 0]
        for z in y:
            print(
                f"ISBN Number:{z.isbn_number}, Title:{z.title}, Format:{z.format}, Subject:{z.subject}, Rental price per day:{z.rental_price_per_day}, Number of copies:{z.number_of_copies} ")

    def available(self):
        y = [l for l in self.book_L if l.number_of_copies > 0]
        for z in y:
            print(
                f"ISBN Number:{z.isbn_number}, Title:{z.title}, Format:{z.format}, Subject:{z.subject}, Rental price per day:{z.rental_price_per_day}, Number of copies:{z.number_of_copies} ")

    def view(self):
        view1 = input("Enter the Subject name: ").upper()
        y = [l for l in self.book_L if l.subject == view1]
        for z in y:
            print(self.book_L)

    def continue_p(self):
        print("*****************************************")
        choice = input("Do yo Need to Continue (y/n)").upper()
        if choice == "Y":
            Books.intro()
            menu1()
        else:
            quit()


def menu1():
    try:
        select2 = int(input("Select what  you want to do?"))
    except ValueError:
        print("An exception occurred")
    while select2 < 0 or select2 > 9:
        input()
        try:
            select2 = int(input("Select what  you want to do?"))
        except ValueError:
            print("An exception occurred")

    if select2 == 1:
        booklist().all_list()
        print("*****************************************")
        booklist().continue_p()

    elif select2 == 2:
        booklist().add()
        print("*****************************************")
        choice1 = input("Do you need to view the all details (y/n)").upper()
        if choice1 == "Y":
            booklist().all_list()
        else:
            booklist().continue_p()

    elif select2 == 3:
        booklist().remove()
        booklist().continue_p()

    elif select2 == 4:
        booklist().available()
        booklist().continue_p()

    elif select2 == 5:
        booklist().zero()
        booklist().continue_p()

    elif select2 == 6:
        booklist().view()

    elif select2 == 7:
        booklist().lend()
        booklist().continue_p()

    elif select2 == 8:
        booklist().give()
        booklist().continue_p()

    elif select2 == 9:
        menu()

    elif select2 == 10:
        quit
class Magazines:  # start_Magazines
            def __init__(self, Magazines_number, title, color, subject, rental_price_per_day, number_of_copies):
                self.Magazines_number = Magazines_number
                self.title = title
                self.color = color
                self.subject = subject
                self.rental_price_per_day = rental_price_per_day
                self.number_of_copies = number_of_copies

            def intro():
                print("********************************")
                print("""         1. View all the Magazines
         2. Add a new resource to the system.
         3. Remove a resource from the system.
         4. View currently available resources.
         5. View currently unavailable resources.
         6. View all resources (any type) filtered by subject.
         7. Lend a resource.
         8. Update resource.
         9. Go to menu
         10. Exit""")
                print("********************************")

class Magazinelist(Magazines):
            def __init__(self):
                self.Magazine_L = []
                self.append2()

            def append2(self):
                Magazine_1 = Magazines(Magazines_number='01', title='History of Cricket', color='color',
                                       subject='Sports',
                                       rental_price_per_day=5.00, number_of_copies=7)
                self.Magazine_L.append(Magazine_1)
                Magazine_2 = Magazines(Magazines_number='02', title='Evolution of the Computer', color='black&white',
                                       subject='Technology',
                                       rental_price_per_day=3.00, number_of_copies=21)
                self.Magazine_L.append(Magazine_2)
                Magazine_3 = Magazines(Magazines_number='03', title='Programming for Beginners', color='black&white',
                                       subject='Technology',
                                       rental_price_per_day=15.00, number_of_copies=5)
                self.Magazine_L.append(Magazine_3)

            def all_list(self):
                for l in self.Magazine_L:
                    print(
                        f"Magazines_number:{l.Magazines_number}, Title:{l.title}, color:{l.color}, Subject:{l.subject}, Rental price per day:{l.rental_price_per_day}, Number of copies:{l.number_of_copies} ")

            def add(self):
                Magazines_number1 = input("Magazines_number: ").strip().upper()
                title1 = input("Title of the Magazines: ").strip().capitalize()
                color1 = input("Format of the Magazines: ").strip().capitalize()
                subject1 = input("Subject Name: ").strip().capitalize()
                rental_price_per_day1 = float(input('Rental price per day: '))
                number_of_copies1 = int(input("Number of Copies: "))
                Magazines1 = Magazines(Magazines_number=Magazines_number1, title=title1, color=color1, subject=subject1,
                                       rental_price_per_day=rental_price_per_day1, number_of_copies=number_of_copies1)
                self.Magazine_L.append(Magazines1)

            def remove(self):
                delete = input("Enter the  Magazine number: ").upper()
                y = [l for l in self.Magazine_L if l.Magazines_number == delete]
                for l in y:
                    self.Magazine_L.remove(l)
                self.all_list()

            def lend(self):
                num1 = input("Enter the  Magazine number: ").upper()
                copy = int(input("Enter number of copies need to lend: "))
                y = list(l for l in self.Magazine_L if l.Magazines_number == num1)
                for l in y:
                    l.number_of_copies -= copy
                self.all_list()

            def give(self):
                num1 = input("Enter the  Magazine number: ").upper()
                copy = int(input("Enter number of copies need to lend: "))
                y = list(l for l in self.Magazine_L if l.Magazines_number == num1)
                for z in y:
                    z.number_of_copies += copy
                self.all_list()

            def zero(self):
                y = [l for l in self.Magazine_L if l.number_of_copies == 0]
                for z in y:
                    print(
                        f"Magazines_number:{z.Magazines_number}, Title:{z.title}, color:{z.color}, Subject:{z.subject}, Rental price per day:{z.rental_price_per_day}, Number of copies:{z.number_of_copies} ")

            def available(self):
                y = [l for l in self.Magazine_L if l.number_of_copies > 0]
                for z in y:
                    print(
                        f"Magazines_number:{z.Magazines_number}, Title:{z.title}, color:{z.color}, Subject:{z.subject}, Rental price per day:{z.rental_price_per_day}, Number of copies:{z.number_of_copies} ")

            def view(self):
                view1 = input("Enter the Subject name: ").upper()
                y = [l for l in self.Magazine_L if l.subject == view1]
                for z in y:
                    print(self.Magazine_L)

            def continue_p(self):
                print("*****************************************")
                choice = input("Do yo Need to Continue (y/n)").upper()
                if choice == "Y":
                    Magazines.intro()
                    menu2()
                else:
                    quit()

def menu2():
            try:
                select3 = int(input("Select what  you want to do?"))
            except ValueError:
                print("An exception occurred")
            while select3 < 0 or select3 > 9:
                input()
                try:
                    select3 = int(input("Select what  you want to do?"))
                except ValueError:
                    print("An exception occurred")

            if select3 == 1:
                Magazinelist().all_list()
                print("*****************************************")
                Magazinelist().continue_p()

            elif select3 == 2:
                Magazinelist().add()
                print("*****************************************")
                choice1 = input("Do you need to view the all details (y/n)").upper()
                if choice1 == "Y":
                    Magazinelist().all_list()
                else:
                    Magazinelist().continue_p()

            elif select3 == 3:
                Magazinelist().remove()
                Magazinelist().continue_p()

            elif select3 == 4:
                Magazinelist().available()
                Magazinelist().continue_p()

            elif select3 == 5:
                Magazinelist().zero()
                Magazinelist().continue_p()

            elif select3 == 6:
                Magazinelist().view()
                Magazinelist().continue_p()
            elif select3 == 7:
                Magazinelist().lend()
                Magazinelist().continue_p()

            elif select3 == 8:
                Magazinelist().give()
                Magazinelist().continue_p()

            elif select3 == 9:
                menu()

            elif select3 == 10:
                quit
        # end_Magazines

def menu():
    def input1():
        print("=========================================")
        print("Welcome to OUSL Library System!")

        print("=========================================")
        print("""Main Menu 
-----------------------------------------
    1. Books
    2. Magazines 
    3. Educational DVDs .
    4. Lecture CDs 
    5. Exit 
""")

    input1()
    try:
        select = int(input("Which resource details you want to find?"))
    except ValueError:
        print("An exception occurred")
    while select < 0 or select > 5:
        input1()
        try:
            select = int(input("Which resource details you want to find?"))
        except ValueError:
            print("An exception occurred")
    if select == 5:
        quit()
    elif select == 1:
        Books.intro()
        menu1()
    elif select == 2:
        Magazines.intro()
        menu2()


menu()
