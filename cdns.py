import requests
import time
import sys
import uuid


urls = {
	'microsoft': 'https://ajax.aspnetcdn.com/ajax/jQuery/jquery-2.1.4.min.js',
	'google': 'https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js',
	'jquery': 'https://code.jquery.com/jquery-2.1.4.min.js',
	'cdnjs': 'https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js',
}

if __name__ == "__main__":
	url = urls[sys.argv[1]]
	duration = int(sys.argv[2])

	print "Requesting %s for %s seconds" % ( url, duration )

	count = 0
	time_so_far = 0
	start_time = time.time()
	while True:
		time_so_far = time.time() - start_time

		if(time_so_far >= duration):
			break

		u = "%s?rand=%s" % ( url, str(uuid.uuid4().get_hex().upper()[0:6]))
		js = requests.get(u)
		count += 1

		# if(count % 5 == 0):
			# print "Requested %s times" % count

	print "Requested %s times (%ss per request)" % ( count, time_so_far / count )