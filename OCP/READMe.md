<h1 align="center"> 
    Princípio Aberto-Fechado / Ocultação da Informação
</h1>

<h4 align="center">
    <img alt="OCP" title="#OCP" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJQwHB-M-TIyO8YvqN4uGlLetYDx3U3z8mEQ&usqp=CAU" width="300px;" />
</h4>

<p align="center">
	<a href="#-O-que-é-?">O que é ?</a> |
	<a href="#-exemplos">Exemplos</a> |
	<a href="#-como-executar">Como executar</a>
</p>

## 🔍 O que é ?

O *Princípio Aberto-Fechado* ou *Princípio da Ocultação da Informação*, segundo Bertrand Meyer, refere-se a capacidade de um software/classe/função permancer aberto para extensões e fechado para modificações, ou seja, deve ser possível realizar adições de campos a esses componentes, enquanto modificações são estritamente pontuais para adaptação das novas adições.
Para exemplificar um pouco mais a definição acima, consideremos os smartphones de hoje em dia. Basicamente, o OCP deve se comportar da mesma forma após a instalação algum app. A adição de um novo programa não impactará o contexto geral do dispositivo (SO), da mesma forma que não afetará outros aplicativos pré-instalados (desconsiderando possíveis comunicações entre eles). Assim, é realizada uma nova adição no dispositivo, sem que haja qualquer modificação.
Para ilustrar um pouco mais, segue um exemplo abaixo.

---

## 💻 Exemplos

Para ilustar esse princípio, consideremos uma aplicação que exibe as notícias do dia de diferentes websites. O código pode ser consultado [aqui](./main.py), seguindo seu fluxo natural. Como pode-se observar, as classes estão isoladas umas das outras, cada uma com uma única responsabilidade (como no princípio SRP). Mas e se desejarmos adicionar um novo site a essa aplicação sem que haja grandes modificações no código? Simples! Basta que uma tupla seja adicionada em `WebsiteSources.py`, indicando a url do site de notícias, a tag a ser buscada, e uma componente da classe para refinar a busca. Apenas uma nova linha deve ser adicionada ao código para que novas notícias sejam impressas!

```python
class WebsiteSources:

    # Websites which we will be extracting the news.
    # They follow the structure: (editor, url, html tag, class type)
    sources = [("G1", "https://g1.globo.com/", "a", "feed-post-link"),
               ("UOL", "https://noticias.uol.com.br/", "h3", "thumb-title"),
               ("EL PAÍS", "https://brasil.elpais.com/", "a", ""),
               # Basta adicionar aqui uma tupla com as informações necessárias!
               ("S.A.", "https://www.scientificamerican.com/", "h2", "t_small-listing-title")]

    @staticmethod
    def getWebsites():
        return WebsiteSources.sources

    pass
```

Mas a adição de websites não é a única componente que se beneficia do princípio OCP. A própria impressão das notícias também! Ao observar a classe `Viewer`, ilustrada abaixo, suporta impressões em console. Mas e se desejarmos uma impressão em um simples .csv? Basta então adicionar um método a mais na classe, não interferindo no contexto geral da aplicação! Além disso, um design pattern *Strategy* também pode ser utilizado para tornar o código ainda mais extensível!

```python
# Class in charge of showing the search results.
class Viewer:

    @staticmethod
    def printConsole(newsList):
        for news in newsList:
            print(news[0], news[1], news[2])
        pass

    @staticmethod
    def printCSV():
        pass
```

Avançando um pouco mais além, e se for desejado adicionar algum algoritmo de aprendizado para detectar tendências e diferenças entre os websites? Essas mudanças são mais complexas, e como pode-se inferir, uma nova classe deverá ser desenvolvida, visando isolar as funcionalidades (mantendo o SRP). Dessa forma, a chamada para esse algoritmo no código pode ser realizada em `Scraper.py`, com a ajuda de um design pattern, como o *Strategy*.

Com isso, fica evidente que a aplicação dos princípios SRP e OCP, apesar de aumentarem um pouco o tamanho dos códigos, os deixam mais legíveis e fáceis para modificação.

---

## 🔌 Como executar

### Pré-requisitos

Certifique-se de que estejam instaladas as seguintes ferramentas:

[Python3](https://www.python.org/downloads/)

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

#### 🧭 Executando a aplicação

```bash

python3 main.py

```

---

## 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

-   **[Python3](https://www.python.org/downloads/)**
-   **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)**

---

## 📘 Referências

[Wikipédia - Princípio Aberto-Fechado](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle#:~:text=In%20object%2Doriented%20programming%2C%20the,without%20modifying%20its%20source%20code.)

[Medium - The SOLID principles in pictures](https://medium.com/backticks-tildes/the-s-o-l-i-d-principles-in-pictures-b34ce2f1e898)
## 🦸 Autor

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img style="border-radius: 25%" src="https://avatars.githubusercontent.com/u/56005905?v=4" width="100px;" alt="Foto de Felipe Tavoni"/><br>
        <sub>
          <b>Felipe Tavoni</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

---

<!-- ## 📝 Licença

Este projeto esta sobe a licença [MIT](./LICENSE).
 -->