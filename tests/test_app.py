from app import get_greeting


def test_get_greeting_default_none():
    assert get_greeting(None) == ""


def test_get_greeting_default_empty():
    assert get_greeting("") == ""


def test_get_greeting_default_whitespace():
    assert get_greeting("   ") == ""


def test_get_greeting_with_name():
    assert get_greeting("Christopher") == "Welcome Christopher"


def test_get_greeting_strips_whitespace():
    assert get_greeting("  Ada  ") == "Welcome Ada"
