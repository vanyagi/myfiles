import json
# создаем пользовательский класс
class Article:
    def __init__(self, title, isbnСode):
        self.title = title
        self.isbnСode = isbnСode
    def get_title(self):
        return self.title
    def get_isbnСode(self):
        return self.isbnСode
# создаем экземпляр класса
art = Article("Микроклимат в помещении", "38-41-42-ПР")
# пытаемся сериализовать его в JSON, но...
#json.dumps(art)
def class_to_dict(obj):
    return obj.__dict__
data = json.dumps(art, default=class_to_dict, ensure_ascii=False)
print(data)