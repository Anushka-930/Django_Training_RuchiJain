from django.test import TestCase
from django.urls import reverse
from .models import Employee


class EmployeeUpdateTests(TestCase):
	def test_employee_can_be_edited(self):
		employee = Employee.objects.create(eno=101, ename='Original', esal=1000)
		update_url = reverse('updateemployee')

		response = self.client.get(update_url, {'id': employee.id})

		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Original')

		response = self.client.post(update_url, {
			'id': employee.id,
			'eno': 102,
			'ename': 'Updated',
			'esal': 2000,
		})

		self.assertRedirects(response, reverse('employeelist'))
		employee.refresh_from_db()
		self.assertEqual(employee.eno, 102)
		self.assertEqual(employee.ename, 'Updated')
		self.assertEqual(employee.esal, 2000)
