import os		# 获取目录下的所有文件列表
import fnmatch	# 文件格式筛选模块，筛选指定格式文件


#遍历
from os import path


# def dirlist(path, allfile):
#     filelist = os.listdir(path)
#     for filename in filelist:
#         filepath = os.path.join(path, filename)
#         if os.path.isdir(filepath):
#             path.dirlist(filepath, allfile)
#         elif fnmatch.fnmatch(filepath,'*.wav'):#判断文件格式
#             allfile.append(filepath)
#             # allfile.append('\n')
#         print('*'*40,filepath,'\n')
#
#     return allfile

#格式转换
def RunScript(fileList) :
    print('hello world start:')


    # readf = open("E:\\py\\readfilename.txt", 'w+') #输出所有读入的文件
    # writef = open("E:\\py\\writefilename.txt", 'w+')   #输出所有创建并写入的文件

    code = "ffmpeg -i "
    codeMid = " -ac 1 -ar 8000 -y "
    print("filelist"+fileList)
    outputname= "D:/PCM/"+os.path.basename(fileList)

    finishcode = code + fileList + codeMid +outputname
    os.system(finishcode)
    # if len(fileList) > 0:
    #     # for index,filename in enumerate(fileList):
    #         if index <= len(fileList):
    #
    #             print("filelist:"+filename)
    #             # print('*'*40,'\n','Begin input = ',input,'\n')
    #             # print(os.path.basename(filename))
    #             # subname = 'D:/PCM/'+os.path.basename(filename)
    #
    #             # output = "D:/PCM/"+subname
    #             # print(subname)
    #
    #
    #
    #             # finishcode = code + input + codeMid +output
    #             # os.system(finishcode)
    #             # print('End output = ',outputfilename,'\n')
    #             # fileList.remove(filename)
    #
    #     else:
    #         #     去数据库查询新的信息
    #             print("去数据库查新信息咯!")
    #
    # else:
    #     print("现在没有要处理的文件,先等等!")




    print('hello world end')



# 主程序运行
# if __name__ =='__main__':
#     # fff = open("E:\\py\\allfile.txt", 'w+')
#     fileDir = r'D:\record_wav'
#     allfile = []
#     dirlist(fileDir,allfile)
#     for name in allfile:
#         # print(name,file=fff)
#         print(name)
#     RunScript(allfile)