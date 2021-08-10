# import requests

# url = 'http://google.com/favicon.ico'
# filename = url.split('/')[-1]
# r = requests.get(url, allow_redirects=True)
# open(filename, 'wb').write(r.content)
# print(r.content)

# import urllib.request

# src = 'https://ky.ntt.edu.vn/images/BaiViet/Nam2019/Thang12/co-hoi-lam-viec-tai-nhat-ban-cho-sinh-vien-khoa-dieu-duong-dh-nguyen-tat-thanh-01.jpg'

# urllib.request.urlretrieve(src, "captcha.png")

# ## Importing Necessary Modules
# import requests # to get image from the web
# import shutil # to save it locally

# ## Set up the image URL and filename
# image_url = "http://benhvienchinhhinh.net/upload/files/11.jpg"
# filename = image_url.split("/")[-1]

# # Open the url image, set stream to True, this will return the stream content.
# r = requests.get(image_url, stream = True)

# # Check if the image was retrieved successfully
# if r.status_code == 200:
#     # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
#     r.raw.decode_content = True
    
#     # Open a local file with wb ( write binary ) permission.
#     with open(filename,'wb') as f:
#         shutil.copyfileobj(r.raw, f)
        
#     print('Image sucessfully Downloaded: ',filename)
# else:
#     print('Image Couldn\'t be retreived')


# # First import wget python module.
# import wget

# # Set up the image URL
# image_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"

# # Use wget download method to download specified image url.
# image_filename = wget.download(image_url)

# print('Image Successfully Downloaded: ', image_filename)


# # importing required modules
# import urllib.request

# # setting filename and image URL
# filename = 'sunshine_dog.jpg'
# image_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"

# # calling urlretrieve function to get resource
# urllib.request.urlretrieve(image_url, filename)




# # Importing required libraries
# import urllib.request

# # Adding information about user agent
# opener=urllib.request.build_opener()
# opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
# urllib.request.install_opener(opener)

# # setting filename and image URL
# filename = 'sunshine_dog.jpg'
# image_url = "https://cdn.pixabay.com/photo/2020/02/06/09/39/summer-4823612_960_720.jpg"

# # calling urlretrieve function to get resource
# urllib.request.urlretrieve(image_url, filename)


# import requests
# import bs4 as bs
# import urllib.request
# import wget

# ##################################################
# # getting url images #
# ##################################################

# url = "http://benhvienchinhhinh.net/upload/files/11.jpg"

# opener = urllib.request.build_opener()
# opener.add_headers = [{'User-Agent' : 'Mozilla'}]
# urllib.request.install_opener(opener)

# raw = requests.get(url).text
# soup = bs.BeautifulSoup(raw, 'html.parser')

# imgs = soup.find_all('img')

# links = []

# for img in imgs:
#     link = img.get('src')
#     links.append(link)
#     print(links)

# ################################################
# # downloading images #
# ################################################

# for url in links:

#     # Invoke wget download method to download specified url image.
#     local_image_filename = wget.download(url)

#     # Print out local image file name.
#     local_image_filename

#     continue

# ---

# import wget
# # base_url = 'https://homepages.cae.wisc.edu/~ece533/images/'
# # image_names = ['airplane.png', 'arctichare.png', 'baboon.png']
# # prefix = 'Beautiful_Plan_'
# # for image_name in image_names:
# #   wget.download(base_url + image_name, out = prefix + image_name)

# base_url = 'http://benhvienchinhhinh.net/upload/files/11.jpg'
# # wget.download(base_url)

# import urllib as urllib

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# req = urllib.request.Request(url=base_url, headers=headers)
# urllib.request.urlopen(req).read()

# print('Done')


from urllib.request import urlopen, Request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
reg_url = "http://benhvienchinhhinh.net/upload/files/11.jpg"
req = Request(url=reg_url, headers=headers) 
html = urlopen(req).read() 
with open('img.jpg', 'wb+') as f:
    f.write(html)
print(html) 