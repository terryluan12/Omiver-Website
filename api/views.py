from django.utils.dateparse import parse_datetime
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .serializer import ClientSerializer, MealPlanSerializer
from core.models import MealPlan, Client

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the API endpoint!")

@api_view(['GET'])
def meal_plan(request):
    """
    Handles the meal plan requests.
    Accepts client_id, start_date, and end_date as query parameters.
    Returns the meal plan for the specified client and date range.
    """
    client_id = request.GET.get('client_id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if not client_id:
        return Response({'error': 'client_id is required'}, status=status.HTTP_400_BAD_REQUEST)
    # Optionally parse start_date and end_date if provided
    start_dt = parse_datetime(start_date) if start_date else None
    end_dt = parse_datetime(end_date) if end_date else None
    meal_plans = MealPlan.get_meal_plans_by_client_and_date(client_id, start_dt, end_dt)
    # Serialize meal plans
    meal_plan_list = [
        {
            'id': mp.id,
            'client_id': mp.client_id,
            'timestamp': mp.timestamp,
            'meals': mp.meals,
            'created_at': mp.created_at,
            'updated_at': mp.updated_at
        }
        for mp in meal_plans
    ]
    meal_plan = MealPlanSerializer(meal_plan_list, many=True)
    return Response(meal_plan.data)

# @login_required
@api_view(['GET'])
def generate_mealPlan(request, client_id):
    client = Client.objects.get(id=client_id)
    return Response({'message': f'will send client info: {client}'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_client(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def client_handler(request,pk):
    if request.method == 'GET':
        client = Client.objects.get(id=pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)
    return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
