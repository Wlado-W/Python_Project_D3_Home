#from news.models import *
#Создаем пользоватлей и авторов
#user1 = User.objects.create(username='User1', first_name='Test1')
#Author.objects.create(authorUser=user1)
#user2 = User.objects.create(username='User2', first_name='Test2')
#Author.objects.create(authorUser=user2)
#Создаем категории
#Category.objects.create(name='IT')
#Category.objects.create(name='Education')
#Category.objects.create(name='Politics')
#Category.objects.create(name='Technology')
#Создаем статьи и новости
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='User1')), categoryType='NW', title='News1', text='This is a news.')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='User1')), categoryType='AR', title='Article 1', text='This is an article.')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='User2')), categoryType='NW', title='News2', text='This is different news.')
Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='User2')), categoryType='AR', title='Article 2', text='This is another article.')
#Получаем обьекты статей
p1 = Post.objects.get(pk=1)
p2 = Post.objects.get(pk=2)
p3 = Post.objects.get(pk=3)
p4 = Post.objects.get(pk=4)
#Получаеи обьекты категорий
c1 = Category.objects.get(name='IT')
c2 = Category.objects.get(name='Education')
c3 = Category.objects.get(name='Politics')
c4 = Category.objects.get(name='Technology')
#Добавляем категории к статьям
p1.postCategory.add(c1)
p2.postCategory.add(c1, c2, c3, c4)
p3.postCategory.add(c3, c2)
p4.postCategory.add(c4)
#Создаем комментарии
Comment.objects.create(commentUser=User.objects.get(username='User1'), commentPost = Post.objects.get(pk=1), text='comment text1')
Comment.objects.create(commentUser=User.objects.get(username='User2'), commentPost = Post.objects.get(pk=1), text='comment text2')
Comment.objects.create(commentUser=User.objects.get(username='User1'), commentPost = Post.objects.get(pk=2), text='comment text1')
Comment.objects.create(commentUser=User.objects.get(username='User2'), commentPost = Post.objects.get(pk=3), text='comment text1')
Comment.objects.create(commentUser=User.objects.get(username='User2'), commentPost = Post.objects.get(pk=4), text='comment text1')
#Рейтинги обьктов
#Post.objects.get(pk=1).like()
#Post.objects.get(pk=1).like()
#Post.objects.get(pk=1).like()
#Post.objects.get(pk=1).like()
#Post.objects.get(pk=2).like()
#Post.objects.get(pk=2).like()
#Post.objects.get(pk=2).like()
#Post.objects.get(pk=2).like()
#Post.objects.get(pk=3).like()
#Post.objects.get(pk=3).like()
#Post.objects.get(pk=4).dislike()
#Post.objects.get(pk=2).dislike()
#Post.objects.get(pk=1).dislike()
#Comment.objects.get(pk=1).like()
#Comment.objects.get(pk=1).like()
#Comment.objects.get(pk=1).dislike()
#Comment.objects.get(pk=2).like()
#Comment.objects.get(pk=2).like()
#Comment.objects.get(pk=2).like()
#Comment.objects.get(pk=2).dislike()
#Comment.objects.get(pk=3).like()
#Обновляем рейтинг авторов
#Author.objects.get(authorUser = User.objects.get(username="User1")).update_rating()
#Author.objects.get(authorUser = User.objects.get(username="User2")).update_rating()
#a = Author.objects.get(authorUser = User.objects.get(username="User1"))
#b = Author.objects.get(authorUser = User.objects.get(username="User2"))
#a.ratingAuthor
#b.ratingAuthor
#Выводим информацию о лучшем авторе
#Author.objects.get(authorUser = User.objects.get(username="User1")).ratingAuthor
#best = Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor') [0]
#print(best)


