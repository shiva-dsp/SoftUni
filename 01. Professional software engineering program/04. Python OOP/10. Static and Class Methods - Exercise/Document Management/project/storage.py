from .category import Category
from .topic import Topic
from .document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    @staticmethod
    def __find_object_by_id(given_id, given_sequence):
        for searched_object in given_sequence:
            if searched_object.id == given_id:
                return searched_object

    def edit_category(self, category_id: int, new_name: str):
        category = self.__find_object_by_id(category_id, self.categories)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__find_object_by_id(topic_id, self.topics)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__find_object_by_id(document_id, self.documents)
        document.file_name = new_file_name

    @staticmethod
    def __delete_item(given_item, given_sequence):
        if given_item in given_sequence:
            given_sequence.remove(given_item)

    def delete_category(self, category_id):
        category = self.__find_object_by_id(category_id, self.categories)
        self.__delete_item(category, self.categories)

    def delete_topic(self, topic_id):
        topic = self.__find_object_by_id(topic_id, self.topics)
        self.__delete_item(topic, self.topics)

    def delete_document(self, document_id):
        document = self.__find_object_by_id(document_id, self.documents)
        self.__delete_item(document, self.documents)

    def get_document(self, document_id):
        return self.__find_object_by_id(document_id, self.documents)

    def __repr__(self):
        return '\n'.join(str(document.__repr__()) for document in self.documents)