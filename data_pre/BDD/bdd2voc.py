import os
import generate_xml
import json_extract

def main(srcDir, dstDir):
    i = 1
    for dirpath, dirnames, filenames in os.walk(srcDir):
        for filepath in filenames:
            fileName = os.path.join(dirpath,filepath)
            print(fileName)
            print("processing: {}, {}".format(i, fileName))
            i = i + 1
            xmlFileName = filepath[:-5]
            objs = json_extract.extract(str(fileName))
            if len(objs):
                tmp = generate_xml.PascalVocWriter(dstDir, xmlFileName, (720,1280,3), fileName)
                for obj in objs:
                    tmp.addBndBox(obj[0],obj[1],obj[2],obj[3],obj[4])
                tmp.save()
            else:
                print(fileName)

if __name__ == '__main__':
    #srcDir = 'bdd100k/labels/100k/val'
    #dstDir = 'bdd100k/Annotations/val'
    srcDir = 'bdd100k/labels/100k/train'
    dstDir = 'bdd100k/Annotations/train'
    main(srcDir, dstDir)
