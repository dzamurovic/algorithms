def sort(unsorted, order):
	sorted = None

	if order == "asc":
		sorted = __do_selection_sort_asc(unsorted, 0)
	if order == "desc":
		sorted = __do_selection_sort_desc(unsorted, 0)

	return sorted

def __find_min_val_idx(unsorted, start_idx):
	idx = start_idx
	min_val_idx = start_idx
	min_val = unsorted[min_val_idx]

	while idx < len(unsorted):
		if unsorted[idx] < min_val:
			min_val = unsorted[idx]
			min_val_idx = idx
		idx += 1

	return min_val_idx

def __find_max_val_idx(unsorted, start_idx):
	idx = start_idx
	max_val_idx = start_idx
	max_val = unsorted[max_val_idx]

	while idx < len(unsorted):
		if unsorted[idx] > max_val:
			max_val = unsorted[idx]
			max_val_idx = idx
		idx += 1

	return max_val_idx

def __do_selection_sort_asc(unsorted, start_idx):
	to_sort = unsorted
	
	idx = start_idx
	if idx < len(to_sort):
		min_val_idx = __find_min_val_idx(to_sort, idx)

		temp = to_sort[min_val_idx]
		to_sort[min_val_idx] = to_sort[idx]
		to_sort[idx] = temp

		idx += 1
		__do_selection_sort_asc(to_sort, idx)

	return to_sort


def __do_selection_sort_desc(unsorted, start_idx):
	to_sort = unsorted
	
	idx = start_idx
	if idx < len(to_sort):
		max_val_idx = __find_max_val_idx(to_sort, idx)

		temp = to_sort[max_val_idx]
		to_sort[max_val_idx] = to_sort[idx]
		to_sort[idx] = temp

		idx += 1
		__do_selection_sort_desc(to_sort, idx)

	return to_sort
