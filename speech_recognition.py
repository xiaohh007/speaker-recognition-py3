#遍历
import fnmatch
import os
from time import sleep


def fileslist(path, allfile):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            path.dirlist(filepath, allfile)
        elif fnmatch.fnmatch(filepath,'*.wav'):#判断文件格式
            allfile.append(filepath)
            # allfile.append('\n')
        print('*'*40,filepath,'\n')

    return allfile

#音频文件解析
def RunSpeech(fileList) :
    print('hello world start:')


    # readf = open("E:\\py\\readfilename.txt", 'w+') #输出所有读入的文件
    # writef = open("E:\\py\\writefilename.txt", 'w+')   #输出所有创建并写入的文件


    code = "speaker-recognition.py -t predict -i "
    codeMid = " -m model.out "
    inputname= "D:/PCM/"+os.path.basename(fileList)
    finishcode = code + inputname + codeMid
    os.system(finishcode)
    # for filename in fileList:
    #
    #     input = filename
    #     print("filename"+filename)
    #
    #     finishcode = code + input + codeMid
    #
    #     os.system(finishcode)
    #
    #         # print('End output = ',outputfilename,'\n')
    #         # print(input,file=readf)
    #         # print(input)
    #         # print(outputfilename,file=writef)
    #         # print(outputfilename)


    print('hello world end')



# 主程序运行
if __name__ =='__main__':
    # fff = open("E:\\py\\allfile.txt", 'w+')
    fileDir = r'D:/PCM'
    allfile = []
    fileslist(fileDir,allfile)
    # for name in allfile:
    #     # print(name,file=fff)
    #     print(name)
    RunSpeech(allfile)