<h1> Trabalho Grafos </h1>

> **Status do Projeto:** Em desenvolvimento ⚠️

> **Documentação:** [LaTeX](https://www.overleaf.com/2134921852dhsmmwyjjjqv)

O intuito desse trabalho prático é criar dois métodos para indentificação de pontes. Pontes são arestas cuja a remoção torna o grafo desconexo. Dentre as aplicações de indentificações de pontes está encontrar os caminhos ou ciclos eurelianos em diferentes grafos, sendo os métodos de identificação de pontes e suas respectivos diretórios:
- [Método Naive](https://github.com/zTrolly/trabalho-grafos/blob/main/BridgeIdentification/naive.py)
- [Método de Tarjan (1974)](https://github.com/zTrolly/trabalho-grafos/blob/main/BridgeIdentification/tarjan_1974.py)

Além dos métodos descritos acima a implementação deverá encontrar um caminho euleriano em um grafo qualquer ou determinar que ele não existe utilizando o seguinte método:
- [Método de Fleury](https://github.com/zTrolly/trabalho-grafos/blob/main/BridgeIdentification/EulerianPath/eulerian_path.py)

Alguns experimentos devem ser realizados em apenas uma máquina para avaliar o tempo gasto para as duas estrátegias de identificação de pontes em grafos aleatórios, sendo os grafos eulerianos, semi-eulerianos e não eulerianos contendo 100, 1000, 10000, 100000 vértices para cada tipo de grafo.
- [Código Python - Criação grafos aleatórios](https://github.com/zTrolly/trabalho-grafos/blob/main/RandomGraphs/random_graph.py)
- [Agoritmo e explicação de cada grafo](https://github.com/zTrolly/trabalho-grafos/blob/main/RandomGraphs/README.md)

--------------------
<p style="font-size: 16px"> <strong> Resultado avaliação - tempo médio: </strong> </p>

Todos os experimentos foram realizados em uma máquina com 16GB de memória RAM 4666MHz, com uma CPU i7-11600K - 4.3GHz, com SSD. Essas especificações de máquina podem ser alteradas.

<br>

<p style="font-size: 16px"> <strong> Método Naive: </strong> </p>

<div align="center" class="table-responsive">

<table class="table">
  <tr>
    <th>Vértices</th>
    <th>Tipo grafo</th>
    <th>Tempo</th>
  </tr>
  <tr>
    <td>100</td>
    <td>Euleriano</td>
    <td>0.0028 s.</td>
  </tr>
  <tr>
    <td>1000</td>
    <td>Euleriano</td>
    <td>0.3447 s.</td>
  </tr>
  <tr>
    <td>10000</td>
    <td>Euleriano</td>
    <td>42.5453 s.</td>
  </tr>
  <tr>
    <td>100000</td>
    <td>Euleriano</td>
    <td>X</td>
  </tr>
</table>

<table class="table">
  <tr>
    <th>Vértices</th>
    <th>Tipo grafo</th>
    <th>Tempo</th>
  </tr>
  <tr>
    <td>100</td>
    <td>Semi-euleriano</td>
    <td>0.0029 s.</td>
  </tr>
  <tr>
    <td>1000</td>
    <td>Semi-euleriano</td>
    <td>0.3480 s.</td>
  </tr>
  <tr>
    <td>10000</td>
    <td>Semi-euleriano</td>
    <td>42.2774 s.</td>
  </tr>
  <tr>
    <td>100000</td>
    <td>Semi-euleriano</td>
    <td>X</td>
  </tr>
</table>

<table class="table">
  <tr>
    <th>Vértices</th>
    <th>Tipo grafo</th>
    <th>Tempo</th>
  </tr>
  <tr>
    <td>100</td>
    <td>Não euleriano</td>
    <td>0.0060 s.</td>
  </tr>
  <tr>
    <td>1000</td>
    <td>Não euleriano</td>
    <td>0.8264 s.</td>
  </tr>
  <tr>
    <td>10000</td>
    <td>Não euleriano</td>
    <td>42.6835 s.</td>
  </tr>
  <tr>
    <td>100000</td>
    <td>Não euleriano</td>
    <td>X</td>
  </tr>
</table>

</div>

<hr>

<p style="font-size: 16px"> <strong> Método Tarjan: </strong> </p>
<div align="center" class="table-responsive">

<table class="table">
  <tr>
    <th>Vértices</th>
    <th>Tipo grafo</th>
    <th>Tempo</th>
  </tr>
  <tr>
    <td>100</td>
    <td>Euleriano</td>
    <td>X</td>
  </tr>
  <tr>
    <td>1000</td>
    <td>Euleriano</td>
    <td>X</td>
  </tr>
  <tr>
    <td>10000</td>
    <td>Euleriano</td>
    <td>X</td>
  </tr>
  <tr>
    <td>100000</td>
    <td>Euleriano</td>
    <td>X</td>
  </tr>
</table>

<table class="table">
  <tr>
    <th>Vértices</th>
    <th>Tipo grafo</th>
    <th>Tempo</th>
  </tr>
  <tr>
    <td>100</td>
    <td>Semi-euleriano</td>
    <td>X</td>
  </tr>
  <tr>
    <td>1000</td>
    <td>Semi-euleriano</td>
    <td>X</td>
  </tr>
  <tr>
    <td>10000</td>
    <td>Semi-euleriano</td>
    <td>X</td>
  </tr>
  <tr>
    <td>100000</td>
    <td>Semi-euleriano</td>
    <td>X</td>
  </tr>
</table>

<table class="table">
  <tr>
    <th>Vértices</th>
    <th>Tipo grafo</th>
    <th>Tempo</th>
  </tr>
  <tr>
    <td>100</td>
    <td>Não euleriano</td>
    <td>X</td>
  </tr>
  <tr>
    <td>1000</td>
    <td>Não euleriano</td>
    <td>X</td>
  </tr>
  <tr>
    <td>10000</td>
    <td>Não euleriano</td>
    <td>X</td>
  </tr>
  <tr>
    <td>100000</td>
    <td>Não euleriano</td>
    <td>X</td>
  </tr>
</table>

</div>

--------------------
<p style="font-size: 16px"> <strong> Organização de diretórios: </strong> </p>

- `Application:` esse diretório é onde contém o código fonte da aplicação, chamada de todos os métodos para a execução, mostrando o resultado para o usuário.
- `RandomGraphs:` possui o código feito para criação de grafos de N quantidade de vértices dos tipos euleriano, semi-euleriano e não euleriano.
- `BridgeIdentification:` implementação dos métodos Naive e Tarjan.
  - `EulerianPath:` implementação do algoritmo de busca de um caminho euleriano no grafo criado.
