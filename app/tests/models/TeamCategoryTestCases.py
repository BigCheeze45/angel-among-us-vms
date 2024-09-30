from django.test import TestCase
from django.db.utils import DataError
from django.core.exceptions import ObjectDoesNotExist

from app.models.TeamCategory import TeamCategory


class TeamCategoryTestCases(TestCase):
    """
    Test TeamCategory model
    """

    def setUp(self):
        # Create a new TeamCategory to start the test
        self.test_instance = TeamCategory.objects.create(name="Admin")

    def test_model_creation(self):
        # Get the created instance from the database
        instance = TeamCategory.objects.get(name="Admin")

        # test if names are the same
        self.assertEqual(instance.name, "Admin")

    def test_model_str(self):
        self.assertEqual(str(self.test_instance), "Admin")

    def test_model_update(self):
        # Update the field value
        self.test_instance.name = "Administration"
        self.test_instance.save()

        updated_instance = TeamCategory.objects.get(name="Administration")
        self.assertEqual(updated_instance.name, "Administration")

    def test_model_name_char_limit(self):
        self.test_instance.name = "Admin" * 2001
        with self.assertRaises(DataError):
            self.test_instance.save()

    def test_model_deletion(self):
        instance_id = self.test_instance.id
        instance_name = self.test_instance.name

        # Delete the model
        self.test_instance.delete()

        # Try getting the deleted model by ID
        with self.assertRaises(ObjectDoesNotExist):
            TeamCategory.objects.get(id=instance_id)

        # Try getting the deleted model by name
        with self.assertRaises(ObjectDoesNotExist):
            TeamCategory.objects.get(name=instance_name)
