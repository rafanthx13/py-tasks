

# My-Notes-Scrapy

## Log

- **Data de Inicio**: 17/05/2018
- **Data de Fim**: 
- **Site Udemy**: https://www.udemy.com/python-com-scrapy/learn/v4
- **Avaliação:** 

## Conteúdo do curso



## Introdução



Estilo de Codificação Oficial do Python (PEP8):

+ https://www.python.org/dev/peps/pep-0008/

virtualenv





## virtualenv

+ Serve para criar ambiente de python, o mesmo que o anacnoda fazia
+ instalar: `pip install virtualenv`
+ criar ambiente: `virtualenv nome_ambiente`
  + Essa pasta fica dentro do Home, você, pelo terminal acessa a pasta `/Scripts` dentro dela, vai ter o arquivo activate: executando `activate` **você vai ativar o ambietne, e vai apareecr a tag no cmd**
+ OBS: Esse ambiente virtaul não interfere no global, e dentro de seu ambiente virtaul, você pode instalar as coisas que não vai atrapalhar





## jupyter

+ Cria um servidor sobre a biblioteca chamada tornado, em que cria um servidor web na máquina que lê o código e vai mostrar ele  oor javascript
+ `ESC+D+D`





## 1. Outras opções sem ser Scrapy

Outras alternaticvas: `request` `beatifulSoup`

### Lib Request

+ Faz requisição HTTP
+ http://docs.python-requests.org/en/master/
+ 

### Lib Beautiful Soup

+ Analisar o HTML
+ https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Exemplo de código:

````python
# Importando bibliotecas
import requests
from bs4 import BeautifulSoup

# REQUEST
# com'request' você acessa as paginas e pega seu conteudo (CTRL+U)
response = requests.get('http://www.gilenofilho.com.br/') # se deter erro, tente com (@verify = False), ele verifica por SSL válida, se der problema, dessa forma, não vai verificar esse item de segurança. Torna menos seguro, mas vai mais rapido

if(response.status_code != 200): # se for difereten de 200, quer dizer que deu problema
    quit()
print(response.text) # texto da pagina em forma de string

# BEAUTIFUL-SOUP: Serve para fazer a busca sobre o response.text
soup = BeautifulSoup(response.text, 'html.parser') # outro parser: html5lib
links = soup.find_all('h3', attrs={'class': 'ctitle'})
# find_all retornar um iteradao, o find (normal) retorna a tag se a achar
for l in links:
    print(l.a) # ao fazer '.a' vai buscar pela tag a que esta dentro de l, se nao hovuer, error
    print(l.a['href']) # usando [] você busca pelo atributo da tag
    print(l.get_text()) # usando get_text() você retira o conteudo, sem isso, todas as opçoes 
    	#retornam a tag com seu dado, usando-a você pega o dado direto
    print(l.span.extract()) # com extract, você tirar 'span' do l, isso é feito na hora, e, retorna o span. Voce pode usar isos para retirar tags internas ou buscar alguma especifica

````



## 2. Scrapy Intro

+ \\scrépai
+ A ideia é evitar todo o trabalho do Request/BeautifulSoup, é tornar o código extensível e tem a vantagem de **acessa as páginas de forma assíncrona/paralelo**.
  + Tambem você ja fica com um modelo para reuso
  + Vantagens:
    + Reuso, manutenção, organizaçãp
    + Tem uma arqutiteura boa para ter alta coesão e baixo acoplamentp
    + Estutura seu projeot de web-crawling de forma que pode rodar ele na nuvem (como se fosse algo global)

##### Arquitetura do Scrapy

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-scrapy-web-scraping\imgs\img01.png)
1. **Spiders** são as classes, elas decidem o que fazr
2.  **Sheduler**: O agendador, idnica a frequencia e configurações para baixar (quantas vezes tentar, o número máximo e etc)
3. **Dowloader Middlewares:** Acessar/Baixaapágina da internet e volta por **callback**: quando retornar (não se sabe quando, ams sabse- que uma hora vai) então executa algo
4. **Item Pipeline**: Decide o que fazer com os dados, acessar baco, rodar um web Service e etc

##### Instalar

`pip install scrapy`. é recomendado criar um ambiente para executar ele


##### Primeira Spider

````python
import scrapy

