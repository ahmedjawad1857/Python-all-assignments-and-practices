# Book-Catalog-App
from typing import Any
class App:
    def __init__(self,)->None:
        self.books:list[dict[str,Any]] = []
    def add_book(self,author:str,title:str,genre:str,year:int)->None:
        book:dict[str,Any] = {"Title":title,"Author":author,"Genre":genre,"Year":year}    
        self.books.append(book)
        print(f"Book '{title}' by Author '{author}' is added.")
    def display_book(self, books: list[dict[str, Any]])->None:
      if self.books:  
        for i,book in enumerate(books,1):
            print(f"{i}. {book['Title']} by Author '{book['Author']}' (genre {book['Genre']} by Year {book['Year']})")
            book['id'] = i
      else:
          print("No Books Found.")           
    def search_book_by_author(self,author:str)->list:
        result = [book for book in self.books if book['Author'].lower() == author.lower()]
        return result             
    def search_book_by_genre(self,genre:str)->list:
        result = [book for book in self.books if book['Genre'].lower() == genre.lower()]
        return result
    def search_book_by_year(self,year:int)->list:
        result = [book for book in self.books if book['Year'] == year]
        return result
    def delete_book(self,id:int)->None:
        for book in self.books:
            if book['id'] == id:
                self.books.remove(book)
                print(f"Book '{book['Title']}' is deleted.")
                break
            else:
                print(f"Invalid Id.")
    def update_book(self,id:int,newTitle:str,newAuthor:str,newGenre:str,newYear:int)->None:
         for book in self.books:
            if book['id'] == id:
                self.books.remove(book)
                print(f"Book with id '{id}' is Updated.")
                book['Title'] = newTitle
                book['Author'] = newAuthor
                book['Genre'] = newGenre
                book['Year'] = newYear
            
                break
            else:
                print(f"Invalid Id.")         
app:App = App()


while True:
    print("\n===== Book Catalog Menu =====")
    print("1. Add a Book")
    print("2. Search Books by Author")
    print("3. Search Books by Genre")
    print("4. Search Books by Year")
    print("5. Delete Books by Title")
    print("6. Update Books by Title")
    print("7. Display All Books")
    print("8. Exit")

    choice:str = input("Enter your choice: ").strip()      
    
    match choice :
        case "1":
            author:str = input("Enter Author: ")
            title:str = input("Enter Title: ")
            genre:str = input("Enter Genre: ")
            year:int = int(input("Enter Year: "))
            app.add_book(author,title,genre,year)
            app.display_book(app.books)
        case "2":
            author1:str = input("Enter Author: ")
            result:list = app.search_book_by_author(author1)
            if result:
                print("\nBooks by", author1)
                app.display_book(result)
            else:
                print("No books found by", author1)
        case "3":
            genre1:str = input("Enter genre: ")
            result1:list = app.search_book_by_genre(genre1)
            if result1:
                print(f"\nBooks in {genre1} genre")
                app.display_book(result1)
            else:
                print(f"No books in {genre1} genre")
        case "4":
            year1 = int(input("Enter year:  "))
            result2:list = app.search_book_by_year(year1)
            if result2:
                print(f"\nBooks in {year1} year")
                app.display_book(result2)
            else:
                print(f"No books in {year1} year")
        case "5":
            id:int = int(input("Enter Id: "))
            app.delete_book(id)
            app.display_book(app.books)   
        case "6":
            id1:int = int(input("Enter Id: "))
            newYear:int = int(input("Enter Year: "))
            newTitle:str = input("Enter Title:  ")
            newAuthor:str = input("Enter Author:  ")
            newGenre:str = input("Enter Genre:  ")
            app.update_book(id1,newTitle=newTitle,newGenre=newGenre,newAuthor=newAuthor,newYear=newYear)
            app.display_book(app.books)           
        case "7":
            app.display_book(app.books)
        case "8":
            break
        case _ :
            print("Invalid choice")                
            