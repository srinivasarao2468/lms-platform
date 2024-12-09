from keycloak import KeycloakOpenID

class KeycloakAuth:
    def __init__(self, server_url, realm_name, client_id, client_secret_key):
        self.keycloak_openid = KeycloakOpenID(
            server_url=server_url,
            realm_name=realm_name,
            client_id=client_id,
            client_secret_key=client_secret_key
        )

    def get_user_info(self, token: str):
        return self.keycloak_openid.userinfo(token)

    def verify_token(self, token: str):
        try:
            return self.keycloak_openid.decode_token(token, verify=True)
        except Exception as e:
            print(f"Token verification failed: {e}")
            return None
