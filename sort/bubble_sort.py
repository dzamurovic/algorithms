def sort(unsorted, order):
	sorted = None

	if order == "asc":
		sorted = __do_bubble_sort_asc(unsorted, 0)
	if order == "desc":
		sorted = __do_bubble_sort_desc(unsorted, len(unsorted) - 1)

	return sorted

def __do_bubble_sort_asc(unsorted, end_idx):
	to_sort = unsorted
	idx = len(to_sort) - 1

	while idx > end_idx:
		if to_sort[idx] < to_sort[idx - 1]:
			temp = to_sort[idx]
			to_sort[idx] = to_sort[idx - 1]
			to_sort[idx - 1] = temp
		idx -= 1

	if end_idx < len(to_sort) - 1:
		end_idx += 1
		return __do_bubble_sort_asc(to_sort, end_idx)
	else:
		return to_sort

def __do_bubble_sort_desc(unsorted, end_idx):
	to_sort = unsorted
	idx = 0

	while idx < end_idx:
		if to_sort[idx] < to_sort[idx + 1]:
			temp = to_sort[idx]
			to_sort[idx] = to_sort[idx + 1]
			to_sort[idx + 1] = temp
		idx += 1

	if end_idx > 0:
		end_idx -= 1
		return __do_bubble_sort_desc(to_sort, end_idx)
	else:
		return to_sort