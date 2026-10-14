puntuaciones={"tortillapapa":6, "fileteempanao":9, "leoncomegambas":3,"webofrito":10 }

for c,v in puntuaciones.items():
    if v>=5:
        print(c,v)

buenos={clave:valor for clave, valor in puntuaciones.items() if valor>=5}

for k in buenos:
    buenos[k]=k+"final"
    print (buenos[k])