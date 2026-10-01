from django.db import models
from django.contrib.auth.models import User


class TestResult(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_results')
	attempt = models.PositiveIntegerField()
	right = models.PositiveIntegerField()
	wrong = models.PositiveIntegerField()
	points = models.PositiveIntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']
