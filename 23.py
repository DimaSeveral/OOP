class NewsPublisher:
    def __init__(self):
        self._subscribers = []  

    def subscribe(self, subscriber):

        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)
            print(f"Подписчик {subscriber.name} добавлен.")

    def unsubscribe(self, subscriber):

        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)
            print(f"Подписчик {subscriber.name} удалён.")

    def notify_subscribers(self, news):

        print(f"\nНОВОСТЬ: {news}")
        for subscriber in self._subscribers:
            subscriber.update(news)


class Subscriber:

    def __init__(self, name):
        self.name = name

    def update(self, news):
        raise NotImplementedError("Метод update() должен быть реализован!")


class EmailSubscriber(Subscriber):
    def update(self, news):
        print(f"{self.name} получил email: '{news}'")


class SMSSubscriber(Subscriber):
    def update(self, news):
        print(f"{self.name} получил SMS: '{news}'")



if __name__ == "__main__":
#экземпляр класса
    publisher = NewsPublisher() 

    alice = EmailSubscriber("Алиса")
    bob = SMSSubscriber("Боб")
    charlie = EmailSubscriber("Чарли")
   


    publisher.subscribe(alice)
    publisher.subscribe(bob)

    publisher.notify_subscribers("Погода сегодня солнечная!")

 
    publisher.subscribe(charlie)
    publisher.unsubscribe(bob)
    

    publisher.notify_subscribers("Завтра ожидается дождь!")