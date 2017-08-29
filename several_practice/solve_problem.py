# #implementation
# import time
# import os
# source = ['"D:\\practice"', 'D:\\']
# target_dir='D:\\practicec'
# target=target_dir+os.sep+\
#     time.strftime('%Y%m%d%H%M%S')+'.zip'
# if not os.path.exists(target_dir):
#     os.mkdir(target_dir)
# zip_command='zip-{0}{1}'.format(target,
#                                 ' '.join(source))
# print('zip command is ')
# print(zip_command)
# print('running')
# if  os.system(zip_command)==0:
#     print('success')
# else:
#     print('failed')import os
import time
import os
# 1. The files and directories to be backed up are specified in a list.
source = [r'D:\\practice.txt',r'D:\\practice1'] #要备份的文件的位置,r是防转义？

# 2. The backup must be stored in a main backup directory
target_dir=r'D:\\' #Remember to change this to what you will be using备份在哪里,目标目录

# 3. The files are backed up into a rar file.
# 4. The name of the rar archive is the current date and time
comment=input('Enter your comment')
if  comment==0:
    target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'  # 备份文件名称targer_dir，加号+是把两个字符串拼起来了
else:
    target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '_'+comment.replace(' ','_')+'.zip'  # 备份文件名称targer_dir，加号+是把两个字符串拼起来了,.string.replace是一个函数，把文字里的空格用_代替

# 5. We use the rar command in windows to put the files in a zip archive,you must to be sure  you have installed WinRARA and that in your path
rar_command = '"C:\\Program Files\\WinRAR\\WinRAR.exe" a %s %s'%(target,' '.join(source))#-a是rar命令

# Run the backup
if os.system(rar_command) == 0: #运行这一条指令，如果运行成功，返回0
    print ('Successful backup to', target)
else:
    print ('Backup FAILED')