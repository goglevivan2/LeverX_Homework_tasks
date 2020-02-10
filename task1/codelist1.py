import json
import xml.etree.ElementTree as xml
import pandas as pd
PATH_rooms ="D:\\LeverX_Python_course\\task1\\src\\rooms.json" # путь к файлу rooms.json
PATH_students ="D:\\LeverX_Python_course\\task1\\src\\students.json" # путь к файлу students.json
XML = True # выводить ли итог в XML?
JSON = True # выводить ли итог в XML?
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
    def dict_to_json(name:str,dictionary:dict)->None:
        '''
        :param  name: name of file
        :param  dict: dictionary of values
        :return: None

        Данная функция загружает словарь в файл json
        '''
        with open(name, 'w') as fp:
            json.dump(dictionary, fp)
        return None

    def xml_result(filename:str)->None:
        '''
        :param filename: name of xml result file
        :return: None

         Данная функция загружает словарь в файл xml
        '''
        root = xml.Element('MyStudents')
        for item in itog_dict:
            appt = xml.Element("Room" + str(item)[6:])
            root.append(appt)
            for item2 in itog_dict[item]:
                student = xml.SubElement(appt, "student")
                student.text = str(item2) + " "
            tree = xml.ElementTree(root)
            with open(filename, "wb") as fh:
                tree.write(fh)



class datawork:
    def DataFrame(dct:dict)->pd.DataFrame:
        '''
        :param dct: dictionary of values
        :return: dataset

        Данная функция организует датасет из словаря
        '''
        df = pd.DataFrame(dct)
        return df

    def RemadeSets(self,students:dict,rooms:dict)->pd.DataFrame:
        '''

        :param students: dictionary (students.json)
        :param rooms: dictionary (rooms.json)
        :return: dataset

        Данная функция совершает преобразование students и rooms в удобный для работы датасет res
        '''
        infostud = obj2.DataFrame(students)
        infostud.rename(columns={'room': 'id_room'}, inplace=True)
        inforooms = obj2.DataFrame(rooms)
        inforooms.rename(columns={'id': 'id_room'}, inplace=True)
        res = infostud.merge(inforooms, on=['id_room'])
        res = res.drop('id', 1)
        res = res.drop('id_room', 1)
        res.rename(columns={'name_y': 'room', 'name_x': 'students'}, inplace=True)
        res.groupby('room')
        return res


obj = filework
rooms = obj.jsonfile_to_dict(PATH_rooms)
students = obj.jsonfile_to_dict(PATH_students)
obj2 =datawork
res = obj2.RemadeSets(obj2,students,rooms)
list_rooms = res.room.drop_duplicates().values.tolist()
# далее преобразование данных в нормальный словарь для работы с файлами
itog_dict ={}
for rms in list_rooms:
    itog_dict[rms] = res[res.room == rms]['students'].drop_duplicates().values.tolist()

if JSON :
    obj.dict_to_json('result.json',itog_dict)
if XML:
    obj.xml_result('result.xml')


