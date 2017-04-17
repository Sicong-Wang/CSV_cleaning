countries = [x.strip() for x in open("0. shrout_list.csv").readlines()]


shfile = open("3. shrout_for_all.sh", "w")
for x in countries:
	print "generating shrout bash command for %s" % x
	shfile.write("echo 'matching %s' \n" % x)
	shfile.write("python '1. main.py' shrout %s \n" % x)

