import requests
import os
from datetime import *

 # downloading catalogue files in STATIC directory 
def cat_download ():
    today = date.today()
    today = today.strftime('%Y-%m-%d')
    y, m, d = today.split('-')
    #ga_static_dir = os.environ['GA_STATIC_DIR']
    file = ''.join(
        ['od-do-canada.', y, m, d, '.jl.gz'])
    url = 'http://open.canada.ca/static/od-do-canada.jl.gz'
    r = requests.get(url, stream=True)                
    with open (file, 'wb') as f:
        for chunk in r.iter_content(1024 * 64):
            f.write(chunk)
    f.close()
if __name__ == '__main__':
    cat_download()
    
  
