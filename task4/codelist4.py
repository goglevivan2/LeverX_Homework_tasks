import psycopg2
import json
import xml.etree.ElementTree as xml
import task4.secret
import task4.queries
import decimal

#Класс первоначальной обработки входных данных
class InitialProcessing:
    def jsonfile_to_dict(self,path: str) -> dict:
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
class CommonJSONEncoder(json.JSONEncoder):

    """
    Common JSON Encoder
    json.dumps(myString, cls=CommonJSONEncoder)
    """

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return {'type{decimal}': str(obj)}
class Dumping:

    def dumpToJSON(filename,dict)->bool:
        try:

            with open(filename, 'w') as fp:
                json.dump(dict, fp,cls=CommonJSONEncoder)
            return True
        except Exception as e:
            print(e)
            return False

class DatabaseInitialization:

    def sql_execution(self,sql:str,tableName:str) -> bool:
        try:
            con = psycopg2.connect(database="postgres",user="postgres",password=task4.secret.password,host="127.0.0.1",port="5432")
            cur = con.cursor()
            cur.execute(sql)
            print("Table"+tableName+" created successfully")
            con.commit()
            con.close()
            return True
        except Exception as e:
            print (e)
            return False
        finally:
            print('this is a work of '+tableName+' table')


class DatabaseFilling:
    def insert_value_to_rooms (roomdict:dict)->bool:
        try:
            con = psycopg2.connect(database="postgres", user="postgres", password=task4.secret.password,
                                   host="127.0.0.1", port="5432")
            cur = con.cursor()
            for item in roomdict:
                cur.execute("INSERT INTO ROOMS VALUES("+str(item['id'])+","+"'"+item['name']+"'"+")")
            con.commit()
            print("Value Inserting")

            con.commit()
            con.close()
            return True
        except Exception as e:
            print(e)
            return False

    def insert_value_to_students(stud) -> bool:
        con = psycopg2.connect(database="postgres", user="postgres", password=task4.secret.password, host="127.0.0.1",port="5432")
        cur = con.cursor()
        for item in stud:
           cur.execute("INSERT INTO STUDENTS VALUES('{birthday}','{id}','{name}','{room}','{sex}')".format(birthday=item["birthday"][0:10],id=item["id"],name=item["name"],room=item["room"],sex=item["sex"]))
        con.commit()
        print("Value Inserting")
        con.commit()
        return True
    def test(SQL):
        con = psycopg2.connect(database="postgres", user="postgres", password=task4.secret.password, host="127.0.0.1",
                               port="5432")
        cur = con.cursor()
        cur.execute(SQL)
        rows = cur.fetchall()
        print(rows)
        return rows

class endWork:
    def dropTable(tablename:str):
        try:
            con = psycopg2.connect(database="postgres", user="postgres", password=task4.secret.password,
                                   host="127.0.0.1", port="5432")
            cur = con.cursor()
            cur.execute('drop table {tabl}'.format(tabl=tablename))
            con.commit()
            con.close()
            return True
        except Exception as e:
            print(e)
            return False




class Main:
    def __init__(self):

        try:
            initialProcessingObject = InitialProcessing()
            databaseInitializationObject = DatabaseInitialization()
            rooms = initialProcessingObject.jsonfile_to_dict('D:\\LeverX_Python_course\\task4\\src\\rooms.json')
            students = initialProcessingObject.jsonfile_to_dict('D:\\LeverX_Python_course\\task4\\src\\students.json')
            databaseInitializationObject.sql_execution(task4.queries.CREATE_ROOMS,'ROOMS')
            databaseInitializationObject.sql_execution(task4.queries.CREATE_STUDENTS, 'STUDENTS')
            DBFillingObject = DatabaseFilling
            DBFillingObject.insert_value_to_rooms(rooms)
            DBFillingObject.insert_value_to_students(students)
            print(' список комнат и количество студентов в каждой из них')
            temp = DatabaseFilling.test(task4.queries.SQL1)
            Dumping.dumpToJSON('D:\\LeverX_Python_course\\task4\\answers\\SQL1.json',temp)
            print(' top 5 комнат, где самые маленький средний возраст студентов')
            temp = DatabaseFilling.test(task4.queries.SQL2)
            Dumping.dumpToJSON('D:\\LeverX_Python_course\\task4\\answers\\SQL2.json', temp)
            print('top 5 комнат с самой большой разницей в возрасте студентов')
            temp = DatabaseFilling.test(task4.queries.SQL3)
            Dumping.dumpToJSON('D:\\LeverX_Python_course\\task4\\answers\\SQL3.json', temp)
            print('список комнат где живут разнополые студенты')
            temp = DatabaseFilling.test(task4.queries.SQL4)
            Dumping.dumpToJSON('D:\\LeverX_Python_course\\task4\\answers\\SQL4.json', temp)
        finally:
            endWork.dropTable('rooms')
            endWork.dropTable('students')

Main()

