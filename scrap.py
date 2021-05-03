# -*- coding: utf-8 -*-
"""
Created on Mon May  3 02:26:49 2021

@author: caioa
"""

from selenium import webdriver
from time import sleep

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://www.linkedin.com/jobs/ci%C3%AAncia-de-dados-vagas/?originalSubdomain=br')
    resultados = driver.find_elements_by_class_name('result-card')
    
    lista_descricao = []
    for r in resultados:
            sleep(2)
            r.click()
            descricao = driver.find_element_by_class_name('description')
            lista_descricao.append(descricao.text)
        
    print(lista_descricao)
    descricao_salvar = '\n'.join(lista_descricao)
    with open ('desc_vagas.txt','w') as f:
        f.write(descricao_salvar)
        
    driver.quit()
        