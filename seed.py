import requests
import time

BASE_URL = "http://localhost:8000"
USER_ID = "tester"

def wait_for_server(timeout=30):
    start = time.time()
    while time.time() - start < timeout:
        try:
            resp = requests.get(f"{BASE_URL}/health")
            if resp.status_code == 200:
                print("✅ Сервер готов!")
                return True
        except requests.exceptions.ConnectionError:
            print("⏳ Ожидание запуска сервера...")
        time.sleep(2)
    print("❌ Сервер не запустился.")
    return False

def create_tender(title, description):
    response = requests.post(
        f"{BASE_URL}/tenders/",
        json={"title": title, "description": description},
        headers={"X-User-ID": USER_ID}
    )
    if response.status_code == 201:
        return response.json()["id"]
    else:
        print(f"Ошибка при создании {title}: {response.status_code}")
        return None

def update_status(tender_id, new_status, reason):
    response = requests.put(
        f"{BASE_URL}/tenders/{tender_id}/status",
        json={"new_status": new_status, "reason": reason},
        headers={"X-User-ID": USER_ID}
    )
    if response.status_code != 200:
        print(f"Ошибка обновления статуса {tender_id}: {response.status_code}")

def main():
    if not wait_for_server():
        return

    tenders = []
    tenders.append(create_tender("Разработка веб-сайта", "Создать лендинг"))
    tenders.append(create_tender("Мобильное приложение", "Приложение для заказа еды"))
    tenders.append(create_tender("Дизайн-проект", "Фирменный стиль"))

    for idx, t in enumerate(tenders):
        if t is None:
            continue
        if idx == 0:
            update_status(t, "active", "Активен")
            time.sleep(0.5)
            update_status(t, "won", "Победитель")
        elif idx == 1:
            update_status(t, "active", "Активен")
            time.sleep(0.5)
            update_status(t, "lost", "Проигран")
        else:
            update_status(t, "active", "Активен")

    print(f"✅ Создано {len(tenders)} тендеров. Откройте http://localhost:8000/docs")

if __name__ == "__main__":
    main()