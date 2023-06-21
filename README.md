# WebScraper-Kabum

Webscraper de Notificação de Preços do Kabum.

O projeto consiste no desenvolvimento de um webscraper personalizado que será responsável por coletar informações de preços e valores de produtos na página do Kabum, um conhecido e-commerce de produtos eletrônicos e informática. O objetivo principal é monitorar os preços de determinados produtos e enviar notificações por e-mail caso o valor configurado seja alcançado.

O webscraper foi construído utilizando tecnologias de automação e programação, como Python e bibliotecas específicas para web scraping, como BeautifulSoup. Poderá ser configurado para acessar periodicamente a página do Kabum, realizar a extração e validação dos dados relevantes.

Além disso, o webscraper poderá ser programado em seu gerenciador de tarefas do Windows para comparar os preços coletados com um valor previamente configurado. Caso o preço de algum produto seja igual ou inferior ao valor configurado, o sistema disparará automaticamente um e-mail de notificação para o usuário responsável, contendo as informações relevantes do produto, como nome, preço e link direto para a página do Kabum.

# Como utilizar:

  1. Em URL, adicione o link da página do produto do site da Kabum que te interessa entre as '' como no exemplo:
   
![image](https://github.com/joaomalonso/WebScraper-Kabum/assets/133373441/4a13a786-95db-43c1-8f47-4de7bf750044)
  
  2. Adicione após o '<' o valor do produto que te interessa de forma inteira como no exemplo da imagem:
     
![image](https://github.com/joaomalonso/WebScraper-Kabum/assets/133373441/6b5e0f15-693e-4747-b341-c7d26f482679)

  3. Adicione seu e-mail no local mencionado para que possa receber a notificação caso o produto fique com valor igual ou menor do que o valor configurado:

![image](https://github.com/joaomalonso/WebScraper-Kabum/assets/133373441/1883660c-cd19-48a4-ad57-0b1aa636bc94)

Obs: Para envio automático dos e-mails baseado em um tempo determinado, é necessário adicionar o programa ao agendador de tarefas do seu sistema operacional. 

# Resultado do programa:

![image](https://github.com/joaomalonso/WebScraper-Kabum/assets/133373441/404f759b-21b2-4830-945e-7417a5cf333f)

# Conclusão:


Esse webscraper personalizado proporcionará ao usuário a comodidade de monitorar os preços de produtos no Kabum sem a necessidade de verificar manualmente o site regularmente. Ao receber uma notificação por e-mail, o usuário poderá aproveitar oportunidades de compra com preços mais baixos, garantindo economia e praticidade.

É importante ressaltar que o uso do webscraper deve estar de acordo com os termos de serviço e políticas de privacidade do Kabum. É recomendado configurar o webscraper para realizar as requisições de forma responsável, respeitando limites de acesso e intervalos adequados para evitar sobrecarga nos servidores do Kabum e possíveis bloqueios de acesso.
