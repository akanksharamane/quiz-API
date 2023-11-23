from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Batches
from .serializers import BatchesSerializer
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class BatchesViewSet(ModelViewSet):
    queryset=Batches.objects.all()
    serializer_class=BatchesSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    def get_serializer_class(self):
        return self.serializer_class

    #get all Batches
    def list(self, request):
        try:
            batches_objs = Batches.objects.all()
            serializer = self.get_serializer(batches_objs, many = True)

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

    #add Batches
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
                'messaage':'Batch added successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # get single Batches
    def retrieve(self, request, pk = None):
        try:
            id = pk
            if id is not None:
                batches_obj = self.get_object()
                serializer = self.get_serializer(batches_obj)

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

    #update all fields of Batch
    def update(self, request, pk=None):
        try:
            
            batches_obj = self.get_object()
            serializer = self.get_serializer(batches_obj, data=request.data, partial=False)

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
                'messaage':'Batch updated successfully'
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
            
            batches_objs = self.get_object()
            serializer = self.get_serializer(batches_objs, data=request.data ,partial = True)

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
                'messaage':'Batch updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # delete Batch
    def destroy(self, request ,pk):
        try:
            id=pk
            batches_obj = self.get_object()
            batches_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'messaage':'Batch deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

            
