
from pysnmp.hlapi import *

# Configurar la dirección IP del switch y las credenciales SNMP
#ip_address = '10.55.0.116'  # Belkin International Inc. 	                                         B4:75:0E:7F:69:2A 
#ip_address = '10.55.1.20'   # LAPN600 Belkin International Inc. 	                                 B4:75:0E:1A:C3:43
ip_address = '10.55.0.125'  # CLPC36-ICSAMTPJ  10.55.0.125 	 CLPC36-ICSAMTPJ  D-Link International 	 A0:AB:1B:51:5E:2E 

community_string = 'public'

# Crear un generador de solicitudes SNMP
iterator = getCmd(SnmpEngine(),
                  CommunityData(community_string),
                  UdpTransportTarget((ip_address, 161)),
                  ContextData(),
                  ObjectType(ObjectIdentity('IF-MIB', 'ifDescr')))

# Iterar a través de las respuestas
for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in iterator:
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        # Imprimir la descripción de cada interfaz
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
