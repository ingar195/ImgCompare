import hashlib
import os
import shutil


def md5(file):
    md5_hash = hashlib.md5()
    a_file = open(file, "rb")
    content = a_file.read()
    md5_hash.update(content)

    digest = md5_hash.hexdigest()
    print(digest)
    return (digest)


def getFileCount(folder):
    count = 0
    for f in os.listdir(folder):
        if not os.path.isdir(folder + "/" + f):
            count += 1
    return count


def compare(folder):
    duplicatePath = f"{folder}/duplicatePath/"
    hashArray = []
    progress = 0
    totalFiles = getFileCount(folder)
    for file in os.listdir(folder):
        print(f"{progress}/{totalFiles}")
        currentFile = f"{folder}/{file}"
        if not os.path.isdir(currentFile):
            print(currentFile)
            if len(hashArray) == 0:
                print("First file skipping")
                hashArray.append(md5(currentFile))
            else:
                hashFile = md5(currentFile)
                if hashFile in hashArray:
                    print("File aleray exists, moving")
                    if not os.path.exists(duplicatePath):
                        os.mkdir(duplicatePath)
                    shutil.move(currentFile, duplicatePath)
                else:
                    print(f"Added {currentFile}")
                    hashArray.append(md5(currentFile))
        else:
            print(f"{currentFile} is a folder so skipped")
        progress += 1

path = "Pic"
compare(path)
