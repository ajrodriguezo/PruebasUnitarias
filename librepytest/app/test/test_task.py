import pytest

from datetime import datetime
from datetime import timedelta

from app.task import Task 

class TestTask():
    
    def test_task(self):
        pass
    
    def test_new_task(self):
        due_date = datetime.now()
        
        task = Task('Title', 'Description', 'eduardo', due_date)
        
        assert task.title == 'Title'
        assert task.description == 'Description'
        assert task.assigned_to == 'eduardo'
        assert task.due_date == due_date
        
    def test_due_date_error(self):
        due_date = datetime.now() - timedelta(days=1)
        Task('Title', 'Description', 'eduardo', due_date)
        #