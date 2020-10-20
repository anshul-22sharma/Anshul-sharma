
def index(request):

	# products = Product.get_all_products();
	products = None
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
	
	return render(request,'index.html',data)



def validateCustomer(customer):
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



def registerUser(request):
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

	error_message = validateCustomer(customer)


		# if(not first_name):
		# 	error_message = "First Name required !!"

		# elif len(first_name) < 4:
		# 	error_message = "First Name must be 4 char long or more"

		# elif not last_name:
		# 	error_message = "Last Name required !!"

		# elif len(last_name) < 4:
		# 	error_message = "Last Name must be 4 char long or more"

		# elif not phone:
		# 	error_message = "Last Name required !!"

		# elif len(phone) < 10:
		# 	error_message = " Phone Number must be 4 char long"

		# elif len(password) < 5:
		# 	error_message = " Password must be 6 char long"

		# elif len(email) < 5:
		# 	error_message = " Email must be 4 char long"

		# # email validation == agar email same rahga toh singup nhi hoga error show kr dega
		# #  
		  
		# elif customer.isExists():
		# 	error_message = "Email Address Already Register..."
	

		# saving

	if not error_message:

		print(first_name, last_name, phone, email, password)

			# customer = Customer(first_name = first_name,
			# 					last_name = last_name,
			# 					phone = phone,
			# 					email = email,
			# 					password = password ) 
			
		customer.password = make_password(customer.password)
		customer.register()	
		return redirect('index')

		# return HttpResponse(request.POST.get('email'))

	else:
			# return HttpResponse("Signup Sucessfully")

		data = {
			'error':error_message,
			'values':value
		}

		return render(request,'signup.html',data)
        

def signup(request):
	# print(request.method)
	if request.method == 'GET':
		return render(request,'signup.html')
	else:
		return registerUser(request)

        
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


