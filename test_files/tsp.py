from tsp_solver.greedy import solve_tsp
import time

def main():
    """pr2392 real file in https://github.com/czajkovsky/tsp/blob/master/in/pr2392.in"""
    try:
        print "Leyendo archivo..."
        start_time = time.time()
        f = open("data/pr2392.in", "r")
        l = f.readline()
        D = []
        for l in f.readlines():
            D.append(map(float, l.split()))
        print("--- %s seconds ---" % str(time.time() - start_time))
        band = True
    except Exception, e:
        print e
        band = False
    if band:
        print "Buscando la ruta mas corta para el viajero..."
        try:
            start_time = time.time()
            path = solve_tsp( D )
            print("---Ruta encontrada en %s seconds ---" % str(time.time() - start_time))
        except Exception, e:
            print "\n[ERROR]: %s\n" % e
            path = None
        if path:
            print "\nsolution:", path
        else:
            print "Ocurrio un error"

if __name__ == '__main__':
    main()
