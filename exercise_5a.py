from queue import Queue
from urllib.request import urlopen, Request
import os
import threading
from multiprocessing import Pool
import sys
import time


HEADER = {'User-Agent': 'Mozilla/5.0'}

# Note: only URL:s ending on .jpg works
IMG_URLS = ["http://cdn.akc.org/content/article-body-image/lab_puppy_dog_pictures.jpg",
            "https://i.natgeofe.com/n/4f5aaece-3300-41a4-b2a8-ed2708a0a27c/domestic-dog_thumb_4x3.jpg",
            "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg",
            "https://media.npr.org/assets/img/2021/08/06/dog-4415649_wide-3ef4f36fb94397991ee6721a5c6929451178d914.jpg",
            #"https://www.dogstrust.org.uk/help-advice/_images/164742v800_puppy-1.jpg",
            "https://cdn.pixabay.com/photo/2016/02/11/17/00/dog-1194087_960_720.jpg",
            "https://cdn.pixabay.com/photo/2016/02/19/15/46/labrador-retriever-1210559_960_720.jpg",
            "https://cdn.pixabay.com/photo/2017/02/16/11/13/dog-2071182_960_720.jpg",
            "https://cdn.pixabay.com/photo/2017/08/28/23/08/dog-2691631__340.jpg",
            "https://cdn.pixabay.com/photo/2020/01/15/19/54/leonberger-4768787__340.jpg",
            #"https://cdn.pixabay.com/photo/2016/01/19/16/50/snowflakes-1149417__340.jpg",
            "https://cdn.pixabay.com/photo/2016/02/25/10/31/puppy-1221791__340.jpg",
            "https://cdn.pixabay.com/photo/2015/02/12/10/30/dog-633562__340.jpg",
            "https://cdn.pixabay.com/photo/2019/06/15/18/27/labrador-4276236__340.jpg",
            "https://cdn.pixabay.com/photo/2016/05/06/14/16/dog-1375938__340.jpg",
            "https://cdn.pixabay.com/photo/2017/03/08/13/06/dog-2126708__340.jpg",
            "https://cdn.pixabay.com/photo/2016/06/05/22/45/otter-1438381__340.jpg",
            "https://cdn.pixabay.com/photo/2014/10/22/14/43/otter-498046__340.jpg",
            "https://cdn.pixabay.com/photo/2017/10/23/23/43/otter-2883047__340.jpg"
            ]

# Change to desired folder
SAVE_FOLDER = "/Users/olivers/Documents/Programmering/vscode/python/python_2a_course/save_folder"  # TODO

def timer(func):
    def timer_wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Execution time: {(end - start):.7f} seconds ({func.__name__})")
        return result
    return timer_wrapper


def request_and_open(URL):
    request = Request(URL, headers=HEADER)
    url_info_byte = urlopen(request, timeout=20).read()
    return url_info_byte


def generate_queue():
    queue = Queue()
    for url in IMG_URLS:
        queue.put(url)
    
    return queue


def worker(queue):
    while queue.empty() != True:
        url = queue.get()
        download_img(url)
        queue.task_done()


def create_and_run_threads(queue):
    num_threads = 2
    for _ in range(num_threads):
        threading.Thread(target=worker, args=(queue,)).start()


def urls_as_list():
    url_list = []
    for url in IMG_URLS:
        url_list.append(url)
    return url_list

def create_and_run_pool(iterable):
    with Pool(8) as p:
        p.map(download_img, iterable)


def download_img(url):
    img_bytes = request_and_open(url)
    img_name = url.split("/")[-1]
    file_path = os.path.join(SAVE_FOLDER, img_name)

    with open(file_path, "wb") as img:
        img.write(img_bytes)
        print(f"Downloading image: {img_name}")




def main():
    #for url in IMG_URLS:
    #    download_img(url)
    queue = generate_queue()
    create_and_run_threads(queue)
    queue.join()
    #url_list = urls_as_list()
    #create_and_run_pool(url_list)

if __name__ == "__main__":
    main()
