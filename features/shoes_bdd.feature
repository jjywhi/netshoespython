Feature: Compra de Tênis na Netshoes

 Scenario: Pesquisar e comprar um tênis
    Given que eu acesso o site da Netshoes
    When eu localizo a barra de pesquisa
    And eu digito "tênis" e pressiono Enter
    Then a página de resultados exibe uma lista de tênis disponíveis

    Given que eu estou na página de resultados de tênis
    When eu escolho um tênis da lista de resultados
    Then a página de detalhes do tênis é carregada

    Given que eu estou na página de detalhes do tênis
    When eu seleciono um tamanho
    And eu clico no botão "Comprar"
    Then que eu vejo o  tênis ao carrinho
    
   
    
    