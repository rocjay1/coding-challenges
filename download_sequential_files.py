import re, os.path
from urllib.request import urlretrieve, urlopen

def download_files(url, output_file): 
    url_components = os.path.split(url)
    page = urlopen(url_components[0])
    html = page.read().decode("utf-8")
    pattern = "<a.*?>.*\.jpg.*</a.*?>"
    match_results = re.findall(pattern, html, re.IGNORECASE)
    for image in match_results:
        tag_free = re.sub("<.*?>", "", image.replace(" ", "")) # remove tags
        image_url = url_components[0] + "/" + tag_free
        urlretrieve(image_url, output_file + "/" + tag_free) # download image to output file
        print("Successfully downloaded\n" + image_url + "\n\r")

url = "http://699340.youcanlearnit.net/image001.jpg"
download_files(url, "./image_downloads")

# This code only downloads the images--couldn't make the sequential download as in the 
# video