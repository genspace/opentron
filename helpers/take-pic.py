def take_pic():
    
    robot.set_lights(rails = 1)
    
    file_name = "/var/lib/jupyter/notebooks/data/file_" + str(dt.now().isoformat()) + ".jpg"
    sys_call = "ffmpeg -y -f video4linux2 -s 640x480 -i /dev/video0 -ss 0:0:1 -frames 1 " + file_name
    
    os.system(sys_call)
    
    robot.set_lights(rails = 0)



