from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Feedback
from .serializers import FeedbacksSerializer
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class FeedbacksViewSet(ModelViewSet):
    queryset=Feedback.objects.all()
    serializer_class=FeedbacksSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated]


    def get_serializer_class(self):
        return self.serializer_class

    #get all Feedback
    def list(self, request):
        try:
            feedbacks_objs = Feedbacks.objects.all()
            serializer = self.get_serializer(feedbacks_objs, many = True)

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

    #add Feedback
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
                'messaage':'feedback added successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # get single Feedback
    def retrieve(self, request, pk = None):
        try:
            id = pk
            if id is not None:
                feedbacks_obj = self.get_object()
                serializer = self.get_serializer(feedbacks_obj)

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

    #update all fields of feedback
    def update(self, request, pk=None):
        try:
            
            feedbacks_obj = self.get_object()
            serializer = self.get_serializer(feedbacks_obj,data=request.data, partial=False)

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
                'messaage':'feedback updated successfully'
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
            
            feedbacks_objs = self.get_object()
            serializer = self.get_serializer(feedbacks_objs,data=request.data,partial = True)

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
                'messaage':'feedback updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })

    # delete Course
    def destroy(self, request, pk):
        try:
            id=pk
            feedbacks_obj = self.get_object()
            feedbacks_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'messaage':'Feedback deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status': APIException.status_code
            })
