print("start")
import requests
import threading

def make_request(url):
    """Makes a GET request to the given URL and prints the response status code."""
    try:
        
        response = requests.get(url)
        print("proxy" in response.text, "proxy")
        print("maximum" in response.text, "error")
        
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
        if i >= 5:
           api= "psFElo5EvBfh03ibluoPX87MVQXne3GO"
        else: 
           api ="adr2BVGD9HCU0pGXmYi4sT65LCG0UWDh"
        url = f"https://api.webscrapingapi.com/v2?api_key={api}&url=https%3A%2F%2Fwww.profitablecpmrate.com%2Fwmbx23g2%3Fkey%3Db7a4029a74caece5dba8ed3619263305&render_js=1"
    
       # proxy = {"http":f"http://{pro}"}
        thread = threading.Thread(target=make_request, args=(url,))
        threads.append(thread)
        thread.start()  # Start the thread immediately

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All requests completed.")


for _ in range(4000):
        print(_)       
        main()
