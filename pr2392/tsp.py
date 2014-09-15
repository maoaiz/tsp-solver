from tsp_solver.greedy import solve_tsp

def main():
	try:
		f = open("pr2392.in", "r")
		l = f.readline()
		D = []
		for l in f.readlines():
			D.append(l.split())
	except Exception, e:
		print e
	path = solve_tsp( D )
	print "solution:", path

if __name__ == '__main__':
	main()
