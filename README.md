# ine5404-aula20-out-2020
Aplicação de cadastro de clientes com o padrão MVC.
O sistema possui uma camada de persistência que usa uma classe **Data Access Object (DAO)**.

- **simple**: cadastra, remove e lista clientes
- **intermediate**: simple + funcionalidades de exportação e importação

A versão intermediate possui duas variantes. Uma delas é baseada em uma View base para as janelas. Views especializadas herdam dessa View base e especializam os métodos de visualização caso necessário.
