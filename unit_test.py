import unittest
from Worker1 import Worker, Collection, dec_sort, dec_search


class Test_Worker(unittest.TestCase):
    collection = Collection()

    def test_add(self):
        worker = Worker(name='John', surname='Doe', department='IT', salary='40000')
        self.assertEqual(worker.get_name(), "John")
        self.assertEqual(worker.get_surname(), "Doe")
        self.assertEqual(worker.get_department(), "IT")
        self.assertEqual(worker.get_salary(), "40000")

    def test_id(self):
        worker1 = Worker(name="John", surname="Doe", department="IT", salary="40000")
        worker2 = Worker(name="Jo", surname="Do", department="PR", salary="30000")
        self.assertNotEqual(worker1.get_id(), worker2.get_id())


class Test_Collection(unittest.TestCase):

    def setUp(self):
        self.collection = Collection()

    def test_delete_worker(self):
        worker = Worker(name="John", surname="Doe", department="IT", salary=50000)
        self.collection.workers.append(worker)
        self.collection.delete_worker(worker.get_id())
        self.assertEqual(len(self.collection.workers), 0)

    def test_add_worker(self):
        worker = Worker(name="John", surname="Doe", department="IT", salary="40000")
        self.collection.workers.append(worker)
        self.assertEqual(len(self.collection.workers), 1)

    def test_sort_workers(self):
        worker1 = Worker(name="John", surname="Doe", department="IT", salary="40000")
        worker2 = Worker(name="Jane", surname="Doe", department="IT", salary="40000")
        self.collection.workers = [worker1, worker2]
        self.collection.sort_workers('name')
        self.assertEqual(self.collection.workers, [worker2, worker1])


if __name__ == "__main__":
    unittest.main()
