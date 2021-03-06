
from googlesearch import search
import os

url="https://www.google.com/search?sxsrf=ALeKk02AwiAJq-2dDPSYoO8s4s8Pj3kI2w%3A1614877297448&ei=cRJBYJX0GrbZz7sP0rSggAI&"
user_agent={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Charset":"ISO-8859-1,utf-8;q=0.7,*;q=0.3",
            "Accept-Encoding": "none",
            "Accept-Language":"en-US,en;q=0.8"}

#websites="list_of_websites"
def folderList ():
    if not os.path.exists("list_of_websites.txt"):
        xy=open("list_of_websites.txt","w")
        #xy.close()
    search_websites()
def search_websites():
    data=input("What do you want to search? Ans:-")
    no_of_websites=int(input("How many websites do you want? Ans:-"))
    j=0
    list_of_websites=[]
    xy = open("list_of_websites.txt", "a")
    xy.write("NEW SEARCH RESULT")
    for i in search(data, tld="com",num=no_of_websites, stop=no_of_websites, pause=2):
        list_of_websites.append(i)
        xy = open("list_of_websites.txt", "a")
        xy.write(f"\n{j+1} : {i} ")
        xy.close()
        print(j+1,":",i)
        j+=1
    print(list_of_websites)




folderList()
