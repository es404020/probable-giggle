from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Genre(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return f"The genre name is {self.name}"

class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name  
    

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)


    class Meta:
        ordering = ['last_name','first_name']

    def get_absolute_url(self):
        return reverse("auth_detail", kwargs={"pk": self.pk})
    

    def __str__(self) -> str:
        return f"{self.first_name} , {self.last_name}"
        

# Create your models here.
class Book(models.Model):
     
     title = models.CharField(max_length=150)
     author =  models.ForeignKey('Author', on_delete=models.SET_NULL,null=True)
     summary = models.TextField(max_length=500)
     isbn = models.CharField('ISBN',max_length=12,unique=True)
     genre = models.ManyToManyField(Genre)
     language = models.ForeignKey('Language',on_delete=models.SET_NULL,null=True)



     def __str__(self) -> str:
         return f"{self.title} {self.author} {self.summary} {self.isbn} {self.genre}"
     
     def get_absolute_url(self):
         return reverse("book_detail", kwargs={"pk": self.pk})
     




import uuid

class BookInstance(models.Model):

    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    book = models.ForeignKey('Book',on_delete=models.RESTRICT,null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True,blank=True)
    borrower = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)


    LOAN_STATUS =(
        ('m','Maintenance'),
        ('o','On Loan'),
        ('a','Available'),
        ('r','Reserved')
    )

    status = models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='m')


    class Meta:
        ordering  = ['due_back']

    def __str__(self) -> str:
        return f"{self.book.title} {self.id}"


