import os
import random
import sys
from pathlib import Path

import src.obfuscation.compress as cmp
import src.obfuscation.encode as encode


def applyMethods(protectionMethods: list, fileContents: str) -> str:
    random.shuffle(protectionMethods)
    
    for n, method in enumerate(protectionMethods):
        fileContents = method(fileContents)
        
        # Create folder for debug files
        folderPath = r"debug" 
        if not os.path.exists(folderPath):
            os.makedirs(folderPath)
            
        # Creating temp files for debug purposes 
        with open(f"debug/debugFile{n}.py", "w") as protectedFile:
            protectedFile.write(fileContents)
            protectedFile.truncate()
    
    return fileContents

def main():
    # Argument receiver from terminal  
    filePath = sys.argv[1]
    fileName = Path(filePath).stem
    
    # Read the contents of the file
    with open(filePath, "rb") as file:
        fileContents = file.read()
    
    # Convert from bytes to string 
    fileContents = fileContents.decode("utf-8")
    
    # Encode contents into single line
    fileContents = encode.b64Encoding(fileContents)     
    
    # Randomising and applying protection methods
    protectionMethods = [
        encode.b64Encoding,
        cmp.lzmaCompress,
        cmp.zlibCompress
    ] 

    fileContents = applyMethods(protectionMethods, fileContents)
        
    # Create folder for output files
    folderPath = r"output" 
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)    
        
    # Creating new file with protections applied
    with open(f"output/{fileName}_Obfuscated.py", "w") as protectedFile:
        protectedFile.write(fileContents)
        protectedFile.truncate()        
            
if __name__ == "__main__":
    main()
