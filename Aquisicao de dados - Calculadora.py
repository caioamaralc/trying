#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


url = 'https://www.vivareal.com.br/aluguel/sp/sao-paulo/apartamento_residencial/?pagina=2'


# In[3]:


c= requests.get(url).content
soup = BeautifulSoup(c)


# In[4]:


nome_anuncio = soup.find_all('span',{'class':'property-card__title js-cardLink js-card-title'})
nome_anuncio[0].text


# In[7]:


paginas = ['']
for i in range(2,5):
    a = '?pagina='+str(i)
    print(a)
    paginas.append(a)


# In[9]:


import pandas as pd
def converter_df(aluguel_lista,quartos_lista,endereco_lista,banheiro_lista,vaga_lista,area_lista):
    data = {'aluguel':aluguel_lista,
           'quartos':quartos_lista,
           'endereco':endereco_lista,
           'banheiro':banheiro_lista,
            'vaga':vaga_lista,
            'area':area_lista}
    df = pd.DataFrame(data)
    return df


# In[11]:


def scrap(url):
    c = requests.get(url).content
    soup = BeautifulSoup(c)
    
    aluguel_tag = soup.find_all('div', {'class':'property-card__price js-property-card-prices js-property-card__price-small'}) 
    aluguel_lista = [p.text for p in aluguel_tag] 
    #print(len(aluguel_lista)) 
    
    quartos_tag = soup.find_all('li', {'class': 'property-card__detail-item property-card__detail-room js-property-detail-rooms'}) 
    quartos_lista = [en.text for en in quartos_tag] 
    #print(len(quartos_lista)) 
    
    endereco_tag = soup.find_all('span', {'class': 'property-card__address'}) 
    endereco_lista = [fg.text for fg in endereco_tag] 
    #print(len(endereco_lista)) 
    
    banheiro_tag = soup.find_all('li', {'class': 'property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom'}) 
    banheiro_lista = [yp.text for yp in banheiro_tag] 
    #print(len(banheiro_lista))

    vaga_tag = soup.find_all('li', {'class': 'property-card__detail-item property-card__detail-garage js-property-detail-garages'}) 
    vaga_lista = [yp.text for yp in vaga_tag] 

    area_tag = soup.find_all('li', {'class': 'property-card__detail-item property-card__detail-area'}) 
    area_lista = [yp.text for yp in area_tag] 
    
    df=converter_df(aluguel_lista,quartos_lista,endereco_lista,banheiro_lista,vaga_lista,area_lista)
    
    return df


# In[20]:


df_lista = []
for pg in paginas:
    URL = 'https://www.vivareal.com.br/aluguel/sp/sao-paulo/casa_residencial/{}#tipos=casa_residencial,condominio_residencial'.format(pg)
    print('Coletando URL:', URL)
    try:
        df = scrap(URL)
        #print(df)
        print('Coletando URL:', URL)
    except Exception as e:
        print('Erro ao coletar dados na url:', url)
        print(e)
    df_lista.append(df)
    df_final = pd.concat(df_lista)


# In[21]:


df_final.head()


# In[23]:


df2=pd.concat(df_lista)
df2.head(77)


# In[24]:


df2['bairro'] = df2.endereco.str.split('\s-').str[1]
df2['rua'] = df2.endereco.str.split('\s-').str[0]
df2['bairro'] = df2.bairro.str.split(',').str[0]

df2.head()


# In[ ]:




