import getopt
import sys
import requests

# Función para realizar la consulta a la API de MAC
def consultar_mac(mac_address):
    API_ENDPOINT = 'https://api.maclookup.app/v2/macs/'
    try:
        respuesta = requests.get(API_ENDPOINT + mac_address)
        procesar_respuesta(respuesta, mac_address)
    except Exception as error:
        print(f"Error al hacer la consulta: {error}")

# Función para procesar la respuesta de la API
def procesar_respuesta(respuesta, mac_address):
    if respuesta.status_code == 200:
        datos = respuesta.json()
        mostrar_resultado(datos, mac_address)
        print(f"Tiempo de respuesta: {respuesta.elapsed.total_seconds() * 1000:.2f}ms")
    else:
        print(f"Error: La API devolvió el estado {respuesta.status_code}")

# Función para mostrar los resultados
def mostrar_resultado(datos, mac_address):
    if datos and 'company' in datos and datos['company']:
        print(f"Dirección MAC : {mac_address}")
        print(f"Fabricante    : {datos['company']}")
    else:
        print(f"Dirección MAC : {mac_address}")
        print("Fabricante    : No encontrado")

# Función para procesar la funcionalidad ARP (aún no implementada)
def consultar_arp():
    print("Funcionalidad ARP aún no implementada.")

# Función principal que procesa los argumentos con getopt y ejecuta las acciones
def main(argv):
    mac_address = None
    mostrar_arp = False

    # Uso de getopt para procesar los argumentos
    try:
        opts, args = getopt.getopt(argv, "m:a", ["mac=", "arp"])
    except getopt.GetoptError:
        print('Uso: script.py --mac <dirección_mac> [--arp]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-m", "--mac"):
            mac_address = arg
        elif opt in ("-a", "--arp"):
            mostrar_arp = True

    # Ejecutar las acciones según los argumentos
    if mac_address:
        print(f"Consultando fabricante para la dirección MAC: {mac_address}")
        consultar_mac(mac_address)
    if mostrar_arp:
        consultar_arp()

# Punto de entrada
if __name__ == "__main__":
    main(sys.argv[1:])
