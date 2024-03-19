# passo a passo do projeto
# passo 1: entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

pyautogui.PAUSE = 1


#abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press('enter')

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa um pouco maior
time.sleep(3)

pyautogui.click(x=650, y=380)   
pyautogui.write("zedamanga@gmail.com")
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.write("1234")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    
    pyautogui.click(x=680, y=261)
    pyautogui.write(tabela.loc[linha, "codigo"])

    pyautogui.press("tab")
    
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
   
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]

    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

   
    pyautogui.press("enter")

    pyautogui.scroll(5000)








# passo 2: fazer login
# passo 3: importar base de dados
# passo 4: cadastrar um produto
# passo 5: repetir o processo de cadastro até acabar