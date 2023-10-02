# Aplicativo Web Multilíngue com Flask

Este é um aplicativo web multilíngue desenvolvido em Flask que oferece conteúdo em vários idiomas. Ele fornece informações sobre alimentação, cuidados, saúde e treinamento de cães.

## Recursos

- Suporte multilíngue para três idiomas: inglês (en), espanhol (es) e português (pt).
- Páginas informativas sobre alimentação, cuidados, saúde e treinamento de cães em cada idioma.
- Uso de blueprints para organizar as rotas por idioma.
- Metatags específicas para melhor otimização de mecanismos de busca (SEO).

## Pré-requisitos

Certifique-se de ter instalado o Python e as seguintes bibliotecas:

- Flask: Para criar o aplicativo web.
- Flask-WTF: Para trabalhar com formulários web.
- Gunicorn: Para servir a aplicação em produção.
- Jinja2: O mecanismo de modelo usado pelo Flask.
- Requests: Para fazer solicitações HTTP.
- WTForms: Para criar e validar formulários.

Você pode instalar essas bibliotecas usando o `pip`. Por exemplo:

```bash
pip install Flask Flask-WTF gunicorn Jinja2 requests WTForms
```

## Como Usar

1. Clone este repositório em sua máquina:

   ```bash
   git clone https://github.com/HudDavi/BSCDOGS.git
   ```

2. Navegue até a pasta do projeto:

   ```bash
   cd BSCDOGS
   ```

3. Execute o aplicativo:

   ```bash
   python app.py
   ```

4. Abra um navegador da web e acesse `http://localhost:8000` ou `http://127.0.0.1:8000` para visualizar o aplicativo em execução.

## Rotas e Idiomas

O aplicativo possui várias rotas, uma para cada idioma:

- `/` (Página inicial) - Idioma padrão (inglês).
- `/en` - Inglês.
- `/es` - Espanhol.
- `/pt` - Português.

As rotas estão configuradas para servir páginas específicas de cada idioma, usando blueprints. Você pode personalizar o conteúdo de cada página em seus respectivos arquivos de modelo.

## Metatags para SEO

As páginas deste aplicativo incluem metatags específicas para SEO, incluindo descrição e palavras-chave. Isso ajuda a melhorar a visibilidade do aplicativo nos mecanismos de busca.

## Autor

Hudson Silva

## Demo

https://bscdogs.onrender.com

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.