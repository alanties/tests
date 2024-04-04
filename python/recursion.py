#test task
def rec_func(tree, root, end):
	if tree:
		del_elems = []
		if int(root) >= int(end):
			for counter in (range(len(tree))):
				if root != '0':
					tree.append(f'{tree[counter]}+{root}')
					tree.append(f'{tree[counter]}-{root}')
				else:
					tree.append(f'{tree[counter]}+{root}')
				if len(tree[counter][-3:]) != 3 or '+' in tree[counter][-3:] or '-' in tree[counter][-3:]:
					tree.append(tree[counter]+root)
				del_elems.append(tree[counter])
			for elem in del_elems:
				tree.remove(elem)
			rec_func(tree, str(int(root) - 1), end)	
		else:
			res = 0
			num = ''
			prev_sign = ''
			for line in tree:
				for sym in line:
					if sym.isdigit():
						num += sym
					elif sym == '+' or sym == '-':
						if prev_sign == '+' or prev_sign == '':
							res += int(num)
						if prev_sign == '-':
							res -= int(num)
						num = ''
						prev_sign = sym

				res = res + int(num) if prev_sign == '+' else res - int(num)
				if res == 200:
					print('+',line)
				res = 0
				num = ''
				prev_sign = ''
	else:
		tree.append(root)
		rec_func(tree, str(int(root) - 1), end)


if __name__ == "__main__":
	rec_func([], '9', '0')
