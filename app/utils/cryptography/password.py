import bcrypt
        
def encrypt_password(_password) -> str:
    salt = bcrypt.gensalt()
    password = bcrypt.hashpw(_password.encode(), salt)
    return password.decode()

def check_password(_password, _hashed) -> bool:
    return bcrypt.checkpw(_password.encode(), _hashed.encode())