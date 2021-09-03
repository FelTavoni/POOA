#include <iostream>
#include <stdlib.h>
#include <string.h>

#define SIZE 20

using namespace std;

class Book {
    private:
        char author[SIZE], title[SIZE], publisher[SIZE];

    public:
        Book(char* author, char* title, char* publisher) {
            strncpy(this->author, author, sizeof(this->author));
            strncpy(this->title, title, sizeof(this->title));
            strncpy(this->publisher, publisher, sizeof(this->publisher));
        }

        ~Book() {
        }

        void showBook() {
            cout << "Author: " << this->author << endl;
            cout << "Title: " << this->title << endl;
            cout << "Publisher: " << this->publisher << endl;
        }

        char* getAuthor() {
            return this->author;
        }

        char* getTitle() {
            return this->title;
        }

        char* getPublisher() {
            return this->publisher;
        }
};

class BookShelf {
    private:
        Book* shelf[SIZE];

    public:
        // Constructor
        BookShelf() {
            // Setting all positions to null
            for (int i = 0; i < SIZE; i++)
                shelf[i] = NULL;
        }

        // Destructor
        ~BookShelf(){
        }

        void AddBook(char* author, char* title, char* publisher) {
            // Searchs for a empty position
            int i;
            int added = 0;
            while ((i < SIZE) && (!added)) {
                if (shelf[i] == NULL) {
                    shelf[i] = new Book(author, title, publisher);
                    added = 1;
                }
                i++;
            }
            if (!added) {
                cout << "Not enough space...remove a book or create a new shef." << endl;
            }
        }

        void RemoveBook(char *title) {
            int i = 0;
            int found = 0;
            while ((i < SIZE) && (!found)) {
                if (shelf[i] != NULL) {
                    if (strncmp(title, shelf[i]->getTitle(), sizeof(shelf[i]->getTitle())) == 0) {
                        found = 1;
                        cout << "Book removed!" << endl;
                        shelf[i]->~Book();
                        shelf[i] = NULL;
                    }
                }
                i++;
            }
            if (!found) {
                cout << "Book not founded..." << endl;
            }
        }

        void searchBook(char* title) {
            int i = 0;
            int found = 0;
            while ((i < SIZE) && (!found)) {
                if (shelf[i] != NULL) {
                    if (strncmp(title, shelf[i]->getTitle(), strlen(title) * sizeof(char)) == 0) {
                        found = 1;
                        cout << "Book founded!" << endl;
                        shelf[i]->showBook();
                    }
                }
                i++;
            }
            if (!found) {
                cout << "Book not founded..." << endl;
            }
        }

        void showBooks() {
            int i = 0;
            while (i < SIZE) {
                if (shelf[i] != NULL) {
                    shelf[i]->showBook();
                    cout << endl;
                }
                i++;
            }
        }

        Book* getBookShelf(int pos) {
            return this->shelf[pos];
        }

};

int main() {
    int option = 0;
    char author[SIZE], title[SIZE], publisher[SIZE];

    BookShelf shelf;

    while (option != -1) {

        // Memset variables to avoid noise
        memset(author, '\0', sizeof(author));
        memset(title, '\0', sizeof(title));
        memset(publisher, '\0', sizeof(publisher));

        cout << "Which operation would you like to run? " << endl;
        cout << "1 - Add new book " << endl;
        cout << "2 - Remove book by tittle" << endl;
        cout << "3 - Search book by title" << endl;
        cout << "4 - Show all books" << endl;
        cout << "(-1) - Exit" << endl;
        cin >> option;

        switch (option) {
            case 1:
                cin.ignore();
                cout << "Adding new book...\n";
                cout << "Author: "; cin.getline(author, SIZE);
                cout << "Title: "; cin.getline(title, SIZE);
                cout << "Publisher: "; cin.getline(publisher, SIZE);
                shelf.AddBook(author, title, publisher);
                break;

            case 2:
                cin.ignore();
                cout << "Removing book...\n";
                cout << "Title: "; cin.getline(title, SIZE);
                shelf.RemoveBook(title);
                break;

            case 3:
                cin.ignore();
                cout << "Searching book...\n";
                cout << "Title: "; cin.getline(title, SIZE);
                shelf.searchBook(title);
                break;

            case 4:
                cin.ignore();
                cout << "Showing all books!" << endl;
                shelf.showBooks();
                break;
            
            default:
                break;
        }

    }

    return 0;
}