from django.db import models
# from store.models import Product
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
# Create your models here.


class TaggedItemManager(models.Manager):
        def get_tags_for(self, obj_type, obj_id):
                content_type = ContentType.objects.get_for_model(obj_type)

                return TaggedItem.objects.select_related('tag').filter(
                        content_type = content_type,
                        object_id = obj_id
                )

class Tag(models.Model):
        label = models.CharField(max_length=255)


class TaggedItem(models.Model):
# what tag applied to what object

        # objects = TaggedItemManager()
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


class LikedItem(models.Model):
        user = models.ForeignKey(User , on_delete=models.CASCADE)
        content_type = models.ForeignKey(ContentType , on_delete=models.CASCADE)
        object_id = models.PositiveBigIntegerField()
        content_object = GenericForeignKey()