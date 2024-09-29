from rest_framework.viewsets import ModelViewSet
from app.models.SkillCategory import SkillCategory
from app.serializer.SkillCategorySerializer import SkillCategorySerializer


class SkillCategoryViewSet(ModelViewSet):
    queryset = SkillCategory.objects.all()
    serializer_class = SkillCategorySerializer
