#comments
#jeepney fare
#user would input their name
#if user is student, student discount mus be applied
#20% discount on student, if not student no discount

name = input('input your name -->')
isStudent = input('Are you a student (yes/no) -->')
fare = eval(input('bayad -->'))

if isStudent == 'yes' :
	discount = fare *2
	new_fare = fare - discount
	print('Hi', name, 'student discount is', discount, 'Discounted fare is', new_fare)
else: 
	print('Sorry',name,' you are  not eligible for student discount')