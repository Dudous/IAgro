import uuid
import hashlib

def get_mac_address():
  mac_int = uuid.getnode()
  mac_hex = hex(mac_int)[2:].upper()
  return ":".join(mac_hex[i:i+2] for i in range(0, 12, 2))

def criar_codigo_unico(mac_address):
    mac_address_bytes = mac_address.encode('utf-8')

    hash_object = hashlib.sha256(mac_address_bytes)
    hash_hex = hash_object.hexdigest()

    return hash_hex

def generateCode():
    mac_address = get_mac_address()
    print(f"MAC Address: {mac_address}")
    return criar_codigo_unico(mac_address)

codigo_unico = generateCode()
print(f"Código Único: {codigo_unico}")
print(len(codigo_unico))