# sao filhas de scrapy.Spider
class GilenoSpider(scrapy.Spider):

	# Toda Spyder tem que ter um 'name'
	name = 'gilenofilho'
    
	# start_urls : Quando tem, recebe uma lsita de urls que ira acessar
	# se tem , entoa vai acesssar ess pagina
	start_urls = ['http://www.gilenofilho.com.br']

	# por default, ao acessar executa 'parse', e tem o retorno do callback
	def parse(self, response):
		# log serve para imprimir no terminal
		self.log('Hello World') # serve pra printar soemnte na tela
        # 2018-05-31 21:38:10 [gilenofilho] DEBUG: Hello World
		self.log(response.body) # imprimir a repsosa: body e outras info
        # 2018-05-31 21:38:10 [gilenofilho] DEBUG: b'<!DOCTYPE html>\n<html 
        # xmlns="http://www.w3.org/1999/xhtml"\n ....
     
# executa no terminal:
# scrapy runspider 01_first_scrapy.py
````

## 3. Estururando um projeto

Criando um projeto Scrapy

`scrapy startproject [nome_do_projeto]`

  + Assim já cria e separa os arquivos, a 4 partes vistas na figura
  + **OBS:** Ao fazer isso, os proximos comandos tem que ser dentro da pasta do projeto, como no git
  + **ALGUNS COMANDOS SO VAO FUNCIONAR NA PASTA PRINCIPAL DO PROJETO**

Criando uma Spyder no projeto

`scrapy genspider [nome_da_spyder] [url_http]`

+ Cria praticamente o código anterior, com o nome e a url

Executando Spyde

`scrapy crawl [nome_spyder]`

+ Busca da pasta que tem todas as Spdrr a spyder com esse nome

##### Pastas

/[nome_projeto_do_start_project]

+ scrapy.cfg : Arquivo de configuração
+ [name_project]/
  + `__init__.py`
  + `items.py`
  + `middlewares.py`
  + `pipelines.py`
  + `settings.py`
  + spiders/
    + `__init__.py`
    + genspider criadas

##### Executando `genspyder`

Executando

`scrapy genspider coursera_course http://www.coursera.org/browse?languages=pt`

Vai gerar

````python
import scrapy


class CourseraCourseSpider(scrapy.Spider):
    name = 'coursera_course'
    allowed_domains = ['http://www.coursera.org/browse?languages=pt']
    start_urls = ['http://http://www.coursera.org/browse?languages=pt/']

    def parse(self, response):
        pass
````

## XPATH (linguagem de Query do HTML)

+ Forma de navegar pela pagina HTML, atravez das Tags. Essa é uma alternativa, mas você tambem pode usar o beautifulSoup/RegeEx para pegar tambem
+ No curso, usará o XPATH pois ele é o padrao para o Scrapy
+ Em geral, o XPATH será pela class CSS da TAG

##### XPATH

+ Busca em forma de arvore
+ ``//``: Quaquer ramo; Pule quaisquer niveis
+ `*` : Qualquer tag
+ `text()`: retorna o texto. isso é do XPHAT. Exemplo: `return div.xpath('./text()')`. Pega somente o conteudo textual
+ `/@href:` pegar conteudo do atributo da tag HTML
+ `.//img[contains(@class, "img-responsive")]/@src ` : busca a tag `img` e filtra por class que seja 'img-responsive'
+ `.`: O ponto é para pegar apartirr do ultimo `xpath()` feito
+ **OBS:** Se um dado pode variar, coloque emm um `for`

###### Exemplo

`.//h3/a` : baseado no xpath anterior ".", pule quaisuer nivies desde que encontre a tag h3 e quando achala pegue a tag `a`

+ https://br.udacity.com/courses/all





###### Scrapy shell

+ A partir desse recurso, voce pode carregar a pagina e depois, a partir do IPython, manipulala de forma iterativa (Semelhante ao jupyer, so que direto com os dados da pagina)
+ **A INDEXAÇÃO EM XPATH COMEÇA DO 1. [1] SIGNIFICA 1°**
+ O Xpath voce tira pelo google crhome, mas, se voce tirar alguns atributos da tag. O chrome arruma outra forma de te entregar o mesmo XPATH sem o elemento retirado

`scrapy shell [url]`

+ `response.xpath('string_xpath_do_F12_Chrome')`
+ `.extract()`
+ `.extract_first()`



###### Passos executados

`scrapy shell https://br.udacity.com/courses/all`

`response`: Vê a resposa do scrapy

`div = response.xpaht('//*[@id="ud860"]')`

`div.extract()`: Extrai o conteudo html interno dela



### 3. `yield` Python

