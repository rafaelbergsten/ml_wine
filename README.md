# API de embrapa

Esta API foi desenvolvida em Flask para coletar dados de vitibrasil do site da Embrapa, incluindo informações sobre produção, processamento, comercialização, importação e exportação de vinhos.

## Índice

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Plano de Arquitetura](#plano-de-arquitetura)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Pré-requisitos

Antes de iniciar, certifique-se de ter os seguintes componentes instalados:

- Python 3.12 ou superior
- Pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado)

## Instalação

1. **Clone o repositório** para o seu ambiente local:
   ```bash
   git clone https://github.com/rafaelbergsten/ml_wine.git
   cd ml_wine
   ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
   ```

3. **Instale as dependências** listadas no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Configuração

1. **Configuração das Variáveis de Ambiente:**

   Crie um arquivo `.env` na raiz do projeto e adicione as variáveis necessárias:

   ```plaintext
   EMBRAPA_URL_PRODUCAO=https://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01
   EMBRAPA_URL_PROCESSAMENTO=https://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02
   EMBRAPA_URL_COMERCIALIZACAO=https://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03
   EMBRAPA_URL_IMPORTACAO=https://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04
   EMBRAPA_URL_EXPORTACAO=https://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05
   JWT_SECRET_KEY=your_jwt_secret_key
   ```

2. **Geração de Tokens JWT:**

   Use o script `generate.py` para gerar um token JWT se necessário:
   ```bash
   python generate.py
   ```

## Uso

1. **Inicie a aplicação Flask**:
   ```bash
   python app.py
   ```

2. **Acessando os Endpoints**:

   - Produção: `GET /api/producao`
   - Processamento: `GET /api/processamento`
   - Comercialização: `GET /api/comercializacao`
   - Importação: `GET /api/importacao`
   - Exportação: `GET /api/exportacao`

   **Exemplo de Requisição com Postman:**
   - Defina o cabeçalho `Authorization` com o valor `Bearer <seu_token_jwt>` para acessar os endpoints protegidos.

## Estrutura do Projeto

- **app.py**: Arquivo principal da aplicação Flask.
- **generate.py**: Script para gerar tokens JWT.
- **requirements.txt**: Lista de dependências do projeto.
- **.env**: Arquivo contendo as variáveis de ambiente (não incluído no repositório).
- **.gitignore**: Arquivo para definir os arquivos e diretórios que devem ser ignorados pelo Git.

## Plano de Arquitetura

O plano de arquitetura do projeto pode ser encontrado [aqui](ARCHITECTURE.md), detalhando as camadas, componentes, e tecnologias usadas no desenvolvimento da API.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.