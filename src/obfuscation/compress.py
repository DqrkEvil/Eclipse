"""
+----------------------------------------------------+
|              Module Name: compress.py              |
|                  Author: DqrkEvil                  |
|             Date Created: 02/05/2024               |
|              Date Edited: 02/05/2024               |
|      Description: Base64 encodes python code       |
+----------------------------------------------------+
"""

import zlib
import lzma

def lzmaCompress(content: str) -> str:
    content = content.encode("utf-8")
    compressed = lzma.compress(content)
    
    protectedContent = "import lzma;" + f'exec(lzma.decompress({compressed}).decode("utf-8"))'
    
    return protectedContent

def zlibCompress(content: str) -> str:
    content = content.encode("utf-8")
    compressed = zlib.compress(content)
    
    protectedContent = "import zlib;" + f'exec(zlib.decompress({compressed}).decode("utf-8"))'
    
    return protectedContent
