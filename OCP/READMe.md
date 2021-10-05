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

Para ilustar esse princípio, consideremos uma aplicação que exibe as notícias do dia de diferentes websites. O código completo pode ser consultado [aqui](./main.py) neste diretório. Como pode-se observar abaixo, `WebsiteSources.py` mantém as classes que são focadas na obtenção das notícias, cada uma com uma única fonte. Dito isso, é possível observar que, caso deseja-se adicionar um novo website, basta que seja criada uma nova classe, via herança, e sobrescrever o construtor, além de chamá-la no método `main.py`. Isso garante o princípio OCP, dado que a extensão será isolada, ou seja, não será necessário interferir no comportamento de nenhuma outra classe! Além disso, observa-se a presença do princípio SRP, já que cada classe está incubida de apenas obter as notícias de determinada fonte.

```python
class NewsFromSource:
    
    def __init__(self, source, url, htlm_tag, html_class):
        self.source = source 
        self.url = url
        self.html_tag = htlm_tag
        self.html_class = html_class
        self.news = []

    def getNews(self):
        self.news = Scraper.Scrap(self.source, self.url, self.html_tag, self.html_class)
        

class NewsFromG1(NewsFromSource):

    def __init__(self):
        NewsFromSource.__init__(self, "G1", "https://g1.globo.com/", "a", "feed-post-link")

    pass
```

Mas a adição de websites não é a única componente que se beneficia do princípio OCP. A própria impressão das notícias também! A classe `Viewer`, ilustrada abaixo, suporta impressões em console e em arquivos CSV. Mas e se for desejado adicionar um terceiro método, que suporte impressões em TXT? Basta então adicionar um método a mais na classe, **relacionado a exibição da saída**, que implemente tal funcionalidade, não interferindo no contexto geral da aplicação! Assim, o código será extendido, mas não modificará qualquer outra componente do código.

```python
class Viewer:

    @staticmethod
    def printConsole(newsList):
        for news in newsList:
            print(news[0], news[1], news[2])
        pass

    @staticmethod
    def printCSV(newsList):
        header = ['source', 'title', 'link']
        with open(newsList[0][0]+'News.csv', 'w', encoding='UTF-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for news in newsList:
                writer.writerow([news[0], news[1], news[2]])
```

Avançando um pouco mais, e se for desejado adicionar algum algoritmo de aprendizado para detectar tendências e diferenças entre os websites? Essas mudanças são mais complexas, mas para atender essa nova requisição, uma nova classe deverá ser desenvolvida, de forma a respeitar o SRP e o OCP. Dessa forma, a chamada para esse algoritmo no código pode ser realizada em `main.py`, possivelmente logo após a obtenção das notícias, a depender do objetivo do algoritmo.

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