import jwt

class AuthenticationService:
    def authenticate(self, token: str) -> dict:
        decoded_token = jwt.decode(token, algorithms=['HS256'])
        return decoded_token
