# atv3-07-12-2024-GT
Atividade 3 referente ao dia 07/12/2024


Questão com método POST :

Crie um app com base nas instruções abaixo:

Usem extensões de um modelo HTML base, que será replicado em todas as páginas. Esse
modelo HTML deverá ter uma tag <nav> na parte superior que fará com que o usuário possa
navegar entre as rotas inicio.html e fazer_pedido.html mencionadas abaixo.
inicio.html - Mostre uma tela inicial com a apresentação de uma pizzaria genérica, no corpo
do seu html deverá ter um botão que levará o usuário para uma nova rota onde ele poderá
fazer um novo pedido.

fazer_pedido.html – Abra um formulário com vários tipos de ingredientes que o usuário
pode escolher na pizza, por exemplo:

Tipo de massa: Massa normal, Massa com queijo, Massa com carvão (Sim, isso existe).
Molho: Molho de tomate, molho branco, sem molho
Ingrediente 1: Queijo mussarela, Queijo prato, queijo cheddar
Ingrediente 2: Calabresa, Peperoni, Lombinho suíno
Ingrediente 3: Catupiry, Requeijão, Ricota
Ingrediente 4: Frango desfiado, Bacon
Borda recheada: Cheddar, Caputiry, Sem recheio

A sua página HTML também deve pedir ao usuário o endereço para o envio da pizza.
Ainda na página de fazer_pedido, você deve criar um botão para confirmar o pedido e isso
levará o usuário para uma outra rota que terá a seguinte mensagem na tela:

Confirmação.html – Exiba a seguinte mensagem com as informações que o usuário te
passou no formulário de pedido:

“Obrigado pelo seu pedido!
Sua pizza com:
{{massa}}
{{molho}}
{{ingrediente1}}
{{ingrediente2}}
{{ingrediente3}}
{{ingrediente4}}
{{borda}}
Será entregue no endereço: {{endereço}} em aproximadamente 40 minutos!”

Coloque também um botão para encaminhar o usuário para a rota inicio.html