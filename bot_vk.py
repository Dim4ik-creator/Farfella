import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests

VK_TOKEN = 'vk1.a.2NsNzEhfZGcXBWpwDYEm2ixlnbpVuEk85Y4-Tnq7Q5eF_cJ0tAmTioVnwGLaQHwaiqviQTAiHGitZHNA5SqkhvSSTBMnwE2Y1C7qjxZUH5vuTFtTA0pktaOW6Uyv7IavKQCwFgpGcpj2gbXh_IS0qAC4kve7n1VwNApMkGUNTYQywcxAF2pHZAL9ecGq_por972EIq_XNdGcwiGY0qFfSA'


def get_weather(city):
    api_key = 'e36a9952f118d2caee0f6e607d21f0a5'

    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',
        'lang': 'ru'
    }

    response = requests.get(base_url, params=params)

    data = response.json()

    print(f"Response: {data}")

    if data['cod'] == 200:

        weather = data['weather'][0]['description']
        temp = int(data['main']['temp'])
        temp_real = int(data["main"]["feels_like"])
        wind = data["wind"]["speed"]

        return f"Погода в {city}: {weather}, температура: {temp}°C, Ощущается как: {temp_real}°C, Скорость ветра: {wind} м/c"

    else:
        return "Не удалось получить данные о погоде."


def main():
    vk_session = vk_api.VkApi(token=VK_TOKEN)

    longpoll = VkLongPoll(vk_session)

    try:
        for event in longpoll.listen():

            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                user_message = event.text.lower()

                city = user_message.split('в ')[-1]

                weather_info = get_weather(city)

                vk_session.method('messages.send', {
                    'user_id': event.user_id,
                    'message': weather_info,
                    'random_id': 0
                })

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    main()
