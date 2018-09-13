from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('drivers\chromedriver.exe')

driver.set_page_load_timeout(10)

user = input("Digite o seu login: ")
password = input("Digite sua senha: ")

driver.get('http://google.com.br')
driver.find_element_by_name('q').send_keys('Gamegol')
driver.find_element_by_name('btnK').send_keys(Keys.ENTER)
driver.find_element_by_partial_link_text('Game Gol').click()
driver.find_element_by_name('iptUsuario').send_keys(user)
driver.find_element_by_name('iptSenha').send_keys(password)
driver.find_element_by_name('iptRepass').click()
driver.find_element_by_class_name('btOk').click()


time.sleep(5)
driver.quit()
