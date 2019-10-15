import sys


from watchdog.observers import Observer
from watchdog.events import *
import time
from speech_recognition import RunSpeech
from wavToPcm import  RunScript



class FileEventHandler(FileSystemEventHandler):
    global fileDir
    global allfile
    global speechfile
    global datetime




    # def __init__(self):
    #     FileSystemEventHandler.__init__(self)

    # def on_moved(self, event):
    #     if event.is_directory:
    #         print("directory moved from {0} to {1}".format(event.src_path,event.dest_path))
    #     else:
    #         print("file moved from {0} to {1}".format(event.src_path,event.dest_path))

    def on_created(self, event):
        # log = Logger('all.log',level='debug')
        global filepath
        datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


        if event.is_directory:
            print(datetime+"directory created:{0}".format(event.src_path))
        else:
            print(datetime+"file created:{0}".format(event.src_path))
            createfile = ("file created:{0}".format(event.src_path))


            filepath = (fileDir+os.path.basename(createfile))
            # log.logger.debug("file created :"+ filepath)
            # fff = open("E:\\py\\allfile.txt", 'w+')
            # 调用文件转码的方法
            FileEventHandler.wav_pcm(filepath)

            FileEventHandler.speech_recognition(filepath)



    # def on_deleted(self, event):
    #     if event.is_directory:
    #         print("directory deleted:{0}".format(event.src_path))
    #     else:
    #         print("file deleted:{0}".format(event.src_path))
    #
    # def on_modified(self, event):
    #     if event.is_directory:
    #         print("directory modified:{0}".format(event.src_path))
    #     else:
    #         print("file modified:{0}".format(event.src_path))

    # 仿照ffmpeg实现命令行运行语音识别程序speaker-recognition.py程序
    def speech_recognition(self):
        RunSpeech(filepath)



    #   文件转码的方法,调用wavToPcm工具类
    def wav_pcm(self):
        RunScript(filepath)





if __name__ == "__main__":
    observer = Observer()
    fileDir = r'E:\FM_DEVICE_SERVER\public\record/'
    event_handler = FileEventHandler()
    observer.schedule(event_handler,fileDir,False)
    observer.start()
    # allfile = []
    # wavToPcm.dirlist(fileDir,allfile)
    # for name in allfile:
    #     # print(name,file=fff)
    #     print(name)
    # RunScript(allfile)
    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
    observer.join()


