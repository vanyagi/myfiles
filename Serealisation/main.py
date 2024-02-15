import json
import jsonpickle
# обратите внимание как мы определяем ссылку
# на классы из других файлов
# from имя_документа import имя_класса
from adress import Address
from student import Student
# мы можем настроить конфигурацию для своих нужд
jsonpickle.set_encoder_options('json',
ensure_ascii=False,
sort_keys=False,
indent=4)
# объект адреса
address = Address("Икряное", "ул. Ленина", "30004")
# объект студента
student = Student("Железняков Д.В.", 42, address)
print("Конвертируем в формат JSON с помощью jsonpickle")
studJSON = jsonpickle.encode(student, unpicklable=False)
print(studJSON)