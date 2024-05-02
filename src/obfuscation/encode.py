"""
+----------------------------------------------------+
|               Module Name: encode.py               |
|                  Author: DqrkEvil                  |
|             Date Created: 18/04/2024               |
|              Date Edited: 02/05/2024               |
|      Description: Base64 encodes python code       |
+----------------------------------------------------+
"""

import base64 as b64

def b64Encoding(content: str) -> str:
    
    # Encode the original file
    content = content.encode("utf-8")
    encodedContent = b64.b64encode(content)
    encodedContent = encodedContent.decode("utf-8")
    
    # Inject code to decode the protected file on runtime making the file executable
    protectedContent = "import base64;" + f'exec(base64.b64decode("{encodedContent}").decode("utf-8"))'
    
    return protectedContent
