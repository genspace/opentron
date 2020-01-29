def export_pic():
    
    time_interval = 10800*2/3 #takes picture every 2 hours (value in seconds)
    threading.Timer(time_interval, export_pic).start()
    
    experiment = "e3"
    
    image_paths = glob("/var/lib/jupyter/notebooks/data/*.jpg".format(experiment))
    url = 'https://website.com/img'
    
    for img_path in image_paths:
        files = {'media': open(img_path, 'rb')}
        requests.post(url, files = files)  
