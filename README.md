<h1> Trabalho Grafos </h1>

> **Status do Projeto:** Em desenvolvimento ⚠️

O intuito desse trabalho prático é criar dois métodos para indentificação de pontes. Pontes são arestas cuja a remoção torna o grafo desconexo. Dentre as aplicações de indentificações de pontes está encontrar os caminhos ou ciclos eurelianos em diferentes grafos, sendo os métodos de identificação de pontes e suas respectivos diretórios:
- [Método Naive](LINK_METODO_NAIVE)
- [Método de Tarjan (1974)](LINK_METODO_TARJAN)

Além dos métodos descritos acima a implementação deverá encontrar um caminho euleriano em um grafo qualquer ou determinar que ele não existe utilizando o seguinte método:
- [Método de Fleury](LINK_METODO_FLEURY)

Alguns experimentos devem ser realizados em apenas uma máquina para avaliar o tempo gasto para as duas estrátegias de identificação de pontes em grafos aleatórios, sendo os grafos eulerianos, semi-eulerianos e não eulerianos contendo 100, 1000, 10000, 100000 vértices para cada tipo de grafo.
- [Código Python - Criação grafos aleatórios](https://github.com/zTrolly/trabalho-grafos/blob/main/Random%20graphs/random_graph.py)
- [Agoritmo e explicação de cada grafo](https://github.com/zTrolly/trabalho-grafos/blob/main/Random%20graphs/README.md)

--------------------
<p style="font-size: 16px"> <strong> Resultado avaliação - tempo médio: </strong> </p>

Todos os experimentos foram realizados em uma máquina com 16GB de memória RAM 4666MHz, com uma CPU i7-11600K - 4.3GHz, com SSD. Essas especificações de máquina podem ser alteradas.


<style> 
.table-responsive{
  width: 100% !important;
}

.table {
    border: 1px solid white;
    width: 50% !important;
    margin: auto;
    margin-top: 5px;
}
</style>
<div class="table-responsive">

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
