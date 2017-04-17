countries = [x.strip() for x in open("0. header_list.csv").readlines()]


shfile = open("3. header_for_all.sh", "w")
for x in countries:
	print "generating header bash command for %s" % x
	shfile.write("echo 'matching %s' \n" % x)
	shfile.write("python '1. main.py' header %s \n" % x)

