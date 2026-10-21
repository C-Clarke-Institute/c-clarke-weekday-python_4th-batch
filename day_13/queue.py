
class QueueError(Exception):
    pass

class Queue:

    def __init__(self):
        self.__queue = []

    def put(self,elem):
        self.__queue.insert(0, elem)

    def get(self):
        if len(self.__queue) > 0:
            val = self.__queue[-1]
            del self.__queue[-1]
            return val

        raise QueueError("Empty Queue")

restaurant_queue = Queue()
restaurant_queue.put("Ranil")
restaurant_queue.put("Anura")
restaurant_queue.put("Namal")

try:
    person = restaurant_queue.get()
    print(person)
except QueueError as e:
    print(f"{str(e)}")
