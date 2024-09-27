"""
修改了所有路径concat的方式。
从原来的只支持Linux改成了更加健壮的两个系统都支持的方式。
"""

import os
from shutil import copyfile
import pdb
import io

# 776的基础路径
veri776_path = "E:\\dataset\\VeRi776"

path = './keypoint_test.txt'
if not os.path.isdir(veri776_path):
    print('please change the veri776_path')

save_path = os.path.join(veri776_path, 'veri', 'view')
if not os.path.isdir(save_path):
    os.makedirs(save_path)

#---------------------------------------
#train_all

f2 = io.open(path, 'r', encoding= 'UTF-8')
train_path = os.path.join(veri776_path, 'image_test')
train_save_path = os.path.join(save_path, 'test')

if not os.path.isdir(train_save_path):
    os.makedirs(train_save_path)
for i in f2:
    filename = i.split('/')[-1].split(' ')[0]   #0190_c014_00051260_1.jpg
    label = i.split('/')[-1][0:4]  #0190
    view = i[-2]  #6
    #../veri/image_train/0190_c014_00051260_1.jpg
    src_path = os.path.join(train_path, filename)  
    if not os.path.exists(src_path):
        continue
    #../veri/view/test/0190
    dst_path = os.path.join(train_save_path, label)
    new_filename = filename.split('.')[0] + '_' + view + '.jpg'  #0190_c014_00051260_1_6.jpg
    if not os.path.isdir(dst_path):
        os.makedirs(dst_path)
    copyfile(src_path, os.path.join(dst_path, new_filename))
f2.close()

pdb.set_trace()

for root, dirs, files in os.walk(train_path, topdown=True):
    for name in files:
        if not name[-3:]=='jpg':
            continue
        ID  = name.split('_')
        src_path = os.path.join(train_path, name)
        dst_path = os.path.join(train_save_path, ID[0])
        if not os.path.isdir(dst_path):
            os.makedirs(dst_path)
        copyfile(src_path, os.path.join(dst_path, name))

#-----------------------------------------
#query

query_path = os.path.join(veri776_path, 'image_query')
query_save_path = os.path.join(veri776_path, 'pytorch' + 'query')

if not os.path.isdir(query_save_path):
    os.makedirs(query_save_path)

for root, dirs, files in os.walk(query_path, topdown=True):
    for name in files:
        if not name[-3:]=='jpg':
            continue
        ID  = name.split('_')
        src_path = os.path.join(query_path ,name)
        dst_path = os.path.join(query_save_path ,ID[0])
        if not os.path.isdir(dst_path):
            os.makedirs(dst_path)
        copyfile(src_path, os.path.join(dst_path ,name))


#-----------------------------------------
#multi-query
# for dukemtmc-reid, we do not need multi-query

query_path = os.path.join(veri776_path, 'multi_query')
query_save_path = os.path.join(veri776_path, 'pytorch', 'multi-query')

if os.path.isdir(query_path):
    if not os.path.isdir(query_save_path):
        os.makedirs(query_save_path)
    for root, dirs, files in os.walk(query_path, topdown=True):
        for name in files:
            if not name[-3:]=='jpg':
                continue
            ID  = name.split('_')
            src_path = os.path.join(query_path, name)
            dst_path = os.path.join(query_save_path, ID[0])
            if not os.path.isdir(dst_path):
                os.makedirs(dst_path)
            copyfile(src_path, os.path.join(dst_path, name))

#-----------------------------------------
#gallery

gallery_path = os.path.join(veri776_path, 'image_test')
gallery_save_path = os.path.join(veri776_path, 'pytorch' + 'gallery')

if not os.path.isdir(gallery_save_path):
    os.makedirs(gallery_save_path)

for root, dirs, files in os.walk(gallery_path, topdown=True):
    for name in files:
        if not name[-3:]=='jpg':
            continue
        ID  = name.split('_')
        src_path = os.path.join(gallery_path, name)
        dst_path = os.path.join(gallery_save_path, ID[0])
        if not os.path.isdir(dst_path):
            os.makedirs(dst_path)
        copyfile(src_path, os.path.join(dst_path, name))


#---------------------------------------
#train_val

train_path = os.path.join(veri776_path, 'image_train')
train_save_path = os.path.join(veri776_path, 'pytorch' + 'train')
val_save_path = os.path.join(veri776_path, 'pytorch' + 'val')

if not os.path.isdir(train_save_path):
    os.makedirs(train_save_path)
    os.makedirs(val_save_path)

for root, dirs, files in os.walk(train_path, topdown=True):
    for name in files:
        if not name[-3:]=='jpg':
            continue
        ID  = name.split('_')
        src_path = os.path.join(train_path, name)
        dst_path = os.path.join(train_save_path, ID[0])
        if not os.path.isdir(dst_path):
            os.makedirs(dst_path)
            # first image is used as val image
            dst_path = os.path.join(val_save_path, ID[0])
            os.makedirs(dst_path)
        copyfile(src_path, os.path.join(dst_path, name))
