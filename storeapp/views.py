from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from .models import *
from django.views import  View

# print(make_password('1234'))
# print(check_password('12345',pbkdf2_sha256$180000$wA5N7x4BsnYH$S6ACkWCoMCpeDIiGzzuX1EGKMTEGaJwGj6bUBVgaAQ8=))

class index(View):

	def post(self, request):
		# import pdb;pdb.set_trace();
		product = request.POST.get('product')
		cart = request.session.get('cart')
		# print(product)

		# cart session create
		

		# anshu = request.session.get('anshu')
		# if anshu:
		# 	if product in anshu:
		# 		anshu[product] += 1
		# 	else:
		# 		anshu[product] = 1
		# else:
		# 	anshu = {}
		# 	anshu[product] = 1
		# 	print("noSession")

		if cart: 
			quantity = cart.get(product)
			if quantity:
				cart[product] = quantity + 1
			else:
				cart[product] = 1  
		else:
			cart = {} 
			cart[product] = 1
		request.session['cart'] = cart
		print('cart', request.session['cart'])
		return redirect('index')

		# request.session['anshu'] = anshu
		# print(request.session['anshu'])
		# return redirect('index')
	
	def get(self, request):

		products = None
		# all session are delete and create a new session jb clear krna ho tb uss krna hain "ONLY"
		# request.session.clear()
		categories = Category.get_all_categories()
		categoryID = request.GET.get('category')	
		
		# print(request.GET)

		# categoryID = request.GET.get('category')

		if categoryID:
			products = Product.get_all_products_by_categoryid(categoryID)
		else:
			products = Product.get_all_products	()

		data = {}

		data['products']=products
		data['categories']= categories  

		# session print in email
		print('you are : ', request.session.get('email'))
		
		return render(request,'index.html',data)



# def index(request):

# 	# products = Product.get_all_products();
# 	products = None
# 	categories = Category.get_all_categories()
# 	categoryID = request.GET.get('category')	
	
# 	# print(request.GET)

# 	# categoryID = request.GET.get('category')

# 	if categoryID:
# 		products = Product.get_all_products_by_categoryid(categoryID)
# 	else:
# 		products = Product.get_all_products	()

# 	data = {}

# 	data['products']=products
# 	data['categories']= categories  

# 	# session print in email
# 	print('you are : ', request.session.get('email'))
	
# 	return render(request,'index.html',data)




# def validateCustomer(customer):
# 	error_message = None

# 	if(not customer.first_name):
# 		error_message = "First Name required !!"

# 	elif len(customer.first_name) < 4:
# 		error_message = "First Name must be 4 char long or more"

# 	elif not customer.last_name:
# 		error_message = "Last Name required !!"

# 	elif len(customer.last_name) < 4:
# 		error_message = "Last Name must be 4 char long or more"

# 	elif not customer.phone:
# 		error_message = "Last Name required !!"

# 	elif len(customer.phone) < 10:
# 		error_message = " Phone Number must be 4 char long"

# 	elif len(customer.password) < 5:
# 		error_message = " Password must be 6 char long"

# 	elif len(customer.email) < 5:
# 		error_message = " Email must be 4 char long"

# 	# email validation == agar email same rahga toh singup nhi hoga error show kr dega
# 	#  
		
# 	elif customer.isExists():
# 		error_message = "Email Address Already Register..."

# 	return error_message





# def registerUser(request):
# 	postData = request.POST

# 	first_name = postData.get('firstname')
# 	last_name  = postData.get('lastname')
# 	phone      = postData.get('phone')
# 	email      = postData.get('email')
# 	password   = postData.get('password')

# 	value = {'first_name' : first_name,
# 			'last_name' : last_name,
# 			'phone' : phone,
# 			'email' : email }


# 		# validation

# 	error_message = None

# 	customer = Customer(first_name = first_name,
# 						last_name = last_name,
# 						phone = phone,
# 						email = email,
# 						password = password ) 

# 	error_message = validateCustomer(customer)


# 		# if(not first_name):
# 		# 	error_message = "First Name required !!"

# 		# elif len(first_name) < 4:
# 		# 	error_message = "First Name must be 4 char long or more"

# 		# elif not last_name:
# 		# 	error_message = "Last Name required !!"

# 		# elif len(last_name) < 4:
# 		# 	error_message = "Last Name must be 4 char long or more"

# 		# elif not phone:
# 		# 	error_message = "Last Name required !!"

# 		# elif len(phone) < 10:
# 		# 	error_message = " Phone Number must be 4 char long"

# 		# elif len(password) < 5:
# 		# 	error_message = " Password must be 6 char long"

# 		# elif len(email) < 5:
# 		# 	error_message = " Email must be 4 char long"

# 		# # email validation == agar email same rahga toh singup nhi hoga error show kr dega
# 		# #  
		  
# 		# elif customer.isExists():
# 		# 	error_message = "Email Address Already Register..."
	

# 		# saving

# 	if not error_message:

# 		print(first_name, last_name, phone, email, password)

# 			# customer = Customer(first_name = first_name,
# 			# 					last_name = last_name,
# 			# 					phone = phone,
# 			# 					email = email,
# 			# 					password = password ) 
			
# 		customer.password = make_password(customer.password)
# 		customer.register()	
# 		return redirect('index')

# 		# return HttpResponse(request.POST.get('email'))

# 	else:
# 			# return HttpResponse("Signup Sucessfully")

# 		data = {
# 			'error':error_message,
# 			'values':value
# 		}

# 		return render(request,'signup.html',data)





			# FUNCTION BASED SIGNUP VIEWS


