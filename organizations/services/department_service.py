from organizations.models import Department


def is_descendant(parent, child):
    """
    Проверяет является ли parent потомком child
    """
    while parent:
        if parent == child:
            return True
        parent = parent.parent
    return False


def move_department(department_id, new_parent_id):

    department = Department.objects.get(id=department_id)

    if new_parent_id:
        new_parent = Department.objects.get(id=new_parent_id)

        # защита от перемещения в самого себя
        if department == new_parent:
            raise ValueError("Cannot move department into itself")

        # защита от циклов
        if is_descendant(new_parent, department):
            raise ValueError("Cannot move department into its child")

        department.parent = new_parent

    else:
        department.parent = None

    department.save()

    return department


def build_department_tree(department):
    return {
        "id": department.id,
        "name": department.name,
        "employees": [e.name for e in department.employees.all()],
        "children": [
            build_department_tree(child)
            for child in department.children.all()
        ]
    }