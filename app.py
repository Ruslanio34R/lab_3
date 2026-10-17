
def greet(name: str = "мир") -> str:
    return f"Привет, {name}!"


def apply_discount(price: float, percent: int) -> float:

    if not 0 <= percent <= 100:
        raise ValueError("Скидка должна быть от 0 до 100 процентов")
    return round(price * (100 - percent) / 100, 2)
