import glob

def generate_train_and_val(image_path, txt_file):
    with open(txt_file, 'w') as tf:

        for jpg_file in glob.glob(image_path + '*.jpg'):
            res = jpg_file[:14]+'/'+jpg_file[15:]

            tf.write(res + '\n')
    print("finish!")


def main(path, dstpath):
    generate_train_and_val(path, dstpath)
    

if __name__ == '__main__':
    #srcpath = 'data/val_bdd/'
    #dstpath = 'data/val.txt'
    srcpath = 'data/train_bdd/'
    dstpath = 'data/train.txt'
    main(srcpath, dstpath)
