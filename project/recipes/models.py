from django.db import models
from django.urls import reverse

# Рецепт
class Recipe(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True, #названия рецептов не должны повторяться
    )
    description = models.TextField()



    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='recipes', # все рецепты в категории будут доступны через поле recipes
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('new_detail', args=[str(self.id)])


# Категория, к которой будет привязываться рецепт
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()
