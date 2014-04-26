__author__ = 'Dan'


def main(argv):

    fn = str(argv[1])
    f = open(fn, 'r')

    num_cases = f.readline()

    case_input = f.readline().split()

    grid_width = int(case_input[0])
    grid_height = int(case_input[1])
    wg = float(case_input[2])
    wh = float(case_input[3])

    print 'hello'
    print num_cases
    print case_input
    print grid_width
    print grid_height
    print wg
    print wh
