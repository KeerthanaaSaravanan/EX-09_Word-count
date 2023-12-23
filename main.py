def program():
  count=0
  with open("text.txt","r") as f:
    for data in f:
      words=data.split()
      for word in words:
         count+=1
  print("Total number of words:",count)
program()