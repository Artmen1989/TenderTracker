import requests
import time
import uuid

BASE_URL = "http://localhost:8000"
USER_ID = "tester"

def create_tender(title, description):
    response = requests.post(
        f"{BASE_URL}/tenders/",
        json={"title": title, "description": description},
        headers={"X-User-ID": USER_ID}
    )
    if response.status_code == 201:
        return response.json()["id"]
    else:
        print(f"Ошибка при создании тендера {title}: {response.status_code} - {response.text}")
        return None

def update_status(tender_id, new_status, reason):
    response = requests.put(
        f"{BASE_URL}/tenders/{tender_id}/status",
        json={"new_status": new_status, "reason": reason},
        headers={"X-User-ID": USER_ID}
    )
    if response.status_code != 200:
        print(f"Ошибка при обновлении статуса {tender_id}: {response.status_code} - {response.text}")

def main():
    print("Ожидание готовности сервиса...")
    time.sleep(3)  # даём серверу время запуститься

    # Создаём несколько тендеров
    tenders = []
    tenders.append(create_tender("Разработка веб-сайта", "Создать лендинг для компании"))
    tenders.append(create_tender("Мобильное приложение", "Разработать приложение для заказа еды"))
    tenders.append(create_tender("Дизайн-проект", "Разработать фирменный стиль"))

    # Обновляем статусы
    for idx, tender_id in enumerate(tenders):
        if tender_id is None:
            continue
        # Первый тендер: draft → active → won
        if idx == 0:
            update_status(tender_id, "active", "Тендер перешёл в активную фазу")
            time.sleep(0.5)
            update_status(tender_id, "won", "Победитель определён")
        # Второй: draft → active → lost
        elif idx == 1:
            update_status(tender_id, "active", "Тендер активен")
            time.sleep(0.5)
            update_status(tender_id, "lost", "Тендер проигран")
        # Третий: draft → active (оставляем активным)
        else:
            update_status(tender_id, "active", "Тендер переведён в активную фазу")

    print(f"✅ Создано и обработано {len(tenders)} тендеров.")
    print("Откройте http://localhost:8000/docs для просмотра и тестирования.")

if __name__ == "__main__":
    main()