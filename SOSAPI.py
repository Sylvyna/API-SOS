import requests
import json
import os
import csv
import concurrent.futures


def Login_usuario(Credenciales:str = "Login.json"):
  '''
  Funcion para realizar el login en la API de SOS-Contador y obtener el token de acceso a la API

  '''
  # Pagina de login de la API
  url = "https://api.sos-contador.com/api-comunidad/login"

  Credentials = rf"{Credenciales}"

  # Cargar el archivo JSON con las credenciales
  payload = json.dumps(json.load(open(Credentials)))

 # Crear el encabezado de la peticion
  headers = {'Content-Type' : 'application/json'}

  # Se realiza la peticion POST
  response = requests.request("POST", url, headers=headers, data=payload)

  # Exportar el resultado a un archivo JSON
  with open('response.json', 'w') as f:
    json.dump(response.json(), f)

  return response.json(), response.json()['jwt'] , payload , headers


def Login_Cuit():
  '''
  Funcion para obtener los bearer token de la API de SOS-Contador por cada contribuyente

  ---
  - pd: las claves se deben reiniciar todos los lunes
  '''

  # se crea la carpeta Token si no existe
  if not os.path.exists('Token'):
    os.makedirs('Token')

  # Se obtiene el response del login, el jwt y el payload
  ResponseLogin, jwt, payload , header = Login_usuario()

  url = 'https://api.sos-contador.com/api-comunidad/cuit/credentials/'

  # Abrir el archivo CSV para escribir los datos
  with open('contribuyentes.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'cuit', 'razon_social', 'jwt']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames , delimiter='|')
    writer.writeheader()


    def fetch_token(i):
      payload = ""
      id = i['id']
      cuit = i['cuit']
      razon_social = i['razonsocial']

      url2 = url + str(id)
      header = {'Content-Type': 'application/json'}
      Authorization = jwt
      header['Authorization'] = f"Bearer {Authorization}"

      # Se realiza la peticion GET
      response = requests.request("GET", url2, headers=header, data=payload)
      
      # Exportar el resultado a un archivo JSON por cada contribuyente
      with open(f'Token/response_{cuit}_{id}_{razon_social}.json', 'w') as f:
        json.dump(response.json(), f)
      
      # Escribir los datos en el archivo CSV
      return {'id': id, 'cuit': cuit, 'razon_social': razon_social , 'jwt': response.json()['jwt']}

    # por cada 'id' en 'cuits' del response se obtiene el bearer token concurrentemente
    with concurrent.futures.ThreadPoolExecutor() as executor:
      results = list(executor.map(fetch_token, ResponseLogin['cuits']))

    # Escribir los datos en el archivo CSV
    for result in results:
      writer.writerow(result)
      
def consulta_f2002():
  
  # Abrir el csv de "contribuyentes.csv" que posee los datos necesarios para hacer la consulta ("cuit"|"razon_social"|"jwt"|"año"|"mes"|"F2002")
  
  url = "https://api.sos-contador.com/api-comunidad/iva/listado/:ejercicio?anio=AAAA&mes=MM"
  
  archivo = "contribuyentes.csv"
  with open(archivo, 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    for row in reader:
      if row['F2002'] == 'SI':
        cuit = row['cuit']
        razon_social = row['razon_social']
        jwt = row['jwt']
        año = row['año']
        mes = row['mes']
        url = url.replace('AAAA', año)
        url = url.replace('MM', mes)
        header = {'Content-Type': 'application/json'}
        Authorization = jwt
        header['Authorization'] = f"Bearer {Authorization}"
        response = requests.request("GET", url, headers=header)
        
        # se crea la carpeta F2002 si no existe
        if not os.path.exists('F2002'):
          os.makedirs('F2002')
    
        with open(f'F2002/F2002_{cuit}_{razon_social}_{año}_{mes}.json', 'w') as f:
          json.dump(response.json(), f)


if __name__=="__main__":
  # Login_Cuit()
  consulta_f2002()