from typing import List, Dict
from mcp.server.fastmcp import FastMCP
import math

mcp = FastMCP("My App")
#######################################################################################
# statistica
#######################################################################################


@mcp.tool()
def stat(number: List[float]) -> dict:
    print("DEBUG - Numeri ricevuti:", number)

    """Calcola parametri statistici inserendo una lista di numeri"""
    if not number:
        return {"error": "Lista vuota o non valida"}

    n = len(number)
    min_value = min(number)
    max_value = max(number)
    mean = sum(number) / n
    # Per calcolare la mediana, possiamo ordinare la lista e trovare il valore centrale
    sorted_numbers = sorted(number)
    mid = len(sorted_numbers) // 2
    median = (sorted_numbers[mid] + sorted_numbers[~mid]) / 2
    variance = sum((x - mean) ** 2 for x in number) / len(number)
    std_dev = math.sqrt(variance)

    return {
        "conteggio": n,
        "minimo": min_value,
        "massimo": max_value,
        "media": mean,
        "mediana": median,
        "varianza": variance,
        "std_dev": std_dev
    }


@mcp.tool()
def linear_regression(x: List[float], y: List[float]) -> dict:
    """Calcola la regressione lineare tra due liste di numeri"""
    if len(x) != len(y) or len(x) == 0:
        return {"error": "Le liste devono avere la stessa lunghezza e non essere vuote"}

    n = len(x)
    x_mean = sum(x) / n
    y_mean = sum(y) / n

    # Calcolo dei coefficienti della retta di regressione
    numerator = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    denominator = sum((x[i] - x_mean) ** 2 for i in range(n))

    if denominator == 0:
        return {"error": "Denominatore zero, impossibile calcolare la regressione"}

    # calcolo R^2
    ss_total = sum((y[i] - y_mean) ** 2 for i in range(n))
    ss_residual = sum((y[i] - (x_mean + (numerator / denominator)
                      * (x[i] - x_mean))) ** 2 for i in range(n))
    r2 = 1 - (ss_residual / ss_total)

    slope = numerator / denominator
    intercept = y_mean - slope * x_mean

    return {
        "numeratore": numerator,
        "denominatore": denominator,
        "ss_total": ss_total,
        "ss_residual": ss_residual,
        "coefficiente_angolare": slope,
        "intercetta": intercept,
        "r_quadrato": r2
    }
