<h1 align="center"> 
	Princípio da Responsabilidade Única
</h1>

<h4 align="center">
    <img alt="SRP" title="#SRP" src="https://res.cloudinary.com/practicaldev/image/fetch/s--1QS5jGfh--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://dev-to-uploads.s3.amazonaws.com/i/wq2iycdlr8om91wzed1y.png" width="300px;" />
</h4>

<p align="center">
	<a href="#-O-que-é-?">O que é ?</a> |
	<a href="#-exemplos">Exemplos</a> |
	<a href="#-como-executar">Como executar</a>
</p>

## 🔍 O que é ?

O Princípio da Responsabilidade Única é um dos cinco princípios de programação orientada a objetos - os princípios **SOLID**. Segundo este princípio, descrito por *Robert C. Martin* em seu livro *Agile Software Development, Principles, Patterns, and Practices*, uma classe deve ter apenas um, e somente um, motivo para mudar.

Para entender um pouco melhor este conceito, considere a imagem acima. Um canivete suiço é equipado com diversas ferramentas, garantindo que a pessoa que o porta esteja preparada para qualquer adversidade. Mas vamos analisar suas ferramentas: saca-rolhas, lâmina, abridor de latas, lixa, lâmina furadora...muitas não!? Essa característica claramente fere o princípio elaborado pelo *Uncle Bob*. Isso porque, caso o princípio fosse aplicado à fabricação de canivetes, deveríamos ter vários deles, cada qual com uma *única ferramenta*. Assim, dependendo da situação, utilizaríamos aquele que está com a ferramenta que realmente desejamos, pois é *responsabilidade* dessa resolver nosso problema em determinada situação.

Dito isso, o software não é diferente. Uma classe pode implementar diversos métodos, cada qual com uma responsabilidade. Assim, o que o princípio prega é que as responsabilidades dos métodos devem estar alinhadas com todos os outros em uma determinada classe, de maneira **coesa**, garantindo que a classe em si tenha apenas uma única responsabilidade no escopo da aplicação. Dessa forma, a classe, com uma única resposabilidade no contexto geral, terá um único motivo para ser modificada, caso necessário, visto que apresenta uma **única responsabilidade**, uma **única função**. Isso permite que em uma aplicação, os componentes (classes) que a compõe estejam de certa forma **fracamente acopladas**, pois uma não apresenta dependência das outras para executar.

Em suma, o Princípio da Responsabilidade Única nada mais é do que uma boa prática de construção de software. Manter essas responsabilidades coesas e pouco acopladas, contribui para que futuras manutenções sejam mais fáceis, além de evitar que haja futuramente algum erro relacionado a alguma dependêcia desse componente.

Vejamos a seguir um exemplo.

---

## 💻 Exemplos

Observe o código abaixo que implementa um administrador de livros em uma estante. Duas classes compõe essa aplicação: *Book* e *BookShelf*. Mas elas apresentam um problema...

Ao observar a função da classe *Book*, seus métodos são responsáveis por criar, destruir, mostrar/imprimir o conteúdo e getters. Podemos dividir essas funcionalidades em duas, *gerenciamento* e *impressão*. Dado isso, conclui-se que a classe *Book* fere o SRP. Não obstante, o mesmo ocorre com a classe *BookShelf*, que também se encarrega do gerenciamento dos livros e da impressão desses. Novamente, há conflito com o princípio.

```c++
class Book {
    private:
        char author[SIZE], title[SIZE], publisher[SIZE];

    public:
        Book(char* author, char* title, char* publisher) {
            // Instancia um livro
        }

        ~Book() {
        }

        void showBook() {
            // Exibe o conteúdo do livro.
        }

        char* getTitle() {
			// Retorna o título do livro.
        }
};

class BookShelf {
    private:
        Book* shelf[SIZE];

    public:
        // Constructor
        BookShelf() {
            // Cria uma estante
        }

        // Destructor
        ~BookShelf(){
        }

        void AddBook(char* author, char* title, char* publisher) {
            // Adiciona um livro
        }

        void RemoveBook(char *title) {
            // Remove um livro por título
        }

        void searchBook(char* title) {
            // Busca um livro por título
        }

        void showBooks() {
            // Imprime todos os livros
        }

};

int main() {
    int option = 0;
    char author[SIZE], title[SIZE], publisher[SIZE];

    BookShelf shelf;

    // Loop de gerenciamento.
}
```

Para resolver isso, é necessário que essas funcionalidades sejam internacionalizadas, ou seja, removidas e inseridas em um contexto global, como é possível observar no código abaixo.

```c++
class Book {
    private:
        char author[SIZE], title[SIZE], publisher[SIZE];

    public:
        Book(char* author, char* title, char* publisher) {
            // Instancia um livro
        }

        ~Book() {
        }

        void showBook() {
            // Exibe o conteúdo do livro.
        }

        char* getAuthor() {
            // Retorna o autor do livro.
        }

        char* getTitle() {
            // Retorna o título do livro.
        }

        char* getPublisher() {
            // Retorna a editora do livro.
        }
};

class BookShelf {
    private:
        Book* shelf[SIZE];

    public:
        // Constructor
        BookShelf() {
            // Cria uma estante
        }

        // Destructor
        ~BookShelf(){
        }

        void AddBook(char* author, char* title, char* publisher) {
            // Adiciona um livro
        }

        void RemoveBook(char *title) {
            // Remove um livro por título
        }

        void searchBook(char* title) {
            // Busca um livro por título
        }

        Book* getBookShelf(int pos) {
            // Retorna o array das prateleiras
        }

};

class Viewer {
    public:
        Viewer() {
        }

        void showContent(Book* book) {
            // Imprime o conteúdo de um livro
        }

        void showAllContent(BookShelf shelf) {
            // Imprimindo o conteúdo de todos os livros
        }
};

int main() {
    int option = 0;
    char author[SIZE], title[SIZE], publisher[SIZE];

    BookShelf shelf;

    // Loop de gerenciamento.
}

```

Por fim, podemos ver que a classe *Viewer* se encarrega de imprimir os conteúdos apenas. Isso facillita futuras mudanças no código. Caso alguma informação mude, basta que mudanças sejam feitas apenas na classe *Viewer*! 

---

## 🔌 Como executar

### Pré-requisitos

Pré-requisitos para rodar
[C++ Compiler](https://gcc.gnu.org/install/download.html). 

#### 🧭 Executando a aplicação

```bash

# Para compilar o bom exemplo...
$ g++ Books_Good.cpp -o Books_Good

# Para executar o bom exemplo...
$ ./Books_Good

# Para compilar o mau exemplo...
$ g++ Books_Bad.cpp -o Books_Bad

# Para executar o mau exemplo...
$ ./Books_Bad

```

---

## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

-   **[C++ Compiler](https://gcc.gnu.org/install/download.html)**

---

## 📘 Referências

[Wikipédia - Princípio da Responsabilidade Única](https://en.wikipedia.org/wiki/Single-responsibility_principle)

## 🦸 Autor

<a>
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/56005905?v=4" width="100px;" alt=""/>
 <br />
 <sub><b>Felipe Tavoni</b></sub></a>
 <br />

---

<!-- ## 📝 Licença

Este projeto esta sobe a licença [MIT](./LICENSE).
 -->