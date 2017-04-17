countries = [x.strip() for x in open("0. funda_list.csv").readlines()]


shfile = open("3. funda_for_all.sh", "w")
for x in countries:
	print "generating funda bash command for %s" % x
	shfile.write("echo 'matching %s' \n" % x)
	shfile.write("python '1. main.py' funda %s \n" % x)

