A aplicação foi codificada em Python 3.

São 10 classes responsáveis por realizar a coleta, construção e parsing dos dados da página de feed.
Foi utilizado o padrão de projeto Factory, por se tratar de uma construção complexa do objeto Feed.

Instale os módulos abaixo:

```
sudo apt-get install python3-pip
sudo apt-get install curl

sudo pip3 install Flask-API
sudo pip3 install Flask-Httpauth
sudo pip3 install beautifulsoup4
```

Para executar o crawler, utilize, na linha de comando, o codigo abaixo :
```
python3 crawler.py
```

Implementei uma aplicação flask simples, para poder realizar o desafio extra
Para rodar o webservice execute:

```
python3 app.py
```

app.py implementa uma autenticação básica, mas a biblioteca flask permite implementar também autenticação por token e oauth, por exemplo.

Por uma questão de praticidade, os usuarios e senhas estão armazenados em um array na própria aplicação, mas uma autenticação factivel ocorreria com uma consulta ao banco de dados (usando db.Model, por exemplo) e a implementação das devidas políticas de segurança, como hashing de senha e autenticação em duas etapas por exemplo.

Os usuários e suas respectivas senhas são:

"globo": "globo",
"danny": "farias",
"alexandre": "prates",
"andreia": "almeida"

Com app.py em execução em outra aba do terminal, podemos realizar uma chamada curl para simular um http request:

```
curl --user globo:globo http://127.0.0.1:5000/
```





