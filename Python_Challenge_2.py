import pandas as pd  # Importação dos módulos a serem utilizados
import mysql.connector
MySQL_connection = mysql.connector.connect(
    host='XX.XXX.XXX.XXX',
    database='challenge',
    user='challenge',
    password='challenge')

Query_1 = "SELECT STORE_CODE, STORE_NAME, START_DATE, END_DATE, BUSINESS_NAME, BUSINESS_CODE FROM data_store_cad"  # Query 1
Query_2 = "SELECT STORE_CODE, DATE, SALES_VALUE, SALES_QTY FROM data_store_sales WHERE DATE BETWEEN '2019-01-01' AND '2019-12-31'"  # Query 2


def date_filter(DATE):  # Função que a query no intervalo de data na lista DATE
    # Cabeçalho de retorno
    Select = "SELECT STORE_NAME AS LOJA, BUSINESS_NAME AS CATEGORIA, ROUND(SUM(SALES_VALUE) / SUM(SALES_QTY),2) AS TM"
    # Configuração da Query 1 na função criada
    From = " FROM (" + Query_1 + ") AS Query1"
    # Junção interna da Query 1 com a Query2 no campo STORE_CODE
    Inner_join = " INNER JOIN (" + Query_2 + ") AS Query2 USING (STORE_CODE) "
    # Agrupamento da tabela resultante por ordem ascendente de LOJA e CATEGORIA
    Group_by = "GROUP BY LOJA, CATEGORIA;"
    # Filtro de data com as datas informadas na função
    Where = "WHERE DATE BETWEEN '" + \
        str(DATE[0]) + "' AND '" + str(DATE[1]) + "'"

    print(pd.read_sql_query(Select + From + Inner_join + Where + Group_by,
          MySQL_connection))  # Impressão da tabela gerada pela função


# Lista de datas com data inicial e data final
DATES = ['2019-10-01', '2019-12-31']
# Aplicação da função date_filter com as datas iniciais e finais contidas na Lista de datas
date_filter(DATES)
