import json

class employer:

    @classmethod
    def write_json(new_data, filename='employer.json'):
        with open(filename,'r+') as file:
            file_data = json.load(file)
            file_data["employ"].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)

    @classmethod
    def read_all(filename = 'employer.json'):
        f=open('employer.json')
        data = json.load(f)
        for i in data['employ']:
            print(i)
        f.close()

    @classmethod
    def delete_employ(ids ,filename = 'employer.json'):
        f = open('employer.json')
        data = json.load(f)
        for i in range(1,len(data)):
            if data[i]["id"] == ids:
                del data[i]
                print('Employe details has been deleted.')
            f.close()

    @classmethod
    def read_employ(id1 , filename = 'employer.json'):
        f=open('employer.json')
        data = json.load(f)
        for i in range(1,len(data)):
            if id1 in data[i]:
                return data[i]
            f.close()



start = int(input(' 1. To add employe. \n 2. To view all employes. \n 3. To delete a emloye. \n 4. To view a specific employe. \n Choose a number to continue...... \n'))
if start==1:
    w = str(input("Enter id-number. = "))
    x = str(input("Enter name of employe. ="))
    z = str(input("Enter designation of employe. ="))
    y={"id":w,"name": x,"designation": z}
    employer.write_json(y)

elif( start == 2):
    employer.read_all()

elif(start == 3):
    ab =str(input('Enter id-number to delete. ='))
    employer.delete_employ(ab)

elif (start == 4):
    xy = str(input('Enter id-number of employe. ='))
    employer.read_employ()

else:
    print('Choose valid option!!!!!!!!!!')