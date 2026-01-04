with open("mybin","rb") as f:
    print(f.read(2).decode())  
    f.seek(4,0) # Move the cursor to the 4th byte  from 0th position #0-->beginning, 1-->current position, 2-->end of file
    print(f.read(1).decode())
    f.seek(-4,2)
    print(f.read(2).decode()) 