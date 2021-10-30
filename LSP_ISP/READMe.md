<h1 align="center"> 
    Princípio da Substituição de Liskov e Princípio da Segregação de Interfaces
</h1>

<h4 align="center">
    <img alt="LSP" title="#LSP" src="https://c3.iggcdn.com/indiegogo-media-prod-cld/image/upload/c_fit,w_auto,g_center,q_auto:best,dpr_2.6,f_auto/v2vmlvqyrdib9qtfdfwc" width="230px;" />
    <img alt="ISP" title="#ISP" src="https://thumbs.dreamstime.com/b/ac-power-sockets-all-types-realistic-illustration-135680600.jpg" width="210px;" />
</h4>

<p align="center">
	<a href="#-O-que-é-?">O que são ?</a> |
	<a href="#-exemplos">Exemplos</a>
</p>

## 🔍 O que são ?

O *Princípio de Substituição de Liskov* prega que os subtipos devem ser substituíveis pelos seus tipos de base, ou seja, uma classe filha deve ser capaz de subtistituir uma classe pai. Isso permite um maior reforço da consistência na herança, para que ambas as classes possam ser alteradas sem problemas de bugs. Considere um pato. Esse é capaz de nadar, grasnar e até botar ovos. Agora imagine um pato de borracha. Esse pode até nadar (já que ele bóia) e até grasnar (se possuir um guizo). Mas não bota ovos. Mapeando essas representações para classes, é possível implementar a classe do pato como Duck, com métodos para nadar, grasnar e botar ovos. Agora, ao implementar a classe RubberDuck, esse deve ser uma herança de Duck!? A resposta é não, pois não apresentaria um método para botar ovo, não sendo possível substituir a classe pai em determinadas situações em que botar ovo é necessário. Assim, o correto é a criação de uma nova classe para RubberDuck.

Já o *Princípio de Segregação das Interfaces* diz que clientes não devem ser forçados a depender de interfaces que não utilizam. Em outras palavras, uma classe não deve ser fundida com uma ferramenta que executa uma ação. Na verdade, ela deve ser fundida com a interface que oferece essa ferramenta. Um exemplo de uso, mais abstrato, são as tomadas. Não podemos utilizar qualquer tipo de carregador em uma delas, pois a interface (a caixa da tomada) nos impede disso. Assim, apenas alguns modelos conseguem se adaptar e carregar determinado dispositivo. Não obstante, o mesmo deve ocorrer com as interfaces em orientação em objetos, impedindo que o programador tenha um acesso indevido à raíz da ferramenta ao qual acessa.

---

## 💻 Exemplos

Uma implementação de urna eletrônica foi realizada em UML para ilustrar os princípios acima, além de seguir os anteriormente apresentados. Você pode consultá-los [aqui](./UrnaEletronica.png).

---

## 📘 Referências

[Wikipédia - Princípio Aberto-Fechado](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle#:~:text=In%20object%2Doriented%20programming%2C%20the,without%20modifying%20its%20source%20code.)

[Medium - The SOLID principles in pictures](https://medium.com/backticks-tildes/the-s-o-l-i-d-principles-in-pictures-b34ce2f1e898)

---

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