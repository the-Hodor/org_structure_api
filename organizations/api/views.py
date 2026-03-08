from rest_framework import viewsets
from organizations.models import Organization, Department, Employee
from .serializers import OrganizationSerializer, DepartmentSerializer, EmployeeSerializer
from organizations.services.department_service import move_department
from organizations.services.department_service import build_department_tree
from rest_framework.decorators import action
from rest_framework.response import Response

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    @action(detail=True, methods=["get"])
    def structure(self, request, pk=None):
        organization = self.get_object()

        root_departments = organization.departments.filter(parent=None)

        data = {
            "organization": organization.name,
            "departments": [
                build_department_tree(dep)
                for dep in root_departments
            ]
        }

        return Response(data)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    @action(detail=True, methods=["post"])
    def move(self, request, pk=None):
        new_parent_id = request.data.get("parent")

        department = move_department(pk, new_parent_id)

        return Response({
            "id": department.id,
            "name": department.name,
            "parent": department.parent.id if department.parent else None
        })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

