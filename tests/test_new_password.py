import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters
    
def test_pass_leng():
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    passleng = len(str(password))
    assert passleng == 100

def test_pass_same():
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password1 = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    password2 = generate_password(100)
    password3 = generate_password(100)
    password4 = generate_password(100)
    assert not (password1 == password2 and password1 == password3 and password1 == password4)

"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""