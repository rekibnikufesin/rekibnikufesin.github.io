import os
import re
import urllib
from glob import glob
from urlparse import urlparse

result = [y for x in os.walk(os.getcwd()) for y in glob(os.path.join(x[0], '*.html'))]
for r in result:
    f = open(r,'r')
    #print f
    for line in f:
        # print line
        for match in re.findall(r'<img\s.*src="([a-zA-z:&#;.\-0-9]+)"', line):
            image = match.replace("&#47;", "/")
            print "Downloading " + image
            filename = urlparse(image)
            print os.path.basename(filename.path)
            urllib.urlretrieve(image, "images/" + os.path.basename(filename.path))
