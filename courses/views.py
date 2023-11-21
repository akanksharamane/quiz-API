from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Courses
from .serializers import CoursesSerializer
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class CoursesViewSet(ModelViewSet):
    queryset=Courses.objects.all()
    serializer_class=CoursesSerializer
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

    #get all Courses
    def list(self,request):
        try:
            courses_objs = Courses.objects.all()
            serializer = self.get_serializer(courses_objs, many = True)

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

    #add Courses
    def create(self,request):
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
                'messaage':'Course added successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # get single Course
    def retrieve(self, request, pk = None):
        try:
            id = pk
            if id is not None:
                courses_obj = self.get_object()
                serializer = self.get_serializer(courses_obj)

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

    #update all fields of Course
    def update(self, request, pk=None):
        try:
            
            courses_obj = self.get_object()
            serializer = self.get_serializer(courses_obj,data=request.data, partial=False)

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
                'messaage':'Course updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    #update specific fields

    def partial_update(self,request, pk=None):
        try:
            
            courses_objs = self.get_object()
            serializer = self.get_serializer(courses_objs,data=request.data,partial = True)

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
                'messaage':'Course updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # delete Course
    def destroy(self, request,pk):
        try:
            id=pk
            courses_obj = self.get_object()
            courses_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'messaage':'Course deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })
