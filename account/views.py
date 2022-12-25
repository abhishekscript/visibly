import base64
import json
import requests

from rest_framework import authentication
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.template import Template
from django.template import Context
from django.http import HttpResponse

from account import serializers
from account import dal
from payments.razorpay import public as razorpay_public
from plugins import public as plugin_public

# Create your views here.


class UserSignUp(generics.CreateAPIView):
    permission_classes = ()
    serializer_class = serializers.UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            plugin_public.get_tokens_for_user(user), status=status.HTTP_201_CREATED, headers=headers
        )


class UserSignIn(APIView):
    permission_classes = ()
    serializer_class = serializers.UserSerializer
    def post(self, request,):
        data = request.data

        if not data.get('email') and not data.get('username'):
            return Response({'error': 'e-mail or username required'})

        password = data.get('password')
        validate = authentication.authenticate
        if data.get('email'):
            user = validate(username=data['email'], password=password)
        if data.get('username'):
            user =  validate(username=data['username'], password=password)

        if user:
            return Response(plugin_public.get_tokens_for_user(user))

        return Response({'error': 'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class FacebookUserSetup(APIView):
    permission_classes = ()
    def post(self, request,):
        data = request.data

        if verify_facebook_user_token(data['fb_token']):
            name = data['name'].split()
            default = {'first_name': None, 'username': data['email']}
            user_name_len = len(name)
            if user_name_len == 2:
                default.update({'first_name': name[0].lower(), 'last_name': name[1].lower()})
            if user_name_len ==1:
                default.update({'first_name': name[0]})

            return Response(
                plugin_public.get_tokens_for_user(
                    dal.get_or_create_user_by_email(data['email'], default)
                )
            )

        return Response({'error': 'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)


class GoogleUserSetup(APIView):
    permission_classes = ()
    def post(self, request,):
        data = request.data

        user_data = verify_and_fetch_google_login_data(data['credential'])
        default = {'first_name': user_data['given_name'], 'last_name': user_data['family_name']}
        return Response(
            plugin_public.get_tokens_for_user(
                dal.get_or_create_user_by_email(user_data['email'], default)
            )
        )


def verify_facebook_user_token(token: str) -> bool:
    """Returns True if token is valid else False"""

    access_token = '1497371897239228|2Lb6yXBt-izS36azd8a-TspM5Lg'
    user_token = token
    url = f'https://graph.facebook.com/debug_token?input_token={user_token}&access_token={access_token}'

    response = requests.request("GET", url)
    if response and response.status_code == 200:
        return True

    return False


def verify_and_fetch_google_login_data(token: str) -> dict:
    """Calls google Verification API and returns user data"""

    token_data = token.split('.')
    return json.loads(base64.b64decode(token_data[1]))


class TestPayment(APIView):
    permission_classes = ()
    def get(self, request,):
        data = razorpay_public.create_order(500, 'INR', '1')
        template = Template(razorpay_public.get_rendered_data())
        
        return HttpResponse(
            template.render(Context(dict(amount=data['amount'], currency=data['currency'])))
        )
