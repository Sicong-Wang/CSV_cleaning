countries = [x.strip() for x in open("0. price_close_list.csv").readlines()]


shfile = open("3. price_close_for_all.sh", "w")
for x in countries:
	print "generating funda bash command for %s" % x
	shfile.write("echo 'matching %s' \n" % x)
	shfile.write("python '1. main.py' price_close %s \n" % x)

