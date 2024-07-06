from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

#STATUS = ((0, "Not Approved"), (1, "Approved"))
class Author(models.Model):
    """
    gives information about the author of the book 
    many authors can have many books, but many books can only have one single author
    Shakespear wrote the Merchant of Venice, Romeo & Juliet and....
    George Orwel wrote Animal Farm, 1984 ...

    """
    fullname = models.CharField(max_length=200, unique=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="add_authors")
    author_image=CloudinaryField('image',default='placeholder')
    place_of_birth=models.CharField(max_length=200)
    date_of_birth=models.DateField()
    short_biography=models.TextField()
    created_on=models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    # metaclass for default view on the admin page
    class Meta:
        ordering =['-created_on','fullname']
    
    def __str__(self):
        #return f"Author: {self.fullname}  added by: {User.get_full_name}. Author born in: {self.place_of_birth} on {self.date_of_birth} | Status: {self.status}"
        return self.fullname
    

class Category(models.Model):
    """
    category will be used to specify the book genre whether it is politics, economics, sociology, thriller,
    """
    category_name=models.CharField(max_length=200, unique=True)
    category_description=models.TextField()

    class Meta:
        ordering =['category_name']
    
    def __str__(self):
        #return f"Author: {self.fullname}  added by: {User.get_full_name}. Author born in: {self.place_of_birth} on {self.date_of_birth} | Status: {self.status}"
        return self.category_name
