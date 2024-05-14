import os
import random
import sys
from pathlib import Path

import src.obfuscation.checksum as check
import src.obfuscation.compress as cmp
import src.obfuscation.encode as encode


def debugDump(fileContents: str) -> None:
    if not debugFlag:
        return
    
    # Create folder for debug files
    folderPath = r"debug" 
    debugNum = 0

    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    
    else:
        # Get the number of files in the folder
        debugNum = len(os.listdir(folderPath))
        
    # Creating temp files for debug purposes 
    with open(f"debug/debugFile{debugNum}.py", "w") as protectedFile:
        protectedFile.write(fileContents)
        protectedFile.truncate()

def applyMethods(protectionMethods: list, fileContents: str) -> str:
    random.shuffle(protectionMethods)
    
    for method in protectionMethods:
        fileContents = method(fileContents)

        debugDump(fileContents)
    
    return fileContents

def main():
    # Argument receiver from terminal  
    filePath = sys.argv[1]
    fileName = Path(filePath).stem
    
    global debugFlag
    debugFlag = "-d" in sys.argv
    
    # Read the contents of the file
    with open(filePath, "rb") as file:
        fileContents = file.read()
    
    # Convert from bytes to string 
    fileContents = fileContents.decode("utf-8")   
    
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
    
    print("Success! Obfuscated file can be found in the 'output' folder.")
            
if __name__ == "__main__":
    main()
