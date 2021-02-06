import time
from selenium import webdriver
import csv


class Captura:
    def __init__(self, chromedriver_path, maximizar=False):
        self.chromedriver_path = chromedriver_path
        self.driver = webdriver.Chrome(self.chromedriver_path)
        if maximizar:
            self.driver.maximize_window()
        self.driver.get("http://www.csa-ma.com.br/")
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div/div/header/div/div/nav[1]/ul/li[3]/a/div[1]/i').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div/div[1]/div[1]/div[4]/div/a').click()
        time.sleep(10)

    def titulo(self, exibir=True):
        lista_titulos = list()
        titulos = self.driver.find_elements_by_xpath("//*[@class='post-title']")
        if exibir:
            print("Títulos:")
        for titulo in titulos:
            if exibir:
                print(titulo.text)
            lista_titulos.append(titulo.text)
        if exibir:
            print("\n")
        return lista_titulos

    def data(self, exibir=True):
        lista_datas = list()
        datas = self.driver.find_elements_by_xpath("//*[@class='post-date']")
        if exibir:
            print("Datas de postagem")
        for data in datas:
            if exibir:
                print(data.text)
            lista_datas.append(data.text)
        if exibir:
            print("\n")
        return lista_datas

    def resumo(self, exibir=True):
        lista_resumos = list()
        resumos = self.driver.find_elements_by_xpath("//*[@class='post-excerpt']")
        if exibir:
            print("Resumos:")
        for resumo in resumos:
            if exibir:
                print(resumo.text)
            lista_resumos.append(resumo.text)
        if exibir:
            print("\n")
        return lista_resumos

    def url_imagem(self, exibir=True):
        lista_urls_imgs = list()
        urls_imgs = self.driver.find_elements_by_xpath("//*[@class='attachment-post-thumbnail']")
        if exibir:
            print("Urls das imagens:")
        for url_img in urls_imgs:
            if exibir:
                print(url_img.get_attribute('src'))
            lista_urls_imgs.append(url_img.get_attribute('src'))
        if exibir:
            print("\n")
        return lista_urls_imgs

    def fecha(self, exibir=True):
        self.driver.quit()
        if exibir:
            print(f"{self.chromedriver_path} fechou!")

    def salva_csv(self, file_name, *postagens):
        quantidade_posts = len(postagens[0])
        quantidade_informacoes = len(postagens)

        with open(f'{file_name}.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            print("Linhas a serem gravadas no CSV:")
            for postagem in range(0, quantidade_posts):
                linha = list()
                for quantidade in range(0, quantidade_informacoes):
                    linha.append(postagens[quantidade][postagem])
                print(linha)
                writer.writerow(linha)
                print('---------------------------------------')
        print(f"CSV gerado! arquivo: {file_name}.csv")

    def envia_mensagem(self, nome, telefone, email, website,mensagem):
        self.driver.find_element_by_xpath("//*[@class='icon-envelope-alt']").click()

        campo_nome = self.driver.find_element_by_xpath(
            "/html/body/div/div/div[3]/div/div/div[2]/div/form/div[2]/div[1]/span[1]/input")
        campo_nome.send_keys(f'{nome}')

        campo_telefone = self.driver.find_element_by_xpath(
            "/html/body/div/div/div[3]/div/div/div[2]/div/form/div[2]/div[1]/span[3]/input")
        campo_telefone.send_keys(f'{telefone}')

        campo_email = self.driver.find_element_by_xpath(
            '/html/body/div/div/div[3]/div/div/div[2]/div/form/div[2]/div[1]/span[4]/input')
        campo_email.send_keys(f'{email}')

        campo_website = self.driver.find_element_by_xpath(
            '/html/body/div/div/div[3]/div/div/div[2]/div/form/div[2]/div[1]/span[5]/input')
        campo_website.send_keys(f'{website}')

        campo_mensagem = self.driver.find_element_by_xpath(
            '/html/body/div/div/div[3]/div/div/div[2]/div/form/div[2]/div[2]/span/textarea'
        )
        campo_mensagem.send_keys(f'{mensagem}')

        self.driver.find_element_by_xpath(
            '/html/body/div/div/div[3]/div/div/div[2]/div/form/div[2]/div[1]/input').click()

        time.sleep(5)
        print("Contato Enviado!")


if __name__ == '__main__':
    try:
        # Não passei o site, visto que essa sequência de passos serve necessariamente para este site
        # maximizar por padrão é False
        bot = Captura(chromedriver_path='chromedriver.exe', maximizar=True)
        titulos = bot.titulo(exibir=False)
        datas = bot.data(exibir=False)
        resumos = bot.resumo(exibir=False)
        urls_imgs = bot.url_imagem(exibir=False)
        bot.envia_mensagem('João Francisco Vieira Rodrigues Filho', '98984046372', 'joaofranciscovrfilho@gmail.com',
                           'github.com/joaofranciscoxd',
                           'Gostaria de fazer parte do time da RDP para adquirir e compartilhar conhecimento!')
        bot.fecha(exibir=False)
        bot.salva_csv("infos", titulos, datas, resumos, urls_imgs)
    except Exception as erro:
        print(erro)
