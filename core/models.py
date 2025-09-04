from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta

class Client(models.Model):
  """Represents a client with personal details.

  This model stores client information, including name, email, and date of birth.
  """
  id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  date_of_birth = models.DateField(null=True, blank=True)
  ethnicity = models.CharField(max_length=100)
  allergies = models.TextField(blank=True)
  sport = models.CharField(max_length=100)
  fitness_goal = models.CharField(max_length=100)
  nutritional_goal = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'<Client {self.first_name} {self.last_name} ({self.email})>'

class MealPlan(models.Model):
  """Represents a meal plan associated with a user and a list of meals.

  This model stores meal plan details, including the user, description, and meals for a specific timestamp.
  """
  client = models.ForeignKey(Client, on_delete=models.CASCADE)
  id = models.AutoField(primary_key=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  meals = models.TextField(help_text="JSON or comma-separated list of meals")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f'<MealPlan for user {self.user_id} for time {self.timestamp}: {self.meals}>'

  @staticmethod
  def get_meal_plans_by_user_and_date(user_id, start_date=None, end_date=None) -> 'models.QuerySet':
    """
    Retrieve MealPlan objects for a user within a date range.
    If no date range is provided, defaults to current week.
    Returns a QuerySet of MealPlan instances.
    """
    now = timezone.now()
    if start_date is None or end_date is None:
      # Get start and end of current week (Monday to Sunday)
      start_of_week = now - timedelta(days=now.weekday())
      end_of_week = start_of_week + timedelta(days=6, hours=23, minutes=59, seconds=59)
      start_date = start_of_week
      end_date = end_of_week
    return MealPlan.objects.filter(client_id=user_id, timestamp__range=(start_date, end_date))
  @staticmethod
  def add_meal_plan(client,meals):
    pass    
