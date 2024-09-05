def bienvenida():
    """_summary_
    La funcion devuelve un mensaje con "Bienvenidos a la UTN"
    """

    print("Bienvenidos a la UTN")


bienvenida()

def calcular_area_rectangulo(base: float, altura: float) -> float:
    """_summary_ 
    La funcion calcula el area de un rectangulo y devuelve su resultado

    Args:
        base (float): _description_ la base del rectangulo
        altura (float): _description_ la altura del rectangulo

    Returns: 
        float: _description_ Devuelve el area
    """

    area = (base * altura)

    print(f"La base es de {base}, la altura de {altura} y el area de {area}")

    return area

calcular_area_rectangulo(20, 2)

