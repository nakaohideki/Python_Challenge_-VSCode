import pandas as pd  # Importação dos módulos a serem utilizados
import matplotlib.pyplot as plt
import mysql.connector
MySQL_connection = mysql.connector.connect(  # Criação de objeto para conexão ao banco de dados
    host='XX.XXX.XXX.XXX',
    database='challenge',
    user='challenge',
    password='challenge')

# Execução de query de consulta a banco de dados SQL
DataFrame = pd.read_sql_query(
    "SELECT Title, Rating FROM IMDB_movies GROUP BY Rating, Title DESC LIMIT 10", MySQL_connection)
# Configuração de gráfico de barras horizontal para exibição
DataFrame.plot.barh(x='Title', y='Rating',
                    title='Top 10 More Rated Movies', color='#0B8FFC')
plt.show()  # Exibição do gráfico de barras horizontal
print("This visualization is interesting for people who do not have any idea of watching.")
