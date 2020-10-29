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