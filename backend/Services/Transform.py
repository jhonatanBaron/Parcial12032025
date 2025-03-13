def transform_data(data):
    for peli in data:
        peli["nombre"] = peli["nombre"].lower().replace(" ", "-")
        peli["categoria"] = "Mala" if peli["califica"] <= 5 else "Regular" if peli["califica"] <= 7 else "Buena"
        peli["decada"] = (peli["año_lanzamiento"] // 10) * 10
        peli["puntuacion_ajustada"] = (peli["califica"] * 2) - ((2025 - peli["año_lanzamiento"]) / 10)
    return data
