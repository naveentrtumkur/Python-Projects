########## Sample Dictionary search proram using web URL ############

import re
import urllib.request

url = "http://dictionary.reference.com/browse/"
try:
    word = input("Enter your word:")

    url = url + word

    data = urllib.request.urlopen(url).read()
    data1 = data.decode("utf-8")

    #print(data1)

    m = re.search('meta name="description" content="', data1)
    start = m.end()
    end = start + 300

    newString = data1[start:end]

    #print(newString)

    m = re.search("See more.", newString)
    end = m.start() - 1

    defn  = newString[0:end]

    print(defn)

except:
    print("Your word was not found in dictionary")
