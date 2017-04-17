countries = [x.strip() for x in open("0. trial_list.csv").readlines()]


shfile = open("3. trial_for_all.sh", "w")
for x in countries:
	print "generating trial bash command for %s" % x
	shfile.write("echo 'matching %s' \n" % x)
	shfile.write("python '1. main.py' trial %s \n" % x)

