
# Create your views here.
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from user_app import serializers
from user_app import private


class UserApplicationView(viewsets.ModelViewSet):
    """API's for User Application"""

    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['post'], detail=False, url_path='extra_action', url_name='extra_action', permission_classes=())
    def save_app(self, request):
        request.data['user'] = request.user.id
        serializer = serializers.UserApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True, url_path='deploy_app', url_name='deploy_app')
    def deploy_app_for_user(self, request):
        deployment_serializer = serializers.UserApplicationDeploymentSerializer(data=request.data)
        if not deployment_serializer.is_valid():
            return Response(deployment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        private.deploy_wordpress_app.delay(request.user.id, deployment_serializer.data['app_id'])
        return Response({})
