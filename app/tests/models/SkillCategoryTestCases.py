from django.test import TestCase
from app.models.SkillCategory import SkillCategory
from django.db.utils import DataError
from django.core.exceptions import ObjectDoesNotExist


class SkillCategoryTestCases(TestCase):
    """
    Test SkillCategory model
    """

    def setUp(self):
        # Create a new SkillCategory to start the test
        self.test_instance = SkillCategory.objects.create(
            category="web design", description="book"
        )

    def test_model_creation(self):
        # Get the created instance from the database
        instance = SkillCategory.objects.get(category="web design")
        # Test names are the same
        self.assertEqual(instance.category, "web design")
        self.assertEqual(instance.description, "book")

    def test_model_update_description(self):
        self.test_instance.description = "cat"
        self.test_instance.save()
        self.assertEqual(self.test_instance.description, "cat")

    def test_model_update_category(self):
        self.test_instance.category = "dog"
        self.test_instance.save()
        self.assertEqual(self.test_instance.category, "dog")

    def test_model_category_char_limit(self):
        self.test_instance.category = "Admin" * 2001
        with self.assertRaises(DataError):
            self.test_instance.save()

    def test_model_deletion(self):
        instance_id = self.test_instance.id

        # Delete the model
        self.test_instance.delete()

        # Try getting the deleted model by ID
        with self.assertRaises(ObjectDoesNotExist):
            SkillCategory.objects.get(id=instance_id)
