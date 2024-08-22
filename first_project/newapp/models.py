from django.db import models

# Create your models here.
class Employee(models.Model):
    empno=models.CharField(max_length=20)
    empname=models.CharField(max_length=100)
    contact=models.CharField(max_length=15)
    salary=models.IntegerField()
    joined=models.DateField(null=True)
    class Meta:
        db_table="employee"
        
    def __str__(self):      
        return f'Name: {self.empname}'
    
'''This tables uses foreign key attribute'''
class Musician(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    instrument=models.CharField(max_length=50)
    
    class Meta:
        db_table="musician"

class Album(models.Model):
    artist=models.ForeignKey(Musician,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    release_date=models.DateField()
    num_stars=models.IntegerField()
    
    class Meta:
        db_table="artists"


'''In the Student Model and Project Model there is Many-To-One Relationship
  It means One Project can be done by more than one student
  but one student only do one project'''
class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Projects(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title}"

    
'''Here we make many-to-many relationship means one field of first table realted to myltiple fields of second table and vice-versa
Suppose we have two tables i.e Publication and Article
One Article may be published in as many Publications
And One Publication can Publish as many articles as they want'''

class Publication(models.Model):
    title=models.CharField(max_length=50)
    
    class Meta:
        ordering=["title"]
        
    def __str__(self):
        return f'{self.title}'

class Article(models.Model):
    headline=models.CharField(max_length=100)
    publications=models.ManyToManyField(Publication)
    
    class Meta:
        ordering=["headline"]
    
    def __str__(self):
        return f'{self.headline}'

'''One-To-One Relationship make use of OneToOneField
   We create two tables i.e Place and Restaurant
   A restaurant is a place
   and a place is associated with a restaurant
   hence we get a one to one relationship'''

class Place(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=80)
    
    def __str__(self):
        return f'{self.name}'
    
class Restaurant(models.Model):
    place=models.OneToOneField(Place,on_delete=models.CASCADE,primary_key=True)
    serve_hot_dogs=models.BooleanField(default=False)
    serve_pizza=models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.place.name} is the restaurant'



    
    
         