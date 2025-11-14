def publish_news(news, send_to_alice=True, send_to_bob=True, send_to_charlie=False):
 
    print(f"\nНОВОСТЬ: {news}")

    if send_to_alice:
        print("Алиса получил email:", f"'{news}'")
    if send_to_bob:
        print("Боб получил SMS:", f"'{news}'")
    if send_to_charlie:
        print("Чарли получил email:", f"'{news}'")


if __name__ == "__main__":

    publish_news("Погода сегодня солнечная!", send_to_alice=True, send_to_bob=True, send_to_charlie=False)

    publish_news("Завтра ожидается дождь!", send_to_alice=True, send_to_bob=False, send_to_charlie=True)