import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ======================================================
# Tabela de Frequências (Absoluta, Relativa e Acumulada)
# ======================================================

def frequencias_cat(dataframe,coluna,ordem=None):
    
    """
    Objetivo: Criar uma tabela de frequências (Absoluta, Relativa e Acumulada)
    
    Parâmetros: 
        dataframe = DataFrame Pandas
        coluna = String
        ordem = Lista ordenada de categorias
        
    Retorno 
        Tabela = DataFrame Pandas com as frequências calculadas
        
    Exemplo:
        frequencias_cat(df,'Coluna')
        
        frequencias_cat(df,'Coluna',['cat1','cat2','catN'])
    """
         
    tb = pd.DataFrame(dataframe[coluna].value_counts()).reset_index()
    tb.rename(columns={'count':'Frequência Absoluta'}, inplace=True)

    total = tb['Frequência Absoluta'].sum()

    tb['Frequência Relativa %'] = 0
    tb['Frequência Acumulada %'] = 0

    if ordem != None:
        tipo = pd.CategoricalDtype(categories=ordem, ordered=True)
        tb[coluna] = tb[coluna].astype(tipo)
        tb = tb.sort_values(by=coluna)
        
    for i in tb.index:
        tb.loc[i,'Frequência Relativa %'] = round(tb.loc[i,'Frequência Absoluta'] / total * 100,2)
    
    tb['Frequência Acumulada %'] = tb['Frequência Relativa %'].cumsum()

    return tb


# ================================================================================
# Agrupamento de variáveis do tipo Quantitativa por Faixas e Tabela de Frequências
# ================================================================================

def frequencias_num(dataframe, coluna,faixa):
    
    """
    Objetivo: Criar agrupamento por faixas para variáveis quantitativas e tabela de frequências (Absoluta, Relativa e Acumulada)
    
    Parâmetros: 
        dataframe = DataFrame Pandas
        coluna = String
        faixa = int
        
    Retorno 
        Tabela = DataFrame Pandas
        
    Exemplo:
        frequencias_num(df,'Coluna',10)
    """
    
    df = pd.DataFrame(dataframe[coluna])
    faixas = np.arange(df[coluna].min(), df[coluna].max()+1, faixa)
    df['Faixa'] = pd.cut(df[coluna], faixas)
    tb = df.groupby('Faixa').count().reset_index()
    
    tb.rename(columns={coluna:'Frequência Absoluta'}, inplace=True)

    total = tb['Frequência Absoluta'].sum()

    tb['Frequência Relativa %'] = 0
    tb['Frequência Acumulada %'] = 0

    for i in tb.index:
        tb.loc[i,'Frequência Relativa %'] = round(tb.loc[i,'Frequência Absoluta'] / total * 100,2)
    
    tb['Frequência Acumulada %'] = tb['Frequência Relativa %'].cumsum()
    
    return tb


# ================
# Gráfico de Pizza
# ================

def pie_plot(dataframe,coluna,titulo):
    """
    Objetivo: Gerar um gráfico de pizza
    
    Parâmetros: 
        dataframe = DataFrame Pandas
        coluna = String nome da coluna
        faixa = int faixa 
        
    Retorno 
        Gráfico de Pizza
        
    Exemplo:
        pie_plot(dataframe,coluna,titulo)
    """
    
    labels = [dataframe[coluna][0],dataframe[coluna][1]]

    freq = [dataframe['Frequência Absoluta'][0],dataframe['Frequência Absoluta'][1]]  

    fig, ax = plt.subplots(figsize=(3,3))
    
    colors = sns.light_palette('seagreen')

    ax.pie(freq, autopct='%1.1f%%', colors=colors, explode=(0,.1), startangle=90)

    ax.set_title(titulo)

    ax.legend(bbox_to_anchor=(1, 0, 0.5,1), loc='center left', labels=labels)

    plt.show()
    
    
    
# ================
# Gráfico de Barra
# ================  
    
def bar_plot(dataframe,eixo_x, eixo_y,titulo):
    """
    Objetivo: Gerar um gráfico de barra
    
    Parâmetros: 
        dataframe = DataFrame Pandas
        eixo_x, eixo_y = String nome das colunas do eixo_x e eixo_y
        titulo = String título do gráfico
        
    Retorno 
        Gráfico de Barra
        
    Exemplo:
        pie_plot(df,eixo_x, eixo_y,titulo)
    """
    
    fig, ax = plt.subplots(figsize=(6,3))
    ax.set_title(titulo)
    ax.
    sns.barplot(dataframe, x=eixo_x, y=eixo_y, palette=sns.light_palette("seagreen"))
    plt.show()