# Fabric interface  
class TransportFactory:
    def create_transport(self):
        pass

# Transport interface
class Transport:
    def move(self):
        pass

# Transports
class Bus(Transport):
    def move(self):
        print("Автобус двигается по маршруту.")

class Metro(Transport):
    def move(self):
        print("Поезд метро двигается по туннелю.")

class LRT(Transport):
    def move(self):
        print("ЛРТ двигается по путям.")

class PublicTaxi(Transport):
    def move(self):
        print("Общественное такси везет пассажиров по городу.")

# Fabric
class BusFactory(TransportFactory):
    def create_transport(self):
        return Bus()

class MetroFactory(TransportFactory):
    def create_transport(self):
        return Metro()

class LRTFactory(TransportFactory):
    def create_transport(self):
        return LRT()

class PublicTaxiFactory(TransportFactory):
    def create_transport(self):
        return PublicTaxi()

# Client code
class TransportTracker:
    def __init__(self, transport_factory):
        self.transport = transport_factory.create_transport()

    def track_transport(self):
        print("Отслеживаем транспорт:")
        self.transport.move()

# Main code
if __name__ == "__main__":
    print("На чем Вы хотите добраться до точки?")
    print("Выберите вид транспорта:")
    print("1. Автобус")
    print("2. Метро")
    print("3. Легкий рапидный транспорт (ЛРТ)")
    print("4. Общественное такси")

    choice = input("Введите номер выбранного транспорта: ")

    if choice == "1":
        tracker = TransportTracker(BusFactory())
        tracker.track_transport()
    elif choice == "2":
        tracker = TransportTracker(MetroFactory())
        tracker.track_transport()
    elif choice == "3":
        tracker = TransportTracker(LRTFactory())
        tracker.track_transport()
    elif choice == "4":
        tracker = TransportTracker(PublicTaxiFactory())
        tracker.track_transport()
    else:
        print("Некорректный выбор. Пожалуйста, выберите от 1 до 4.")
