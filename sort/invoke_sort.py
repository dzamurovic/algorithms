import sys
import inspect
import random
import bubble_sort
import selection_sort
import insertion_sort

def __generate_int_list(start, end):
	unsorted = range(start, end)
	random.shuffle(unsorted)
	return unsorted

def __list_to_string(list):
	list_str = ""
	for el in list:
		list_str = list_str + "%d " % el
	return list_str

def __resolve_algorithm(alg_name):
	sort_function = None
	if "bubble" == alg_name:
		sort_function = bubble_sort.sort
	elif "selection" == alg_name:
		sort_function = selection_sort.sort
	elif "insertion" == alg_name:
		sort_function = insertion_sort.sort
	else:
		sort_function = None
	
	return sort_function

def __check_input_args(args):
	return len(args) == 2

def __print_usage_and_exit():
	print "Usage: python -m sort.invoke_sort sort_algorithm"
	sys.exit(1)

if __name__ == "__main__":
	if not __check_input_args(sys.argv):
		__print_usage_and_exit()

	sort_algorithm = __resolve_algorithm(sys.argv[1])
	if not sort_algorithm is None:
		print "Invoking %s.%s" % (inspect.getmodule(sort_algorithm).__name__, sort_algorithm.__name__)

		unsorted = __generate_int_list(1, 10)
		print "Input: %s" % __list_to_string(unsorted)

		sorted_asc = sort_algorithm(unsorted, "asc")
		print "Output (asc): %s" % __list_to_string(sorted_asc)

		sorted_desc = sort_algorithm(unsorted, "desc")
		print "Output (desc): %s" % __list_to_string(sorted_desc)
	else:
		print "Unknown sorting algorithm requested."
