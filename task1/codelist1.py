import json
import xml.etree.ElementTree as xml
import pandas as pd
class filework:
    def jsonfile_to_dict(path:str)->dict:
        """

        :param path: json file path
        :return: dictionary of value

        Данная функция парсит json-файл и перегоняет значения в словарь.
        """
        try:
            with open(path) as file:
                value = json.load(file)
        except Exception as e:
            print(e)
            print("Ошибка чтения файла")
            exit()

        return value

class datawork:
    def DataFrame(dct:dict):
        df = pd.DataFrame(dct)
        return df




obj = filework
rooms = obj.jsonfile_to_dict("D:\\LeverX_Python_course\\task1\\src\\rooms.json")
students = obj.jsonfile_to_dict("D:\\LeverX_Python_course\\task1\\src\\students.json")

obj2 =datawork
# Надо ещё посмотреть JSON to Dataset
infostud = obj2.DataFrame(students)
infostud.rename(columns={'room':'id_room'}, inplace=True)
inforooms = obj2.DataFrame(rooms)
inforooms.rename(columns={'id':'id_room'}, inplace=True)
res = infostud.merge(inforooms,on=['id_room'])
res=res.drop('id',1)
res=res.drop('id_room',1)
res.rename(columns={'name_y':'room','name_x':'students'}, inplace=True)
res.groupby('room')
#res = infostud['room'].merge(inforooms['id'])
#print(res.room.drop_duplicates().values.tolist())
#print(res[res.room == "Room #748"]['students'].drop_duplicates().values.tolist())


list_rooms = res.room.drop_duplicates().values.tolist()
itog_dict ={}

for rms in list_rooms:
    itog_dict[rms] = res[res.room == rms]['students'].drop_duplicates().values.tolist()

#print (itog_dict)


with open('result.json', 'w') as fp:
    json.dump(itog_dict, fp)



def xml_result(filename):
    root = xml.Element('MyStudents')
    for item in itog_dict:
        appt = xml.Element("Room"+str(item)[6:])
        root.append(appt)
        for item2 in itog_dict[item]:
            student = xml.SubElement(appt, "student")
            student.text = str(item2)+" "
        tree = xml.ElementTree(root)
        with open(filename, "wb") as fh:
            tree.write(fh)


xml_result('result.xml')