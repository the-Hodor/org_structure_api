from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="departments"
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children"
    )

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="employees"
    )

    def __str__(self):
        return self.name