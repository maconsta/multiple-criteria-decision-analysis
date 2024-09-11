# import hashlib
# import os
# from functools import wraps
# from flask import request
# from flask import jsonify
#
# from backend.app import app
#
#
# class AuthError(Exception):
#     """
#        Class AuthError, helper class, use when throwing authentication errors. Extends Exception.
#
#        Attributes
#        ==========
#
#        error : str
#            error type
#
#        status_code : str
#            status code of the error
#        """
#
#     def __init__(self, error, status_code):
#         self.error = error
#         self.status_code = status_code
#
#
# @app.errorhandler(AuthError)
# def handle_auth_error(exception):
#     response = jsonify(exception.error)
#     response.status_code = exception.status_code
#     return response
#
#
# def get_token_auth_header():
#     """
#     Obtains the Access Token from the Authorization Header
#     """
#     auth = request.headers.get("Authorization", None)
#     if not auth:
#         raise AuthError({"code": "authorization_header_missing",
#                          "description":
#                              "Authorization header is expected"}, 401)
#
#     parts = auth.split()
#
#     if parts[0].lower() != "bearer":
#         raise AuthError({"code": "invalid_header",
#                          "description":
#                              "Authorization header must start with"
#                              " Bearer"}, 401)
#     elif len(parts) == 1:
#         raise AuthError({"code": "invalid_header",
#                          "description": "Token not found"}, 401)
#     elif len(parts) > 2:
#         raise AuthError({"code": "invalid_header",
#                          "description":
#                              "Authorization header must be"
#                              " Bearer token"}, 401)
#
#     token = parts[1]
#     return token
#
#
# def requires_auth(func):
#     """
#     Determines if the Access Token is valid
#     """
#
#     @wraps(func)
#     def decorated(*args, **kwargs):
#         token = get_token_auth_header()
#
#         try:
#             data = jwt.decode(token, app.config['JWT_SECRET_KEY'])
#         except:
#             raise AuthError({"code": "invalid_token", "description": "Invalid Token"}, 401)
#
#         return func(*args, **kwargs)
#
#     return decorated
#
#
# def hash_string(string):
#     # Create a salt
#     salt = os.urandom(16)
#
#     # Hash the string with the salt
#     hashed_string = hashlib.pbkdf2_hmac('sha256', string.encode(), salt, 100000)
#
#     return salt + hashed_string
#
#
# def verify_string(stored_string, provided_string):
#     stored_string = stored_string.decode()
#
#     # Extract the salt from the stored string
#     salt = stored_string[:16]
#
#     # Extract the hashed string from the stored string
#     stored_hashed_string = stored_string[16:]
#
#     # Hash the provided string with the same salt
#     hashed_string = hashlib.pbkdf2_hmac('sha256', provided_string.encode(), salt, 100000)
#
#     # Compare the hashed strings
#     return hashed_string == stored_hashed_string
