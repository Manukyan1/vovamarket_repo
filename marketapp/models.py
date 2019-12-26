from django.db import models

class ad_adding(models.Model):
    item_name = models.CharField(max_length = 150, db_index = True)
    item_price = models.IntegerField()
    tags = models.ManyToManyField('Tag', blank=True, related_name='items_relname')
    slug = models.SlugField(max_length=150, unique = True)
    body = models.TextField(blank = True, db_index = True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.item_name)


class Tag(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('categ_detal_n', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)
