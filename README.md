# aFastnote - API de Anotações Rápidas

### 🚀 Uma API leve e eficiente para criar, armazenar e gerenciar suas anotações!

## 📌 Sobre o Projeto
O **aFastnote** é uma API projetada para facilitar a criação e gerenciamento de anotações de forma rápida e intuitiva. Ideal para quem precisa armazenar informações temporárias ou gerenciar notas de maneira simples e eficiente.

## 🎯 Recursos Principais
✅ Criar, editar e excluir anotações
✅ Organização por categorias e etiquetas
✅ Suporte a formatação de texto
✅ Integração com autenticação JWT
✅ API RESTful com documentação em Swagger
✅ Banco de dados otimizado

## 🏗️ Tecnologias Utilizadas
- **Linguagem**: Python
- **Framework**: Django + Django Rest Framework (DRF)
- **Banco de Dados**: PostgreSQL
- **Autenticação**: JWT (JSON Web Token)
- **Implantação**: Render
- **Documentação**: Swagger / Redoc

## 🚀 Como Rodar o Projeto

### 📥 Clonando o Repositório
```sh
git clone https://github.com/seuusuario/aFastnote-backend.git
cd aFastnote-backend
```

### 🛠 Configurando o Ambiente
Certifique-se de ter o **Python 3.9+** instalado.

```sh
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 🛠 Configurando o Banco de Dados
```sh
python manage.py migrate
```

### ▶️ Executando a API
```sh
python manage.py runserver
```
Acesse a API em: [http://localhost:8000](http://localhost:8000)

## 🔑 Autenticação
A API utiliza JWT para autenticação. Para obter um token de acesso, envie uma requisição **POST** para:
```sh
POST /api/v1/authentication/token/
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```
O token deve ser enviado no cabeçalho das requisições autenticadas:
```sh
Authorization: Bearer SEU_TOKEN
```
Para renovar o token:
```sh
POST /api/v1/authentication/token/refresh/
{
  "refresh": "SEU_REFRESH_TOKEN"
}
```

### 🔹 Criar um novo usuário
```sh
POST /api/v1/auth/register/
{
  "username": "seu_usuario",
  "password": "Sua_senha123@",
  "confirm_password": "Sua_senha123@"
}
```

## 📖 Documentação da API
Acesse a documentação interativa via Swagger:
[http://localhost:8000/api/v1/docs](http://localhost:8000/api/v1/docs)

## 📦 Endpoints Principais
### 🔹 Criar uma nova nota
```sh
POST /api/v1/notes/
{
  "title": "Minha Nota",
  "content": "Conteúdo da minha anotação",
  "tag": "trabalho"
}
```
### 🔹 Listar todas as notas
```sh
GET /api/v1/notes/
```
### 🔹 Editar uma nota
```sh
PUT /api/v1/notes/{id}/
{
  "title": "Título atualizado",
  "content": "Conteúdo atualizado",
  "tag": "nova_tag"
}
```
### 🔹 Excluir uma nota
```sh
DELETE /api/v1/notes/{id}/
```

## 🌎 Deploy
O projeto está implantado no Render. 

### 📌 Acessando a API em Produção
Acesse a API diretamente pelo link:
[https://afastnote.onrender.com](https://afastnote.onrender.com)

## 👨‍💻 Contribuição
Sinta-se à vontade para contribuir! Crie um **fork** do repositório, faça suas melhorias e envie um **pull request**. 

---
**🚀 Desenvolvido por Marcos Martins** 💻
