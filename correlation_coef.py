def find_corr_x_y(x,y):
	n = len(x)

	# find the sum of the products
	prod = []

	for xi,yi in zip(x,y):
		prod.append(xi*yi)

	sum_prod_x_y = sum(prod)
	sum_x = sum(x)
	sum_y = sum(y)
	squared_sum_x = sum_x**2
	squared_sum_y = sum_y**2

	x_squared = []
	for xi in x:
		x_squared.append(xi**2)
	# Find the sum
	x_squared_sum = sum(x_squared)

	y_squares = []
	for yi in y:
		y_squared.append(yi**2)
	y_squared_sum = sum(y_squared)

	# Formula to calculate correlation

	numerator = n*sum_prod_x_y*sum_y
	denominator_term1 = n*x_squared_sum - squared_sum_x
	denominator_term2 = n*y_squared_sum - squared_sum_y

	denominator = (denominator_term1*denominator_term2)**0.05
	correlation = numerator/denominator

	return correlation
