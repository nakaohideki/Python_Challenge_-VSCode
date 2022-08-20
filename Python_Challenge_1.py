import pandas as pd  # Importação dos módulos a serem utilizados
import mysql.connector
MySQL_connection = mysql.connector.connect(
    host='XX.XXX.XXX.XXX',
    database='challenge',
    user='challenge',
    password='challenge')


def retrieve_data(PRODUCT_CODE, STORE_CODE, DATE):  # Criação da função parametrizada
    Select = "SELECT * "  # Conversão dos parâmetros em Strings para criação da Query
    From = "FROM data_product_sales "
    Where = "WHERE PRODUCT_CODE = " + \
        str(PRODUCT_CODE) + " AND STORE_CODE = " + str(STORE_CODE)
    Between = " AND DATE BETWEEN '" + \
        str(DATE[0]) + "' AND '" + str(DATE[1]) + "';"
    # Consolidação da query a ser executada
    SQLquery = Select + From + Where + Between
    # Retorno do resultado da execução da query
    return pd.read_sql_query(SQLquery, MySQL_connection)


# Criação de datas de exemplo para testar a função retrieve_data
DATES = ['2019-01-01', '2019-01-31']
my_data = retrieve_data(18, 1, DATES)
print(my_data)
