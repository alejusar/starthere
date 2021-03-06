import zipfile
import shutil,os

def unzipAndMove(_in, _out , src):
    try:
        zin = zipfile.ZipFile(_in, 'r')
        zin.extractall(_out)
        if src:
            moveFiles(src, _out)
            shutil.rmtree(src)
    except Exception, e:
        print str(e)
        return False
    return True

def moveFiles(root_src_dir,root_dst_dir):
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir)
        if not os.path.exists(dst_dir): os.mkdir(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file): os.remove(dst_file)
            shutil.move(src_file, dst_dir)
            
def getUpdateFile(path,default = 0):
    if os.path.exists(path):
        try:
            f = open(path, 'r')
            return f.read()
        except: pass
    return default

def saveUpdateFile(path,value):
    try: open(path,'w+').write(value)
    except: pass