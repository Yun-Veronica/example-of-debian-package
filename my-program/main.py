#!/usr/bin/env python3

import sys

def main():
    
    print(f"Number of arguments: {len(sys.argv)}")
    print("Arguments passed:")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")
        
    print(f"Hello, {sys.argv}")

if __name__ == "__main__":
    main()
