print("start")
import requests
import threading
from random import randint
def make_request(url):
    """Makes a GET request to the given URL and prints the response status code."""
    try:
        
        response = requests.get(url)
        print("proxy" in response.text, "proxy")
        
    except requests.exceptions.RequestException as e:
        print(f"Error for URL {url}: {e}")

def main():
    """Creates and starts 10 threads to make requests to different URLs."""
    #urls = [
       #f"https://api.webscrapingapi.com/v1?api_key=d6jZT9oiMvCTSYIfSz51g81Fm0rnHJdh&url=https%3A%2F%2Fwww.effectiveratecpm.com%2Fwmbx23g2%3Fkey%3Db7a4029a74caece5dba8ed3619263305&render_js=1&wait_until=networkidle0&wait_for={randint(5000, 8000)}"
   # for _ in range(randint(10, 20))]
    #p =["104.207.54.151:3128","45.202.77.233:3128","154.213.198.0:3128"]#"156.228.108.196:3128","156.228.99.115:3128","156.228.91.151:3128"]
    
    
    threads = []
    
    for i in range(10):
        ad = "https://www.profitableratecpm.com/f3ttrgmm?key=c48e66368d4932733432e517cf035cb2"
        api ="QXCup9rVWya171QRYtNHtTqzTxB6lipX"
        url = f"https://api.webscrapingapi.com/v1?api_key={api}&url={ad}=1&wait_until=networkidle0&device=mobile&wait_for={randint (6000,10000)}&country=au"

       # proxy = {"http":f"http://{pro}"}
        thread = threading.Thread(target=make_request, args=(url,))
        threads.append(thread)
        thread.start()  # Start the thread immediately

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All requests completed.")


for _ in range(3000):
        print(_)       
        main() 
