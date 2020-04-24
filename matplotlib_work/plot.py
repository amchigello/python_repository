from matplotlib import pyplot as plt
import requests


def get_response(url):
    response = requests.get(url).json()
    data = response["timelineitems"][0]
    del data['stat']
    dev_x = list(data.keys())
    dev_y = [x['new_daily_cases'] for x in list(data.values())]
    return (dev_x, dev_y)


if __name__ == "__main__":
    india_data = get_response(
        "https://thevirustracker.com/free-api?countryTimeline=IN")
    us_data = get_response(
        "https://thevirustracker.com/free-api?countryTimeline=KR")

    plt.plot(range(len(india_data[1])), india_data[1], label="India", color="#10a6c4")
    plt.plot(range(len(us_data[1])), us_data[1], label="South Korea", color="#97c410")
    plt.legend()
    plt.grid()
    plt.title("Daily Coronavirus count")
    plt.xlabel("Days since first case")
    plt.ylabel("Case count per day")
    plt.show()

