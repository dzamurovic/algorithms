def sort(unsorted, order):
	sorted = None

	if order == "asc":
		sorted = __do_insertion_sort_asc(unsorted, 1)
	if order == "desc":
		sorted = __do_insertion_sort_desc(unsorted, 1)

	return sorted

def __do_insertion_sort_asc(unsorted, end_idx):
	to_sort = unsorted

	idx = end_idx
	while idx > 0 and idx < len(unsorted):
		val = to_sort[idx]
		if val < to_sort[idx - 1]:
			temp = to_sort[idx - 1]
			to_sort[idx] = temp
			to_sort[idx - 1] = val

		idx -= 1

	if end_idx < len(to_sort):
		end_idx += 1
		to_sort = __do_insertion_sort_asc(to_sort, end_idx)

	return to_sort

def __do_insertion_sort_desc(unsorted, end_idx):
	to_sort = unsorted

	idx = end_idx
	while idx > 0 and idx < len(unsorted):
		val = to_sort[idx]
		if val > to_sort[idx - 1]:
			temp = to_sort[idx - 1]
			to_sort[idx] = temp
			to_sort[idx - 1] = val

		idx -= 1

	if end_idx < len(to_sort):
		end_idx += 1
		to_sort = __do_insertion_sort_desc(to_sort, end_idx)

	return to_sort