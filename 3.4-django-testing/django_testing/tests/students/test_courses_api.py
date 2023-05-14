import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


BASE_URL = '/api/v1/courses/'

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student():
    return Student.objects.create(name='ivanov')

@pytest.fixture
def course(student):
    course = Course.objects.create(name='Python')
    course.students.add(student)
    return course


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

# @pytest.mark.django_db
# def test_get_courses(client):
#     # arrange
#     #client = APIClient()
#     st=Student.objects.create(name = 'ivanov', birth_date = '2000-06-12')
#     print(st.id)
#     #Course.objects.create(name = 'python', students = st)
#     Course.objects.create(name='python2', )
#     #print(client)
#
#     # act
#     response = client.get('/api/v1/courses/')
#     #print(response.status_code)
#
#
#     # assert
#
#     assert response.status_code==200
#     data = response.json()
#     assert len(data) == 1
#     assert data[0]['name']=='python2'
#     #assert 1 == 1
#
# @pytest.mark.django_db
# def test_create_courses(client):
#     response = client.post('/api/v1/courses/', data={'name':'python2'}, format='json')
#
#     assert response.status_code == 201

@pytest.mark.django_db
def test_get_retrieve(client, student, course):
    #response = client.get(BASE_URL + '1/')
    response = client.get(f'{BASE_URL}{course.id}/')
    #response = client.get(BASE_URL+course.id+'/')

    assert response.json()['id'] == 1
    assert response.status_code == 200

@pytest.mark.django_db
def test_get_list(client, student, course_factory):
    courses = course_factory(_quantity=5)
    response = client.get(BASE_URL)

    assert response.status_code == 200
    assert len(response.json()) == len(courses)
    for i, course in enumerate(response.json()):
        assert course['name'] == courses[i].name

@pytest.mark.django_db
def test_get_id_filter(client, course_factory):
    course = course_factory(_quantity=5)

    response = client.get(f'{BASE_URL}?id={course[4].id}')
    data = response.json()

    assert response.status_code == 200
    assert data[0]['name'] == course[4].name

@pytest.mark.django_db
def test_get_name_filter(client, course_factory):
    course = course_factory(_quantity=5)

    response = client.get(f'{BASE_URL}?name={course[4].name}')
    data = response.json()

    assert response.status_code == 200
    assert data[0]['name'] == course[4].name

@pytest.mark.django_db
def test_post_create(client, student):
    response = client.post(BASE_URL, data={'name': 'python', 'students': [student.id]})

    assert response.json()['id'] == 17
    assert response.status_code == 201


@pytest.mark.django_db
def test_patch_update(client, course_factory):
    course = course_factory(_quantity=1)
    data = {
        'name': 'new_name',
    }

    response = client.patch(f'{BASE_URL}{course[0].id}/', data=data)
    test_response = client.get(f'{BASE_URL}{course[0].id}/')
    resp_data = test_response.json()

    assert response.status_code == 200
    assert test_response.status_code == 200
    assert resp_data['name'] == data['name']


@pytest.mark.django_db
def test_delete_delete(client, course_factory):
    course = course_factory(_quantity=1)

    response = client.delete(f'{BASE_URL}{course[0].id}/')
    test_response = client.get(f'{BASE_URL}{course[0].id}/')

    assert response.status_code == 204
    assert test_response.status_code == 404


# @pytest.mark.parametrize(
#     ['data', 'expected_code'],
#     (
#         ({
#             'name': 'test_course',
#             'students': 11,
#         }, 400),
#         ({
#             'name': 'test_course',
#         }, 201),
#     )
# )
#
# @pytest.mark.django_db
# def test_post_limit(client, settings, data, expected_code):
#     settings.MAX_STUDENTS_PER_COURSE = 0
#
#     response = client.post(BASE_URL, data=data)
#
#     assert response.status_code == expected_code