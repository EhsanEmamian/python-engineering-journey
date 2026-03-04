def analyze_number(n: int) -> dict:
    return {
        "is_even": n % 2 == 0,
        "is_positive": n > 0,
        "square": n ** 2,
    }