# def signup(request):
# 	# print(request.method)
# 	if request.method == 'GET':
# 		return render(request,'signup.html')
# 	else:
# 		return registerUser(request)




class signup(View):

	def get(self, request):
		return render(request,'signup.html')

	def post(self, request):

		postData = request.POST

		first_name = postData.get('firstname')
		last_name  = postData.get('lastname')
		phone      = postData.get('phone')
		email      = postData.get('email')
		password   = postData.get('password')

		value = {'first_name' : first_name,
				'last_name' : last_name,
				'phone' : phone,
				'email' : email }

			# validation

		error_message = None

		customer = Customer(first_name = first_name,
							last_name = last_name,
							phone = phone,
							email = email,
							password = password ) 

			# change kara hai class based views self pass krke

		error_message = self.validateCustomer(customer)


		if not error_message:

			print(first_name, last_name, phone, email, password)

			customer.password = make_password(customer.password)
			customer.register()	
			return redirect('index')


		else:
				# return HttpResponse("Signup Sucessfully")

			data = {
				'error':error_message,
				'values':value
			}

			return render(request,'signup.html',data)



	def validateCustomer(self,customer):
		error_message = None

		if(not customer.first_name):
			error_message = "First Name required !!"

		elif len(customer.first_name) < 4:
			error_message = "First Name must be 4 char long or more"

		elif not customer.last_name:
			error_message = "Last Name required !!"

		elif len(customer.last_name) < 4:
			error_message = "Last Name must be 4 char long or more"

		elif not customer.phone:
			error_message = "Last Name required !!"

		elif len(customer.phone) < 10:
			error_message = " Phone Number must be 4 char long"

		elif len(customer.password) < 5:
			error_message = " Password must be 6 char long"

		elif len(customer.email) < 5:
			error_message = " Email must be 4 char long"

	# email validation == agar email same rahga toh singup nhi hoga error show kr dega
	#  
			
		elif customer.isExists():
			error_message = "Email Address Already Register..."

		return error_message

		






		# return HttpResponse('Reeceived Post Request')

		# postData = request.POST

		# first_name = postData.get('firstname')
		# last_name  = postData.get('lastname')
		# phone      = postData.get('phone')
		# email      = postData.get('email')
		# password   = postData.get('password')  

		# value = {'first_name' : first_name,
		# 		'last_name' : last_name,
		# 		'phone' : phone,
		# 		'email' : email }

		# # validation
		# error_message = None

		# customer = Customer(first_name = first_name,
		# 					last_name = last_name,
		# 					phone = phone,
		# 					email = email,
		# 					password = password ) 

		# error_message = validateCustomer(customer)


		# # if(not first_name):
		# # 	error_message = "First Name required !!"

		# # elif len(first_name) < 4:
		# # 	error_message = "First Name must be 4 char long or more"

		# # elif not last_name:
		# # 	error_message = "Last Name required !!"

		# # elif len(last_name) < 4:
		# # 	error_message = "Last Name must be 4 char long or more"

		# # elif not phone:
		# # 	error_message = "Last Name required !!"

		# # elif len(phone) < 10:
		# # 	error_message = " Phone Number must be 4 char long"

		# # elif len(password) < 5:
		# # 	error_message = " Password must be 6 char long"

		# # elif len(email) < 5:
		# # 	error_message = " Email must be 4 char long"

		# # # email validation == agar email same rahga toh singup nhi hoga error show kr dega
		# # #  
		  
		# # elif customer.isExists():
		# # 	error_message = "Email Address Already Register..."
	

		# # saving

		# if not error_message:

		# 	print(first_name, last_name, phone, email, password)

		# 	# customer = Customer(first_name = first_name,
		# 	# 					last_name = last_name,
		# 	# 					phone = phone,
		# 	# 					email = email,
		# 	# 					password = password ) 
			
		# 	customer.password = make_password(customer.password)
		# 	customer.register()	
		# 	return redirect('index')

		# # return HttpResponse(request.POST.get('email'))

		# else:
		# 	# return HttpResponse("Signup Sucessfully")

		# 	data = {
		# 		'error':error_message,
		# 		'values':value
		# 	}

		# 	return render(request,'signup.html',data)




				# LOGIN FUNCTION VIEWS 

# def login(request):
# 	if request.method == 'GET':
# 		return render(request,'login.html')

# 	else:
# 		import pdb;pdb.set_trace()
# 		email    = request.POST.get('email')
# 		password = request.POST.get('password')
# 		customer = Customer.get_customer_by_email(email)
# 		error_message = None
# 		# print(customer)
# 		# print(email,password)


# 		if customer:
# 			flag = check_password(password,customer.password)
# 			if flag:
# 				return redirect('index')
			
# 			else:
# 				error_message = 'Email or Password invalid !!...'
# 		else:
# 			error_message = 'Email or Password invalid !!...'
			
# 		print(email,password)
# 		return render(request,'login.html',{'error': error_message})



		# LOGIN USED BY CLASS BASED VIEWS

class loginview(View):

	def get(self, request):
		return render(request,'login.html')

	def post(self, request):

		email    = request.POST.get('email')
		password = request.POST.get('password')
		customer = Customer.get_customer_by_email(email)
		error_message = None
		# print(customer)
		# print(email,password)


		if customer:
			flag = check_password(password,customer.password)
			if flag:
				# session used
				request.session['customer_id'] = customer.id
				request.session['email'] = customer.email
				return redirect('index')
			
			else:
				error_message = 'Email or Password invalid !!...'
		else:
			error_message = 'Email or Password invalid !!...'
			
		print(email,password)
		return render(request,'login.html',{'error': error_message})







