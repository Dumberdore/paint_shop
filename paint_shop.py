#!/usr/local/bin/python3


# 5
# 1 M 3 G 5 G
# 2 G 3 M 4 G
# 5 M

class customer_request:
	def __init__(self):
		self.paint_order = {}
		self.is_satisfied = False

	def removePaint(self, paint_id):
		del self.paint_order[paint_id]

	def _addPaint(self, paint_id, paint_type):
		self.paint_order[paint_id] = paint_type


def find_critical_customers(cust_list):
	critical_custs = []
	for cust in cust_list:
		if len(cust) == 1:
			critical_custs.append(cust)

def satisfy_critical_customers(cust_list, paint_shop_solution):

	for critical_cust in cust_list:
		critical_paint_id = next(itr(critical_cust.paint_order))
		if critical_paint_id not in paint_shop_solution
			paint_shop_solution[critical_paint_id] = critical_cust.paint_order[critical_paint_id]
		else:
			if critical_cust.paint_order[critical_paint_id] != paint_shop_solution[critical_paint_id]:
				return False

		critical_cust.is_satisfied = True

def satisfy_customers_with_critical_demand(cust_list, paint_shop_solution):

	for cust in cust_list:
		for paint_id, paint_type in paint_shop_solution.items():

			if paint_id in cust.paint_order:
				if paint_type == cust.paint_order[paint_id]
					cust.is_satisfied = True

Solution = {}
all_cust_satisfied = False

