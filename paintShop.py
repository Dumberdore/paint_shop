#!/usr/local/bin/python3
import argparse

class Customer:
	cust_id = 0
	request_list = []

	def __init__(self, input_list, record_number):
		self.cust_id = "Cust" + str(record_number)
		self._sortByTypeThenId(input_list)
		self.is_satisfied = False
		self.is_critical = len(input_list) == 1

	def _sortByTypeThenId(self, input_list):

		gloss_list = []
		matt_list = []

		for paint_id, paint_type in input_list.items():
			if paint_type == 'M':
				matt_list.append(paint_id)
			else:
				gloss_list.append(paint_id)

		request_list_gloss = [[x,'G'] for x in sorted(gloss_list)]
		request_list_matt = [[x,'M'] for x in sorted(matt_list)]
		request_list_gloss.extend(request_list_matt)

		self.request_list = request_list_gloss		

	def setSatisfied(self):
		self.is_satisfied = True	

	def __str__(self):
		field_1 = " "
		if self.is_satisfied :
			field_1 = "-"

		field_2 = " "
		if self.is_critical :
			field_2 = "*"

		return field_1 +" "+ field_2 +" " + str(self.cust_id) +" "+str(self.request_list)

class PaintRequested:
	paint_id = 0
	requsts = {}
	is_resolved = False

	def __init__(self, paint_no):
		self.requsts = dict()
		self.paint_id = paint_no

	def addCustomerRequest(self, cust_id, paint_type):
		self.requsts[cust_id] = paint_type

	def __str__(self):
		field_1 = " "
		if self.is_resolved :
			field_1 = "-"

		return field_1 +" "+ str(self.paint_id) +" : "+ str(self.requsts)

class PaintShop:
	solution_set = {}

	def addPaintAndType(self, paint_id, paint_type):
		self.solution_set[paint_id] = paint_type


def print_current_state_of_ds(all_customers, all_paint, solution):

	solution_string = ' '.join([value for (key, value) in sorted(solution.items())])
	print(solution_string)

def satisfy_all_customers_with_ids(all_customers, request_list):
	
	for cust in all_customers:
		if cust.cust_id in request_list:
			cust.setSatisfied()

def remove_conflicts(curr_paint_requsts, remove_list):

	for x in remove_list:
		del curr_paint_requsts[x]

def anyCustUnsatisfied(customer_list):

	for c in customer_list:
		if c.is_satisfied == False:
			return True

	return False # All customer are satisfied

def makeRemainingColorsInGloss(solution_set, no_of_paints):

	for x in range(1,no_of_paints+1):

		if str(x) not in solution_set:
			solution_set[str(x)] = 'G'


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('inputFile', help='Provide input File Path')
	args = parser.parse_args()

	paint_shop = PaintShop()
	paints_to_be_made = 0

	with open(args.inputFile) as f:
		xRequest = f.readlines()
		xRequest = [x.strip() for x in xRequest]
		paints_to_be_made = int(xRequest[0])

	# Form desired Data structures - Paints
	all_paint = {}
	for x in range(1, int(xRequest[0]) + 1):
		curr_paint_requested = PaintRequested(x)
		all_paint[x] = curr_paint_requested

	# Form desired Data structures - Customers
	customer_records = sorted(xRequest[1:], key = len)
	all_customers = []

	for index, customer_record in enumerate(customer_records):
		trimmed_request = customer_record.replace(' ','')
		request_pairs = [trimmed_request[i:i+2] for i in range(0, len(trimmed_request), 2)]
		request_dict = {}
		for paint in request_pairs:
			request_dict[paint[0]] = paint[1]

		curr_customer = Customer(request_dict, index + 1)

		for paint_id, paint_type in curr_customer.request_list:
			(all_paint[int(paint_id)]).addCustomerRequest(curr_customer.cust_id, paint_type)
		
		all_customers.append(curr_customer) 

	print_current_state_of_ds(all_customers, all_paint, paint_shop.solution_set)

	for curr_cust in all_customers:
		if curr_cust.is_satisfied != True:

			for req_paint_id, req_paint_type in curr_cust.request_list:
				curr_paint = all_paint[int(req_paint_id)]

				if (curr_cust.cust_id in curr_paint.requsts):
					if curr_paint.requsts[curr_cust.cust_id] == req_paint_type:

						satisfy_all_customers_with_ids(all_customers, [k for k,v in curr_paint.requsts.items() if v == req_paint_type])
						remove_conflicts(curr_paint.requsts, [k for k,v in curr_paint.requsts.items() if v != req_paint_type])
						paint_shop.addPaintAndType(req_paint_id, req_paint_type)
						break;
					

	if anyCustUnsatisfied(all_customers) :
		print("No solution exists")
		return 1

	makeRemainingColorsInGloss(paint_shop.solution_set, paints_to_be_made)
	print_current_state_of_ds(all_customers, all_paint, paint_shop.solution_set)
	return 0

if __name__ == '__main__':
        main()



