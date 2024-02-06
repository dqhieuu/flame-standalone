import os
import numpy as np

def merger(folder, full = False):
    # read all npy files from frame subfolder in folder, full means all 5 param, else only 3
    folder_list = os.listdir(folder)
    folder_list.sort()
    file_name = ['exp.npy', 'pose.npy', 'shape.npy']
    if full:
        file_name += ['tex.npy', 'detail.npy']
    
    data = []
    for frame in folder_list:
        frame_path = os.path.join(folder, frame)
        
        for f in file_name:
            file_path = os.path.join(frame_path, f)
            if os.path.exists(file_path):
                data.append(np.load(file_path))
            else:
                print('File not found:', file_path)

    out = np.concatenate(data)
    print(out.shape)
    np.save('merged_params.npy', out)
        
    test = folder_list[0]
    test_file0 = os.path.join(folder, test, file_name[0])
    test_file1 = os.path.join(folder, test, file_name[1])
    test_file2 = os.path.join(folder, test, file_name[2])
    print(np.load(test_file0).shape)
    print(np.load(test_file1).shape)
    print(np.load(test_file2).shape)
    if full:
        test_file3 = os.path.join(folder, test, file_name[3])
        test_file4 = os.path.join(folder, test, file_name[4])
        print(np.load(test_file3).shape)
        print(np.load(test_file4).shape)
    # => 156 params each

path = '/home/huy/emoca/output/videoCheo/2/code/EMOCA_v2_lr_mse_20'
merger(path)