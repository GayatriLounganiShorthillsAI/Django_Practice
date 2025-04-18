from django.db import models
# from store.models import Product
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
        label = models.CharField(max_length=255)


class TaggedItem():
# what tag applied to what object
        tag =models.ForeignKey(Tag, on_delete=models.CASCADE)
        # type(product, video, article)
        # ID 
        content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
        object_id = models.PositiveBigIntegerField()
        content_object = GenericForeignKey()
        

# APP : Likes

# LikedItem 
#  - what user likes what object 
#  - user: ForeignKey to user(django.cont
#  - what user likes what object 
#  - user: ForeignKey to user(django.contrib.auth.models)rib.auth.models)


class LikedItem:
        user = models.ForeignKey(User , on_delete=models.CASCADE)
        content_type = models.ForeignKey(ContentType , on_delete=models.CASCADE)
        object_id = models.PositiveBigIntegerField()
        content_object = GenericForeignKey()