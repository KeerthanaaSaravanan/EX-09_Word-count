# EX-09: Word-count
## AIM:
To write a python program for getting the word count from a text.
## EQUIPEMENT'S REQUIRED: 
PC
Anaconda - Python 3.7
## ALGORITHM: 
### Step 1:
Create a file with .txt file extension.

### Step 2: 
Add some texts in that file.

### Step 3: 
Create a python file.
### Step 4:  
Write a code to count the number of words in that file.
### Step 5: 
Run the program.
### Step 6: 
Display the output.

## PROGRAM:
```
def program():
 count=0
 with open("text.txt","r") as f:
  for data in f:
     words=data.split()
     for word in words:
         count+=1
 print("Total number of words:",count)
program()
```
### OUTPUT:
![Screenshot 2023-12-23 124406](https://github.com/KeerthanaaSaravanan/EX-09_Word-count/assets/145742596/298f0ca8-116a-45e1-a165-7921e8cf7a46)
![Screenshot 2023-12-23 124353](https://github.com/KeerthanaaSaravanan/EX-09_Word-count/assets/145742596/ba891057-caf5-478f-89f5-54576adaca1b)
![Screenshot 2023-12-23 124344](https://github.com/KeerthanaaSaravanan/EX-09_Word-count/assets/145742596/3991654b-4019-4b03-8900-5dcd9b012316)

## RESULT:
Thus the program is written to find the word count from a text.
