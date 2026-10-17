"""Демо-модуль для показа Pull Request."""


def greet(name: str = "мир") -> str:
    """Возвращает приветствие. Ветка feature/greeting-name может расширить это."""
    return f"Привет, {name}!"


def apply_discount(price: float, percent: int) -> float:
    """Считает цену со скидкой.

    >>> apply_discount(100.0, 10)
    90.0
    """
    if not 0 <= percent <= 100:
        raise ValueError("Скидка должна быть от 0 до 100 процентов")
    return round(price * (100 - percent) / 100, 2)
