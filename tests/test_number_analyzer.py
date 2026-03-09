from core.number_analyzer import analyze_number


def test_analyze_number_even_positive():
    result = analyze_number(4)
    assert result["is_even"] is True
    assert result["is_positive"] is True
    assert result["square"] == 16


def test_analyze_number_odd_negative():
    result = analyze_number(-3)
    assert result["is_even"] is False
    assert result["is_positive"] is False
    assert result["square"] == 9