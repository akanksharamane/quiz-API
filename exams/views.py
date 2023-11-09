from django.shortcuts import render
from .serializers import ExamSerializer
from . models import Exam
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class ExamViewset(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        # if self.action == 'list':
        #     return AuthorSerializer
        # if self.action == 'create':
        #     return AuthorSerializer
        # elif self.action == 'upload_image':
        #     return AuthorImageSerializer
        return self.serializer_class

    #get all exam details
    def list(self,request):
        try:
            author_objs = Exam.objects.all()
            serializer = self.get_serializer(author_objs, many = True)

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

    #add exam detail
    def create(self,request):
        try:
            serializer =self.get_serializer(data=request.data)

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
                'messaage':'Exam detail added successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # get single exam detail
    def retrieve(self,request,pk=None):
        try:
            id = pk
            if id is not None:
                exam_obj = self.get_object()
                serializer = self.get_serializer(exam_obj)

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

    #update all fields of exam detail
    def update(self,request, pk=None):
        try:
            #author_objs = Author.objects.all()
            exam_objs = self.get_object()
            serializer = self.get_serializer(exam_objs,data=request.data, partial=False)

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
                'messaage':'Exam detail updated successfully'
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
            #author_objs = Author.objects.all()
            exam_obj = self.get_object()
            serializer = self.get_serializer(exam_obj,data=request.data,partial = True)

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
                'messaage':'Exam detail updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # delete exam detail
    def destroy(self, request,pk):
        try:
            id=pk
            author_obj = self.get_object()
            author_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'messaage':'Exam detail deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

