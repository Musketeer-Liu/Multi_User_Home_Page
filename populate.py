# import os
# import random
# import django
# from faker import Faker


# from django.contrib.auth.models import User
# from blog.models import Post, Comment




# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# django.setup()
# fake = Faker()
# USERS = ['A', 'B', 'C', 'D', 'E']


# # def add_user():
# #     u = User.objects.get_or_create(username=random.choice(USERS))[0]
# #     u.save()
# #     return u


# def populate():
#     for user in USERS:
#         author = user
        
#         fake_title = fake.sentence()
#         fake_author = fake.name()
#         fake_text = fake.text()

#         p = Post.objects.get_or_create(author = author, title=fake_title, text=fake_text)[0]
#         c = Comment.objects.get_or_create(post=p, author=fake_author, text=fake_text, approved_comment=True)[0]




# if __name__ == '__main__':
#     print('Population Script:')
#     populate()
#     print()

