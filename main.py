import src.obfuscation.encode as encode
import src.obfuscation.compress as cmp

import sys
import random

def main():
    # Settings
    originalFile = sys.argv[1]
    
    # Read the contents of the file
    with open(originalFile, "rb") as originalFile:
        fileContents = originalFile.read()
    
    fileContents = fileContents.decode("utf-8")
    
    # Randomising and applying protection methods
    protectionMethods = [
        encode.b64Encoding,
        cmp.lzmaCompress,
        cmp.zlibCompress
    ] 
    
    random.shuffle(protectionMethods)
    
    for n, method in enumerate(protectionMethods):
        fileContents = method(fileContents)
        
            # Creating new file with protections applied
        with open(f"tempFiles/tempFile{n}.py", "w") as protectedFile:
            protectedFile.write(fileContents)
            protectedFile.truncate()
        
        # Creating new file with protections applied
    with open("protectedFile.py", "w") as protectedFile:
        protectedFile.write(fileContents)
        protectedFile.truncate()        
            
if __name__ == "__main__":
    main()