+ A palavra reservada `yield` cria um generator, com ele, os valores serãolidos sobre demando (preguiçoso). Serve para `for ... in` não é como uma lista/dict/tuple já construida, pois, ele verifica os valiores memso a medida que for sendo pesquisado

+ Vantagem:

  + **É COMO SE FOSSE EXECUTADO PARCIALEMNTE**
  + **SCRAPY É ASSINCRONO, POR ISSO É IMPORATNE SABER ISSO, POIS, PERCEBA ENTÃO QUE NÂO PREISA TER TUDO COMPLETO, A MEDIA QUE FOR APARECENDO (PROMISSE) VAI EXECUTANDO** 
  + É como uma lsita, lida um por um, sob medida, como se entrega-se elemento pro elemento asism que é presiso (Lazy)
  + Ao invez de executar toda a sequencia, ele meio que **retorna um yeild**, deixa marcado onde paraou e depois joga o outro **yeild**

  Exemplo

  ````python
  def list_cars():
  	yield 'ford'
      print('yield 1')
      yield 'honda'
      print('yield 2')
      yield 'hyundai'
      print('yield 3')
      
  # Vendo seu retorno
  print(list_cars) # retorna ==> <generator object list_cars at ....>
  
  # executando
  for car in list_cars():
      print(car)
  '''
  Vai ser imprimido
  ford
  yield 1
  honda
  yield 2
  hyundai
  yield 3
  '''
  
  # perceba  a parte preguiçosa.
  # 1. Ele buscou o primiero yield, pra fazer isso, ele executou a funçao
  	# mas, nao imprimiu as outras coisas, ele parou no 1° yield
  # 2. Qundo foi buscar o segundo,  yeld, continouo de onde parou, leu o 
  	# print('yield 1) , imprimiu e depois retornou o 2 yield 'honda'
  ````

### 4. Spider Que faz request

Spider_course (vendo o Yield)

````python
import scrapy


class UdacitySpider(scrapy.Spider):

    name = "udacity"
    start_urls = ['https://br.udacity.com/courses/all/']

    # Faz um callback
    def parse(self, response):
        divs = response.xpath("/html/body/div[1]/div/div[2]/div[2]/div[1]/div")
        for div in divs:
            link = div.xpath('.//h3/a')
            href = link.xpath('./@href').extract_first()
            # Retorna um Yield
            # vai fazer uma nova requisçao, a 'url'
            # e quando voltar, vai executar o parse_detail
            yield scrapy.Request(
                url='https://br.udacity.com%s' % href,
                callback=self.parse_detail
            )

    # Aplicado para cada pagina de instutor
    def parse_detail(self, response):
        title = response.xpath('//title/text()').extract_first()
        headline = response.xpath(
            '//h2[contains(@class, "course-header-subtitle")]/text()'
        ).extract_first()
        image = response.xpath(
            '/html/body/div[1]/div[2]/div/div/div/div[2]/div[2]/div[1]/img/@src'
        ).extract_first()
        instructors = []
        for div in response.xpath('//div[contains(@class, "instructor-information-entry")]'):
            instructors.append(
                {
                    'name': div.xpath('.//h3//span/text()').extract_first(),
                    'image': div.xpath('.//img/@src').extract_first(),
                }
            )
        yield {
            'title': title,
            'headline': headline,
            'image': image,
            'instructors': instructors,
        }
````





## Projeto olx

`scrapy starproject olx`

`cd olx`

`scrapy genspider cars pe.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios`

`scrapy crawl cars`



Usando `scrapy shell https://pe.olx.com.br/grande-recife/autos-e-pecas/carros-vans-e-utilitarios/gol-trend-1-0-pra-vende-logo-495428198`

Vai aparecer umonte de coisa, ma no final tera tipo um prompt do Jupyer, agora da pra fazer iterativo

**É bom usar o scrapy shell para conhecer o ambiente do site para depois gerar o spider**

````
# voce atual sobre 'response'

In [1]: response
Out[1]: <200 https://pe.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios>

In [8]: response.xpath('//title/text()').extract_first() # requisitando direto pelo shell
Out[8]: 'VW - VOLKSWAGEN GOL 1.0 TREND/ POWER 8V 4P 2013 - 495428198 | OLX'

# pegar Span em que seu conteudo interno seja Ano
In [14]: response.xpath("//span[contains(text(), 'Ano')]")
Out[14]: [<Selector xpath="//span[contains(text(), 'Ano')]" data='<span class="term">Ano:</span>'>]

