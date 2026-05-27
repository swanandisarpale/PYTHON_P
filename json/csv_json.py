


def main():
    file=open("Salary_preediction2.csv","r") #opening csv in read mode
    file_data=file.read()
    
    file_items=file_data.split("\n") #spliting rows
    
    headers=file_items[0] #spliting headers in colum names
    headers=headers.split(",")
    
    data=[] #empty list to store all rows of data
    for d in range(1,len(file_items)):           #rows loop
        data.append(file_items[d].split(","))
  
    json=[]   #empty list to store final json objects
    temp={}   # temp dict to store one row at a time

    for d in range(0,len(data)):
        for h in range(0,len(headers)):   #loop through each column
            temp[headers[h]]=data[d][h]   #maping header value
            
        json.append(temp) # adding the complete dict to json
        temp={}   #temp for next row 

    for i in json:
      print(i)    #prints each json objects
    
    file=open("xyz.json","a")
    file.write("[")  #starts json array
    for i in json:
        file.write(str(i).replace("'",'"')+",\n")  #converting dict into string
    
    file.close()
        
    file=open("xyz.json","r")
    data=file.read()
    data=data[0:-2]+"]"

    file=open("xyz.json","w")
    file.write(data)
    file.close()
    
if __name__ == '__main__':
    main()