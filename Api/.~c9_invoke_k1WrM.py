from binance.spot import Spot

client = Spot()
[429, 500, 502, 503, 504]
class BinanceApi:
    def __init__(self):
        self.session = requests.Session()
    
    def init_session(retry, backoff_factor, allowed_methods, status_forcelist):
        self.adapter = HTTPAdapter(max_retries=Retry(total=retry, backoff_factor=backoff_factor, allowed_methods=allowed_methods, status_forcelist=status_forcelist))
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
    
    def get