# Buscar tag strong que esteja na frente da de ano, bucar sua tag <a> e retirar do atributo title o seu texto. Temos entao o ano do carro
In [16]: response.xpath("//span[contains(text(), 'Ano')]/following-sibling::strong/a/@title").extract_first()
Out[16]: '2013'



````

Um conselho para resolver paginação, qnd nao se sabe o número, é seguir o 'Next Page' analisar sua url e dpeois executalo



Sem extract_first voce vai pegar a tag

com extract first, voce vai pegar o conteudo



### Item Pipilne 

Classe que implementa os 4 métodos abaixos para processamento dos dados e tambem sua externalizaçâo;

Serve para: Processar o item e salvalo no bangco

Quando voce cria `starproject` ele deixa essa classe no arquivo `pipelines.py`. Apesar disos, ele nâo está ativado. Para isso voce deve ativalo em `setting.py` para direcionar para esse arquivo.



Em setting temos isso, onde é um dic onde:

	index => local onde está a calsse

	value => ordençao, quanto menor, vai buscar primeira (isso serve quando voce tem vários)

````python
# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'olx.pipelines.OlxPipeline': 300,
}
````











![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-scrapy-web-scraping\imgs\img02.png)



Quando agente retorna um didiconario, ele entende isso como item

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-scrapy-web-scraping\imgs\img03.png)

Quando a Psider é ativada

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-scrapy-web-scraping\imgs\img04.png)

Quando a Spider é fechada

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-scrapy-web-scraping\imgs\img05.png)

Quando ele inicializa todo o crawler



### Scrapy Shell

`scrapy shell url`

reotrna um response

(.//span[conains(@class, "domain-name")]/text()).extract_first()



# Add

## Fazer requisição ede acordo com local

`scrapy shell`

em sequida faz

`form scrapy import Request`

`req = Request('https//www.coursera.org/browse?languages=pt', headres = {"Accept-Language" : "pr-br"})`

`fetch(req)` # pegat essa requisiçâo e por de vlta no scrapy, agora, vai fazer com esse idioma

Essa parte de Acapet Langugeuse tambem tem no `settings.py`

depois de esquetutar isso, vai voltar para `response`

````
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'pt-br',
}
````

#### Argumetnos na linha de comando

+ Colocar `-a` em seguida `nome-da-variavel = valor`
+ `scrapy crawl coursera -a category=computer-science`

###### `start_requests()`

+ Esse método é sempre executado
+ Ele já está implementando e por padrâo ele chama `start_url` e executa sua url
+ Porém, podemos sobreecrevelo para **Definir as urls iniciais**
  + Assim, vamos colcoar para que seja de acordo com o argumento passado
  + Segue o código para ``scrapy crawl coursera -a category=computer-science``

````python
import scrapy


class CourseraSpider(scrapy.Spider):

    name = "coursera"
    start_urls = ['https://www.coursera.org/browse?languages=pt']

    category = None # vai ser passado por arg na command_line

    def start_requests(self):
        if self.category is None: # se nao ha nada, executa tudo
            yield scrapy.Request(
                url='https://www.coursera.org/browse?languages=pt',
                callback=self.parse
            )
        else: # executa somente com aquilo que queremos
            yield scrapy.Request(
                url='https://www.coursera.org/browse/%s' % self.category,
                callback=self.parse_category
            )

    def parse(self, response):
        self.log('here')
        categories = response.xpath("//div[contains(@class, 'rc-DomainNav')]/a")
        for cat in categories:
            cat_url = cat.xpath('./@href').extract_first()
            self.log('Category: %s' % cat_url)
            yield scrapy.Request(
                url='https://www.coursera.org%s' % cat_url,
                callback=self.parse_category
            )
    
    def parse_category(self, response):
        self.log(response.xpath("//title/text()").extract_first())
````

#### Item e ItemLoad

+ Até esse momento no curso, o que retornávemos era um dicionário, e, o scrapy entendia ele como item. Agora vamos fazer isso de forma mais elaborada dentro de `items.py`

````python
# items.py
# Craindo um item
class CourseItem(scrapy.Item):
    title = scrapy.Field()
    headline = scrapy.Field()
    url = scrapy.Field()
    instructors = scrapy.Field()
    lectures = scrapy.Field()
    image = scrapy.Field()
````

+ Esse `ITEM`  **Funciona como um dicionario para isnerir os campos**
+ No shell voce pode charma da seguinte forma:
  + `from nome-project.items import AddItem`
  + `item = AddItem(0)`
  + `item['title'] = response.xpath.....`

