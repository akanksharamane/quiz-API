from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Branches
from .serializers import BranchesSerializer
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class BranchesViewSet(ModelViewSet):
    queryset=Branches.objects.all()
    serializer_class=BranchesSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    def get_serializer_class(self):
        # if self.action == 'list':
        #     return AuthorSerializer
        # elif self.action == 'create':
        #     return AuthorSerializer
        # elif self.action == 'upload_image':
        #     return AuthorImageSerializer
        return self.serializer_class

    #get all Branches
    def list(self, request):
        try:
            branches_objs = Branches.objects.all()
            serializer = self.get_serializer(branches_objs, many = True)

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #add Branches
    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_201_CREATED,
                'data': serializer.data,
                'messaage':'Branch added successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # get single branch
    def retrieve(self, request, pk = None):
        try:
            id = pk
            if id is not None:
                branches_obj = self.get_object()
                serializer = self.get_serializer(branches_obj)

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #update all fields of branch
    def update(self, request, pk=None):
        try:
            
            branches_obj = self.get_object()
            serializer = self.get_serializer(branches_obj, data=request.data, partial=False)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data,
                'messaage':'Branch updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #update specific fields

    def partial_update(self, request, pk=None):
        try:
            
            branches_objs = self.get_object()
            serializer = self.get_serializer(branches_objs, data=request.data ,partial = True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'data': serializer.errors,
                    'message':'Invalid data'
                })
            serializer.save()

            return Response({
                'status':status.HTTP_200_OK,
                'data': serializer.data,
                'messaage':'Branch updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # delete Branch
    def destroy(self, request ,pk):
        try:
            id=pk
            branches_obj = self.get_object()
            branches_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'messaage':'Branch deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

