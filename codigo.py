import pyautogui as pg
import time
import pandas as pd

pg.PAUSE = 0.5

pg.press("win")
pg.write("edge")
pg.press("enter")

time.sleep(5)

pg.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pg.press("enter")

time.sleep(5)

pg.click(x=458, y=354)
pg.write("pythonimpressionador@gmail.com")
pg.press("tab")
pg.write("senha12345")

pg.press("tab")
pg.press("enter")

time.sleep(2)

tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:

    codigo = tabela.loc[linha, "codigo"]

    pg.click(x=421, y=238)
    pg.write(codigo)
    pg.press("tab")
    pg.write(tabela.loc[linha, "marca"])
    pg.press("tab")
    pg.write(tabela.loc[linha, "tipo"])
    pg.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pg.write(categoria)
    pg.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pg.write(preco_unitario)
    pg.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pg.write(custo)
    pg.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != 'NaN':
        pg.write(obs)
    pg.press("tab")
    pg.press("enter")
    pg.scroll(5000)