
from .Subject_Model import Subject
class LogSystem:
    def __init__(self,dict):
        self.dict=dict
    def add(self,subject):
        self.dict[subject.name]=subject.dates
    