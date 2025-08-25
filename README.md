# BPG Brasil

Repositório para o projeto do desenvolvimento do site do Boletim Paranaense de Geociências (BPG).

## Sobre o projeto

O projeto visa a reformulação completa do design, funcionalidades e otimização de hospedagem do website oficial do BPG, com o intuito de profissionalizar o principal canal digital do coletivo.

Esta nova versão do projeto utiliza o framework **Django** para o backend, permitindo o gerenciamento dinâmico de conteúdo, como artigos, editores e destaques, através de um painel de administração.

## Ferramentas Utilizadas

  * **Frontend:** HTML, CSS, JavaScript
  * **Backend:** Python, Django
  * **Banco de Dados (Desenvolvimento):** SQLite3
  * **Ferramentas de Design:** Figma
  * **Sistema de Versionamento:** Git / GitHub

## Começando: Configuração do Ambiente de Desenvolvimento

Para rodar este projeto localmente, siga os passos abaixo.

### 1\. Pré-requisitos

  * **Python 3.10+:** [Baixe aqui](https://www.python.org/downloads/). Durante a instalação no Windows, marque a opção "Add Python to PATH".
  * **Git:** [Baixe aqui](https://git-scm.com/downloads).

### 2\. Clone o Repositório

Abra seu terminal, navegue até a pasta onde deseja salvar o projeto e clone o repositório:

```bash
git clone https://github.com/seu-usuario/bpg-brasil.git
cd bpg-brasil
```

### 3\. Crie e Ative o Ambiente Virtual (`venv`)

É crucial usar um ambiente virtual para isolar as dependências do projeto.

```bash
# Crie o ambiente virtual (só precisa fazer isso uma vez)
python -m venv venv

# Ative o ambiente virtual (faça isso toda vez que for trabalhar no projeto)
# No Windows:
.\venv\Scripts\activate
# No Mac/Linux:
source venv/bin/activate
```

Você saberá que funcionou quando vir `(venv)` no início do seu terminal.

### 4\. Instale as Dependências

Crie um arquivo `requirements.txt` para que outros possam instalar as mesmas dependências que você.

**Para o dono do projeto (faça isso uma vez antes de commitar):**

```bash
pip freeze > requirements.txt
```

**Para todos os outros (e para o dono, depois de clonar):**
Instale todas as bibliotecas necessárias com um único comando:

```bash
pip install -r requirements.txt
```

### 5\. Configure as Variáveis de Ambiente (`.env`)

Por segurança, informações sensíveis como a `SECRET_KEY` não são salvas no repositório.

1.  Na raiz do projeto, crie uma cópia do arquivo `.env.example` e renomeie para `.env`.

2.  Abra o arquivo `.env` e preencha com uma nova chave secreta do Django. Você pode gerar uma nova chave [neste site](https://djecrety.ir/).

    ```
    # Exemplo de conteúdo para o arquivo .env
    SECRET_KEY='sua-nova-chave-secreta-gerada-aqui'
    ```

### 6\. Configure o Banco de Dados

O Django precisa criar o banco de dados e as tabelas iniciais.

```bash
python manage.py migrate
```

### 7\. Crie um Superusuário

Você precisa de um login de administrador para acessar o painel de controle.

```bash
python manage.py createsuperuser
```

Siga as instruções para criar seu nome de usuário, email e senha.

## Como Rodar o Projeto

1.  Certifique-se de que seu ambiente virtual (`venv`) está ativado.

2.  Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

3.  Abra seu navegador e acesse os seguintes endereços:

      * **Site Principal:** `http://127.0.0.1:8000/` (eventualmente, quando as views forem criadas)
      * **Painel de Administração:** `http://127.0.0.1:8000/admin/`

Faça login no painel de administração com o superusuário que você criou para gerenciar o conteúdo do site.
