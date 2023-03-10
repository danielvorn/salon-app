from django.http import Http404, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from salonapp.models import Salon
from salonapp.serializers import SalonSerializer

# Create your views here.


# @api_view(['GET', 'POST'])
# def salon_list(request):
#     """
#     List all salons, or create a new salon.
#     """
#     if request.method == 'GET':
#         salons = Salon.objects.all()
#         serializer = SalonSerializer(salons, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = SalonSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def salon_detail(request, pk):
#     """
#     Retrieve, update or delete a salon.
#     """
#     try:
#         salon = Salon.objects.get(pk=pk)
#     except Salon.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = SalonSerializer(salon)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = SalonSerializer(salon, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         salon.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

class SalonList(APIView):
    """
    List all salons, or create a new salon.
    """

    def get(self, request, format=None):
        salons = Salon.objects.all()
        serializer = SalonSerializer(salons, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SalonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalonDetail(APIView):
    """
    Retrieve, update or delete a salon instance.
    """

    def get_object(self, pk):
        try:
            return Salon.objects.get(pk=pk)
        except Salon.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        salon = self.get_object(pk)
        serializer = SalonSerializer(salon)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        salon = self.get_object(pk)
        serializer = SalonSerializer(salon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        salon = self.get_object(pk)
        salon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
