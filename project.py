#from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
#def document_initialised(navegador):
    #return navegador.execute_script("return initialised")
navegador = webdriver.Edge()
navegador.get("https://forms.gle/ssJqxQ81rSkQRPwu5")
#WebDriverWait(navegador, timeout=1000000).until(document_initialised)

#Loja
navegador.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("547554000")
#Usuario
navegador.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input[1]').send_keys("MARCUSV")
#Senha
navegador.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Mv.24071")
#Clica no botão de logar
navegador.find_element("xpath", '').click


#Tipo produto
navegador.find_element("xpath", '//*[@id="i17"]/div[3]/div').click
#Tipo pessoa
navegador.find_element("xpath", '//*[@id="i33"]/div[3]/div').click
#CPF
navegador.find_element("xpath", '').send_keys("00000000191")
#Renda
navegador.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("32000")
#Valor solicitado
navegador.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("12000")
#Data Nacimento
navegador.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("01011960")
#Clica no botão de prosseguir
navegador.find_element("xpath", '').click




##Escolher o top (clica na combobox)
#navegador.find_element("xpath", '').click
##Escolher o top (clica no item da combobox)
#navegador.find_element("xpath", '').click



##Escolher parcela
#navegador.find_element("xpath", '').click
##Prosseguir
#navegador.find_element("xpath", '').click