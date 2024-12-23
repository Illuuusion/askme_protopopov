from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app.models import Profile, Question, Answer, Tag, QuestionLike, AnswerLike
from faker import Faker
from django.db import IntegrityError
import random


class Command(BaseCommand):
    help = "Fill the database with test data"

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='Ratio of data population')

    def handle(self, *args, **options):
        fake = Faker()
        ratio = options['ratio']

        users = []
        for _ in range(ratio):
            while True:
                username = fake.user_name()
                try:
                    user = User.objects.create_user(username=username)
                    users.append(user)
                    break
                except IntegrityError:
                    continue

        profiles = [Profile(user=user, avatar=None) for user in users]
        Profile.objects.bulk_create(profiles)

        tags = [Tag(name=fake.word()) for _ in range(ratio)]
        Tag.objects.bulk_create(tags)

        questions = []
        for _ in range(ratio * 10):
            question = Question(
                title=fake.sentence(),
                text=fake.text(),
                author=random.choice(users)
            )
            questions.append(question)
        Question.objects.bulk_create(questions)

        for question in questions:
            question.tags.add(*random.sample(tags, random.randint(1, 5)))

        answers = []
        for _ in range(ratio * 100):
            answer = Answer(
                question=random.choice(questions),
                author=random.choice(users),
                text=fake.text(),
                is_accepted=random.choice([True, False])
            )
            answers.append(answer)
        Answer.objects.bulk_create(answers)

        question_likes = []
        for _ in range(ratio * 200):
            user = random.choice(users)
            question = random.choice(questions)
            if not QuestionLike.objects.filter(user=user, question=question).exists():
                question_like = QuestionLike(user=user, question=question)
                question_likes.append(question_like)
        QuestionLike.objects.bulk_create(question_likes)

        answer_likes = []
        for _ in range(ratio * 200):
            user = random.choice(users)
            answer = random.choice(answers)
            if not AnswerLike.objects.filter(user=user, answer=answer).exists():
                answer_like = AnswerLike(user=user, answer=answer)
                answer_likes.append(answer_like)
        AnswerLike.objects.bulk_create(answer_likes)

        self.stdout.write(self.style.SUCCESS(f'Successfully populated the database with a ratio of {ratio}'))
