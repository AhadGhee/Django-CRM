from django.db import models  # Import Django's models module to define database tables

# Define a database model named Record
class Record(models.Model):
    # Automatically store the date & time when a record is created
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)

    # Basic contact information fields
    first_name = models.CharField(max_length=50)   
    last_name = models.CharField(max_length=50)   
    email = models.CharField(max_length=100)       
    phone = models.CharField(max_length=15)       
    address = models.CharField(max_length=100)     
    city = models.CharField(max_length=50)         
    state = models.CharField(max_length=50)        
    zipcode = models.CharField(max_length=10)      

    # This method defines how the object is displayed as a string
    def __str__(self):
        # When you print a Record object, it will show "FirstName LastName"
        return f"{self.first_name} {self.last_name}"