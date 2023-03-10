import functools

user = {"username": "Jose", "access_level": "guest"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permission for {user['username']}"
    return secure_function


@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "otra paswortd"


print(get_password("billing"))
