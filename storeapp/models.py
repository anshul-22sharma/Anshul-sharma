from django.db import models
from django.conf import settings 


class Category(models.Model):

	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

	@staticmethod
	def get_all_categories():
		return Category.objects.all()


class Product(models.Model):
	name        = models.CharField(max_length=100)
	description = models.TextField(default='',null=True,blank=True)
	price       = models.IntegerField()
	image       = models.ImageField(upload_to='products/')
	category    = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)

	def __str__(self):
		return self.name

	@staticmethod
	def get_all_products():
		return Product.objects.all()

	

			# category id ko get krna ho toh aise bhi kr skthe hai bina java script ke
			
	@staticmethod
	def get_all_products_by_categoryid(category_id):
		if category_id:
			return Product.objects.filter(category=category_id)
		else:
			return Product.get_all_products();


class Customer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name  = models.CharField(max_length=50)
	phone      = models.CharField(max_length=15)
	email      = models.EmailField()
	password   = models.CharField(max_length=500)

	def __str__(self):
		return self.first_name

	def register(self):
		self.save() 

	@staticmethod 
	def get_customer_by_email(email):

		try:
			return Customer.objects.get(email=email)
		except:
			return False


	def isExists(self):
		if Customer.objects.filter(email= self.email):
			return True
		return False




	

	

