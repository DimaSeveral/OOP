
_subscribers = []


def subscribe(name, notify_func):

    subscriber = (name, notify_func)
    if subscriber not in _subscribers:
        _subscribers.append(subscriber)
        print(f"Подписчик {name} добавлен.")


def unsubscribe(name, notify_func):
    
    subscriber = (name, notify_func)
    if subscriber in _subscribers:
        _subscribers.remove(subscriber)
        print(f"Подписчик {name} удалён.")


def notify_subscribers(news):
   
    print(f"\nНОВОСТЬ: {news}")
    for name, notify_func in _subscribers:
        notify_func(name, news)



def email_notify(name, news):
    print(f"{name} получил email: '{news}'")

def sms_notify(name, news):
    print(f"{name} получил SMS: '{news}'")



if __name__ == "__main__":
    
    subscribe("Алиса", email_notify)
    subscribe("Боб", sms_notify)

    
    notify_subscribers("Погода сегодня солнечная!")

    
    subscribe("Чарли", email_notify)
    unsubscribe("Боб", sms_notify)

    
    notify_subscribers("Завтра ожидается дождь!")