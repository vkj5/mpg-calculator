nodef calculate_mpg(distance: float, fuel: float) -> float:
    if not isinstance(distance, (int, float)) or not isinstance(fuel, (int, float)):
        raise TypeError("Inputs must be numbers.")

    if fuel == 0:
        raise ValueError("Fuel cannot be zero.")

    if distance < 0 or fuel < 0:
        raise ValueError("Distance and fuel must be non-negative.")

    return (distance / fuel)

