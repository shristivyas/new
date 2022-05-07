import json
 

def write_json(new_data, filename='employer.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["employ"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)


def read_all(filename = 'employer.json'):
    f=open('employer.json')
    data = json.load(f)
    for i in data['employ']:
        print(i)
    f.close()
 
def delete_employ(ids ,filename = 'employer.json'):
    f = open('employer.json')
    data = json.load(f)
    for i in range(len(data)):
        if data[i]["id"] == ids:
            del data[i]
            break

def read_employ(ids , filename = 'employer.json'):
    f=open('employer.json')
    data = json.load(f)
    for i in range(len(data)):
        if data[i]["id"] == ids:
            print (i)
    f.close()

start = int(input(' 1. To add employe. \n 2. To view all employes. \n 3. To delete a emloye. \n 4. To view a specific employe. \n Choose a number to continue...... \n'))
if start==1:
    w = str(input("Enter id-number. = "))
    x = str(input("Enter name of employe. ="))
    z = str(input("Enter designation of employe. ="))
    y={"id":w,"name": x,"designation": z}
    write_json(y)

elif( start == 2):
    read_all()

elif(start == 3):
    ab =str(input('Enter id-number to delete. ='))
    delete_employ(ab)

elif (start == 4):
    xy = str(input('Enter id-number of employe. ='))
    read_employ()

else:
    print('Choose valid option!!!!!!!!!!')