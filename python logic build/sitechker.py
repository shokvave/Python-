#import urllib
#use urllin.request
#write a function that takes a url and then returns a response


import urllib.request as urllib




def main(url):
    print("checking connectivity")

    response = urllib.urlopen(url)
    print("connected to ", url , "succesfully")
    print("the response code was:", response.getcode())

print("this is a site connectivity checker program")
input_url = input("enter url of site that you want to check: ")

main(input_url)