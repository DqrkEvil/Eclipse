import src.obfuscation.encode as encode
import src.obfuscation.compress as cmp

import sys

def main():
    # Settings
    originalFile = "test/HelloWorld.py"
    
    # Read the contents of the file
    with open(originalFile, "rb") as originalFile:
        fileContents = originalFile.read()
    
    fileContents = fileContents.decode("utf-8")
    
    # Applying protection methods
    fileContents = encode.b64Encoding(fileContents)
        
        # Creating new file with protections applied
    with open("protectedFile.py", "w") as protectedFile:
        protectedFile.write(fileContents)
        protectedFile.truncate()
        
if __name__ == "__main__":
    main()
