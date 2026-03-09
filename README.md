# Projeto de Automação de Prospecção Comercial para Serviços de Raio-X

## Visão Geral

Este projeto foi desenvolvido em Python com o objetivo de estudar e implementar automação aplicada à prospecção comercial de clientes no setor de diagnóstico por imagem, especificamente para serviços de exames de raios X.

O sistema foi criado para auxiliar na identificação de potenciais clientes, coleta de informações de contato e organização de leads comerciais. A partir dessas informações, o projeto também realiza automação de interações iniciais via WhatsApp Web.

A proposta principal foi testar, na prática, como processos repetitivos de prospecção comercial podem ser automatizados utilizando ferramentas de programação, integração com serviços externos e manipulação de dados.

Durante o desenvolvimento, o sistema foi utilizado em um contexto real de prospecção comercial voltado para empresas da área de saúde, como hospitais privados, clínicas particulares e centros médicos que potencialmente poderiam necessitar de serviços de diagnóstico por imagem.

---

# Contexto de Uso Comercial

O projeto foi pensado para apoiar atividades comerciais de uma empresa que presta serviços de diagnóstico por raios X.

O objetivo era identificar potenciais parceiros ou clientes institucionais que pudessem demandar esse tipo de serviço, como por exemplo:

- hospitais privados
- clínicas particulares
- centros médicos
- unidades de diagnóstico
- estabelecimentos de saúde especializados

Para isso, foram utilizados filtros de busca e consultas direcionadas, utilizando termos estratégicos como:

- hospital privado
- clínica particular
- centro médico
- clínica de diagnóstico
- clínica de imagem

Essas consultas permitem localizar estabelecimentos relevantes, coletar informações públicas disponíveis e organizar esses dados para posterior contato comercial.

---

# Objetivos do Projeto

O projeto foi desenvolvido com os seguintes objetivos:

- estudar automação de processos comerciais
- estruturar um fluxo simples de prospecção de clientes
- integrar coleta de dados com ferramentas externas
- organizar listas de leads para contato comercial
- testar automação de interação via WhatsApp Web
- explorar integração entre APIs, planilhas e automação de navegador

---

# Estrutura e Simplicidade de Gestão

Uma das características do projeto é sua simplicidade de gestão operacional.

O sistema não utiliza banco de dados tradicional. Em vez disso, os dados são armazenados em planilhas, o que facilita o uso e a manutenção mesmo por usuários que não possuem conhecimento técnico avançado.

Inicialmente, a base de dados foi estruturada utilizando arquivos Excel. Essa abordagem permitia um gerenciamento simples das listas de leads. No entanto, surgiram alguns problemas técnicos relacionados ao compartilhamento e atualização simultânea das planilhas.

Devido a essas limitações, foi necessário migrar o armazenamento de dados para o Google Sheets, que oferece melhor suporte para colaboração, atualização em tempo real e integração com APIs.

Essa mudança permitiu melhorar significativamente a estabilidade e a sincronização das informações utilizadas pelo sistema.

---

# Tecnologias Utilizadas

- Python
- Automação de navegador
- Integração com Google Maps API
- Integração com Google Sheets
- Manipulação de dados estruturados
- Automação de interações no WhatsApp Web

---

# Arquitetura do Projeto

O projeto foi dividido em diferentes módulos para organizar melhor as responsabilidades de cada parte do sistema.

## Estrutura dos Arquivos

### abrir_wpp.py

Responsável por iniciar e preparar o ambiente de execução do WhatsApp Web.

Esse script abre o navegador e permite que o usuário realize o login através do QR Code. Após o primeiro login, a sessão pode ser reutilizada em execuções posteriores, evitando a necessidade de escanear o QR Code repetidamente.

Principais funções:

- abrir o WhatsApp Web automaticamente
- iniciar sessão de login
- armazenar sessão autenticada para reutilização

---

### bot_envio.py

Módulo responsável pela automação do envio de mensagens para os contatos previamente identificados no processo de prospecção.

O sistema utiliza estratégias de automação que simulam comportamentos humanos e controlam intervalos de interação para reduzir a possibilidade de detecção por mecanismos automatizados de verificação de bots utilizados por plataformas como Google e WhatsApp.

Principais funções:

- envio automatizado de mensagens
- controle de fluxo de interação
- simulação de comportamento humano
- contato inicial com potenciais clientes

---

### dadosPython.py

Este módulo é responsável pelo processo de prospecção e coleta de dados de potenciais clientes.

O script realiza consultas utilizando a API do Google Maps, buscando estabelecimentos relevantes com base em palavras-chave previamente definidas.

Os resultados obtidos são organizados e enviados diretamente para uma planilha no Google Sheets, permitindo a construção de uma base de leads atualizada.

Principais funções:

- consulta automatizada na API do Google Maps
- coleta de dados de estabelecimentos
- filtragem de resultados
- envio automático das informações para o Google Sheets

---

### teste_whatsapp.py

Script destinado à realização de testes de funcionamento da automação do WhatsApp.

Ele permite validar se:

- o navegador abre corretamente
- o WhatsApp Web é carregado
- os elementos necessários para automação estão acessíveis

Esse módulo foi utilizado principalmente durante o desenvolvimento para depuração e validação do sistema.

---

### client_secret.json

Arquivo que originalmente armazena credenciais necessárias para autenticação em serviços do Google.

Essas credenciais são sensíveis e não devem ser expostas publicamente. Por esse motivo, no repositório público essas informações foram substituídas por arquivos de texto sem conteúdo real.

---

### token.pickle

Arquivo gerado automaticamente durante o processo de autenticação com serviços do Google.

Ele contém informações de autenticação que permitem manter sessões ativas entre execuções do sistema. Assim como o arquivo de credenciais, esse arquivo também contém dados sensíveis e não deve ser publicado publicamente.

Por esse motivo, no repositório os arquivos originais foram substituídos por versões neutras em formato de texto.

---

# Fluxo de Funcionamento do Sistema

O funcionamento geral do sistema segue as seguintes etapas:

1. definição de palavras-chave para busca de potenciais clientes  
2. consulta automatizada na API do Google Maps  
3. coleta de informações públicas de estabelecimentos  
4. envio dos dados para uma planilha no Google Sheets  
5. preparação da lista de contatos comerciais  
6. inicialização do WhatsApp Web  
7. login via QR Code (necessário apenas na primeira execução)  
8. execução do módulo de automação de envio de mensagens  

---

# Possíveis Evoluções do Projeto

Algumas melhorias que poderiam ser implementadas em versões futuras incluem:

- integração com banco de dados estruturado
- criação de dashboards de análise de leads
- personalização automática de mensagens
- integração com APIs oficiais de comunicação
- criação de interface gráfica para gerenciamento do sistema

---

# Considerações Finais

Este projeto foi desenvolvido com foco educacional e experimental, buscando explorar o uso de automação, coleta de dados e integração entre diferentes serviços digitais para apoiar processos comerciais.

Ele demonstra como ferramentas de programação podem ser utilizadas para estruturar e automatizar partes do processo de geração e organização de leads, especialmente em contextos onde a prospecção de clientes é uma atividade recorrente.
