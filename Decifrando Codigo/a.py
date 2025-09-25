from datetime import datetime

data = datetime.now()

data_formatada = data.strftime("%d/%m/%Y %H - %Mco")
print(data_formatada)