# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from google.oauth2 import id_token
# from google.auth.transport import requests as google_requests
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.models import User
# from django.conf import settings


# class GoogleAuthView(APIView):
#     """
#     POST: Accepts a Google token and exchanges it for a JWT token.
#     """

#     def post(self, request):
#         token = request.data.get("token")

#         try:
#             # Verify the Google token
#             id_info = id_token.verify_oauth2_token(
#                 token, google_requests.Request(), settings.GOOGLE_CLIENT_ID
#             )

#             # Retrieve or create user from the verified Google token
#             user, created = User.objects.get_or_create(
#                 email=id_info["email"],
#                 defaults={
#                     "first_name": id_info["given_name"],
#                     "last_name": id_info["family_name"],
#                     "username": id_info["email"],
#                 },
#             )

#             # Create JWT token for the user
#             refresh = RefreshToken.for_user(user)

#             return Response(
#                 {
#                     "refresh": str(refresh),
#                     "access": str(refresh.access_token),
#                 }
#             )

#         except ValueError:
#             # Invalid token
#             return Response(
#                 {"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
#             )


# class LogoutView(APIView):
#     def post(self, request):
#         try:
#             refresh_token = request.data.get("refresh")
#             if not refresh_token:
#                 return Response(
#                     {"error": "Refresh token required"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#             token = RefreshToken(refresh_token)
#             token.blacklist()

#             return Response(
#                 {"message": "Successfully logged out"},
#                 status=status.HTTP_205_RESET_CONTENT,
#             )
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
