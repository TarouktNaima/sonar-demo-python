from src.app import add, is_palindrome
def test_add():
    assert add(2,3) ==6
    assert add(-1, 1) ==0
def test_is_palindrome():
    assert is_palindrome("radar")
    assert is_palindrome("A man a plan a canal Panama")
    assert not is_palindrome("hello")