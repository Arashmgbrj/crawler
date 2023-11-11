from bs4 import BeautifulSoup
import requests
class Main:
    def Crawler(self):
        out_tag_a = []
        all_a_tag = [""]
        src = []
        while True:
         request = requests.get('https://arshiyanet.ir/'+all_a_tag[0])
         soup = BeautifulSoup(request.text,'html.parser')
         find_all_a_href = soup.find_all('a',href=True)
         for i in find_all_a_href:
             i['href']
             if i['href'] in all_a_tag:
                pass
             elif i['href'] in out_tag_a:
                pass
             else:
                all_a_tag.append(i['href'])
         out_tag_a.append(all_a_tag[0])
         all_a_tag.pop(0)
         image = soup.find_all('img')
         for i in image:
             src.append(i['src'])
         
         if len(all_a_tag) == 0:
            break
        print(src)
        print(out_tag_a)
            
if __name__ == "__main__":
   bot = Main()
   bot.Crawler()