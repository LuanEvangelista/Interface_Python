# Interface com Python
Este código cria uma aplicação com duas janelas utilizando a biblioteca PySimpleGUI. A primeira janela é uma tela de login, onde o usuário pode inserir seu nome. A segunda janela é uma tela de pedidos, onde o usuário pode selecionar o que deseja pedir (pizza ou coxinha).

## Funções

<ul>
    <li> 'janela_login' : cria a primeira janela, com um campo de texto para o usuário inserir seu nome e um botão para continuar.</li>
    <li> 'janela_pedido' : cria a segunda janela, com duas opções de checkbox para escolher o que pedir e dois botões para voltar ou fazer o pedido.</li>
    
</ul>

## Loop de leitura de eventos
O código possui um loop de leitura de eventos que verifica as ações do usuário nas janelas. Quando o usuário clica no botão "continuar" na primeira janela, a segunda janela é exibida e a primeira janela é escondida. Quando o usuário clica no botão "voltar" na segunda janela, a segunda janela é escondida e a primeira janela é exibida. Quando o usuário clica no botão "fazer pedido" na segunda janela, uma mensagem de confirmação é exibida, mostrando o que foi pedido.

## Requisitos
<ul>
    <li> PySimpleGUI</li>
</ul>

## Extra
Este código pode ser utilizado como base para desenvolver aplicações mais complexas com janelas interativas.
## Saida
![1](https://user-images.githubusercontent.com/82175827/144887876-91bd62bb-9303-4814-9057-a17b5f940be9.PNG)
![2](https://user-images.githubusercontent.com/82175827/144887878-b96bbc67-6162-4120-8d0f-27009c2c7c2c.PNG)
![3](https://user-images.githubusercontent.com/82175827/144887880-313eac5c-2404-43a1-99c4-155c4e38b2ce.PNG)
