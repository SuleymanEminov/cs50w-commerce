from distutils.command.upload import upload
from pyexpat import model
from django.contrib.auth.models import AbstractUser
from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MinMoneyValidator



class User(AbstractUser):
    def __str__(self) -> str:
        return f"{self.username}"


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.name}"
    


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id")
    title = models.CharField(max_length=64)
    image = models.ImageField(null=True,blank=True)
    description = models.TextField() 
    # price = models.DecimalField(max_digits=11, decimal_places=2)
    price = MoneyField(
        max_digits=14, 
        decimal_places=2, 
        default_currency='USD',
        validators=[
            MinMoneyValidator(0)
        ])
    created_time = models.DateTimeField(auto_now_add=True)
    
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default="No Category Listed", blank=True,related_name='category_id')
    # comments = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_no')
    # bids = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name='bid_no')
    def __str__(self) -> str:
        return f"{self.user}: {self.title}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_comment")

    def __str__(self) -> str:
        return f"{self.id}: {self.user} -- {self.comment}"

class Bid(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_bid')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_bid")
    price = MoneyField(
        max_digits=14, 
        decimal_places=2, 
        default_currency='USD',
        validators=[
            MinMoneyValidator(0)
        ])

