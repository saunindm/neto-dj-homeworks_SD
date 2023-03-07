import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from django.urls import reverse
from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


# проверка получения первого курса (retrieve-логика)
@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    courses = course_factory(_quantity=10)
    url = reverse('courses-list')
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == courses[0].id


# проверка получения списка курсов (list-логика):
@pytest.mark.django_db
def test_get_courses_list(client, course_factory):
    courses = course_factory(_quantity=10)
    url = reverse('courses-list')
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)


# проверка фильтрации списка курсов по id
@pytest.mark.django_db
def test_filter_course_by_id(client, course_factory):
    courses = course_factory(_quantity=10)
    url = reverse('courses-list')
    for i, c in enumerate(courses):
        response = client.get(url, data={'id': c.id})
        assert response.status_code == 200
        data = response.json()
        assert data[0]['id'] == c.id


# проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_filter_course_by_name(client, course_factory):
    courses = course_factory(_quantity=10)
    url = reverse('courses-list')
    for i, c in enumerate(courses):
        response = client.get(url, data={'name': c.name})
        assert response.status_code == 200
        data = response.json()
        assert data[0]['name'] == c.name


# тест успешного создания курса
@pytest.mark.django_db
def test_create_course(client):
    url = reverse('courses-list')
    response = client.post(url, data={'name': 'course-name'})
    assert response.status_code == 201  # проверка кода
    data = response.json()
    assert data['name'] == 'course-name'


# тест успешного обновления курса
@pytest.mark.django_db
def test_update_courses(client, course_factory):
    course = course_factory(_quantity=1)
    url = reverse('courses-detail', args=[course[0].id])
    response = client.patch(url, data={'name': 'new-course-name'})
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'new-course-name'


# тест успешного удаления курса
@pytest.mark.django_db
def test_delete_courses(client, course_factory):
    courses = course_factory(_quantity=2)
    url = reverse('courses-detail', args=[courses[0].id])
    response = client.delete(url, data={'id': courses[0].id})
    assert response.status_code == 204
    assert Course.objects.count() == len(courses) - 1


# тест ограничения числа студентов на курсе
@pytest.mark.parametrize("count", [19, 21])
def test_with_specific_settings(count, settings):
    settings.MAX_STUDENTS_PER_COURSE = 20
    assert count <= settings.MAX_STUDENTS_PER_COURSE
