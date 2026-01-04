with open("mybin","wb") as f: #in this we don't have to manually close the file, it would automatically close  
    f.write("abcdefghij".encode()) #or f.write(b"abcdefghij")