#### Item loader

+ Nele é uma forma de carregar um item
+ Pode parecer estranho, mas, isso serve pra quando voce tem spider muito grandes, aí, esse tipo de organização será necessário
+ Exemplo no SHELL

![](C:\Users\Rafael\Google Drive\Private Studies\Computer Advanced\udemy-scrapy-web-scraping\imgs\img06.png)

+ Esse `processor` e `take_firsdt` é a forma de pegar o dado. Perceba que, nao usamos `extract_first` quando passamos o xpath. Mas, fará extract_first por que definimos o `default` como `TakeFirst`
+ Vantagem: Voce separa bem as coisas, entao, quando der um erro, você vai saber onde ir

#### Projeto Veduca

`scrapy genspider veduca veduca.org`



#### Item Loader, criando um customisado

+ Ele especifica o tratamento e forma de pegar os dados

+ class VeducaItemLoader(ItemLoader):

      

  ```python
  class VeducaItemLoader(ItemLoader):
      
      default_output_processor = TakeFirst()
  
      # str.strip = remove exccesos de espaço em branco
      # remove_tags = vem de w3lib, serve pra tirar tags html se tiver
      # MapMompose = aplicar varias funções
      instructors_description_in = MapCompose(remove_tags, str.strip)
  ```

### Coisas HTTP - Cookies

+ Meta dados que ficam no seu broser ao navegar pela web
+ A partir de sua manipulaçâo, podemos então imitar uma navegaçâo humana

##### Trabalhar com Form (Em vez de GET , fazer um POST para logar no site)

+ Erro 403 : É erro de segurança, em geral por alguma burocracia do servidor. Quando ocorre, em geral, quer dizer que é a falta de algum token de segurança
+ entaô: basta conseguir entrar com login, colocando dados na requisiçâ (Ou ela é POST, ou voce poe no seu HEEDAER)
+ A forma de colocar isso para cada site varia muito
  + É necessairo fazer muito `F12` No google chrome pra saver na parte de netwrok, das requisiçôes HTTP, qual é o campo que passa o token, 

````python
import scrapy

from courses import settings


class EdxLoginSpider(scrapy.Spider):
    
    name = 'edx_login'
    allowed_domains = ['courses.edx.org', 'edx.org']
    start_urls = [
        'https://courses.edx.org/login?next=/dashboard'
    ]

    def parse(self, response):
        # dadosque serao passado pelo formulario
        formdata = {
            # seting. ==> sao variaveis criadas dentro de settit
            'email': settings.EDX_EMAIL,
            'password': settings.EDX_PASSWORD,
        }
        headers = {}
        # quando requisitar a pagina de dash, vai voltar um token criado pelo
        # servidor, ele vai ficar no cooie, agora vamos pegar isso
        cookies = response.headers.getlist('Set-Cookie')
        #depois vamos procurar no que retonra (retonara uma lsita, e ,a gnt nao sabe em qual delas esta)
        # vamos achar e dividir em 2 partes e pegar a 2 parte
        # obs: cookies sao dividios por COOKIE: key=value;key2=value2;
        csrf_token = ''
        for cookie in cookies:
            cookie = cookie.decode('utf-8')
            if 'csrf' in cookie:
                csrf_token = cookie.split(';')[0].split('=')[1]
                break
        self.log(csrf_token)
        # Coloca esse token e ja o prepara para fazer a quisicao POST
        headers['X-CSRFToken'] = csrf_token
        # Por via das duvidas, vamos pasar tambem outro dado CTE para nao ter problema
        headers['X-Requested-With'] = 'XMLHttpRequest'
        yield scrapy.FormRequest(
            url='https://courses.edx.org/user_api/v1/account/login_session/',
            method='POST', formdata=formdata, callback=self.parse_login,
            headers=headers
        )

    def parse_login(self, response):
        yield scrapy.Request(
            url='https://courses.edx.org/dashboard',
            callback=self.parse_dashboard
        )
    
    def parse_dashboard(self, response):
        self.log(response.xpath('//title/text()').extract_first())
````

#### Outras opçoes quando tem muito JS

+ Selenium
  + O scrapy é umpocuo complicado jutnalo com 
+ Splash
  + O Splash presisa do Dcokeer, mas, se o seu PC for Windowas 10 home, voce nao consegue o docekr original mesmo
  + Entao, use o Docker Tool Box