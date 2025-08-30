from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from interview.models import Question, Answer


class QuestionsGetPostAPITestCase(APITestCase):
    """
    Класс для тестирования questions/
    """

    """
    Инициализируем тестовый вопрос и путь для обращения
    """
    def setUp(self):
        self.test_question = Question.objects.create(text="Test question")
        self.url = reverse("get_post_question")

    def test_get_questions(self):
        """
        Получение списка моделей Question. В результате получаем status_code=200
        Среди моделей есть экземпляр с тестовым вопросом
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["text"], self.test_question.text)

    def test_get_empty_list_questions(self):
        """
        При отсутствии записей в БД запрос на получение всех моделей Question
        вернёт пустой список
        """
        Question.delete(self.test_question)
        response = self.client.get(self.url)
        self.assertEqual(len(response.data), 0)
        self.assertFalse(
            Question.objects.filter(pk=self.test_question.pk).exists()
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_new_question(self):
        """
        Создание нового экземляра Question с добавление в БД
        """
        data = {"text": "Second test question"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            Question.objects.filter(text="Second test question").exists()
        )

    def test_post_new_question_incorrect_date(self):
        """
        При обращении по пути /questions/ с указанной некорректной датой, метод
        вернёт status_code 400 с описанием ошибки
        """
        data = {"text": "Second test question", "created_at": "2025"}
        response = self.client.post(self.url, data)
        self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_new_question_empty_text(self):
        """
        При обращении по пути /questions/ с незаполненным полем text метод
        вернёт status_code 400 с описанием ошибки
        """
        data = {}
        response = self.client.post(self.url, data)
        self.assertTrue(response.status_code == status.HTTP_400_BAD_REQUEST)
        self.assertTrue(
            response.data["text"][0] == "Question field cannot be empty"
        )


class QuestionsGetDeleteAPITestCase(APITestCase):
    """
    Класс для тестирования questions/id
    """

    """
    Инициализируем тестовый вопрос и ответ, а также путь для обращения
    """
    def setUp(self):
        self.test_question = Question.objects.create(text="Test question")
        self.test_answer = Answer.objects.create(
            question_id=self.test_question,
            text="Test answer",
            user_id="16763be4-6022-406e-a950-fcd5018633ca"
        )
        self.url = reverse(
            "get_delete_questions", kwargs={"id": self.test_question.pk}
        )
        self.incorrect_url = reverse(
            "get_delete_questions", kwargs={"id": 2}
        )

    def test_get_question_with_answers(self):
        """
        Получение модели Question и всех ответов на этот вопрос
        """
        response = self.client.get(self.url)
        self.assertTrue(len(response.data["answers"]), 1)
        self.assertContains(response, "Test answer")

    def test_get_question_with_non_existent_question_id(self):
        """
        Попытка получить модель Question с id, которого нет в БД
        """
        response = self.client.get(self.incorrect_url)
        self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_question_by_id(self):
        """
        Удаление экземпляра Question по id с удалением всех ответов на него
        """
        response = self.client.delete(
            reverse("get_delete_questions", kwargs={
                "id": self.test_question.pk
            })
        )
        self.assertTrue(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Answer.objects.filter(text="Test answer").exists())
        self.assertFalse(Question.objects.filter(text="Test question").exists())

    def test_do_not_delete_question_by_id(self):
        """
        Попытка удалить вопрос с ответами по несуществующему id
        """
        response = self.client.delete(self.incorrect_url)
        self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)


class AnswersPostAPITestCase(APITestCase):
    """
    questions/id/answers/
    """

    """
    Инициализируем тестовый вопрос, а также путь для обращения
    """
    def setUp(self):
        self.test_question = Question.objects.create(text="Test question")
        self.url = reverse(
            "post_answer", kwargs={"id": self.test_question.pk}
        )

    def test_post_answer(self):
        """
        Создание нового ответа
        """
        data = {
            "text": "Test answer",
            "user_id": "123e4567-e89b-12d3-a456-426614174011",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

