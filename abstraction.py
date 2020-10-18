from abc import ABC, abstractmethod
class dog(ABC):
    def daySchedule(self, time):
        print("you fed the dog at: ",time)

    @abstractmethod

    def beat(self, time):
        pass

class correctSchedule(dog):
    def beat(self, time):
        print("the dog is supposed to be fed at {}".format(time))


obj= correctSchedule()
obj.daySchedule("9 AM")
obj.beat("9 AM")
