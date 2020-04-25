from matplotlib import pyplot as plt
import requests


def get_country_timeline(country_code):
    url = "https://thevirustracker.com/free-api?countryTimeline={}".format(
        country_code)
    response = requests.get(url).json()
    country = response["countrytimelinedata"][0]["info"]["title"]
    data = response["timelineitems"][0]
    del data['stat']
    dev_x = list(data.keys())
    dev_y = [x['new_daily_cases'] for x in list(data.values())]
    return (dev_x, dev_y, country)

def plot_daily_cases(*countries):
    for country in countries:
        data = get_country_timeline(country)
        plt.plot(range(len(data[1])), data[1], label=data[2])
    plt.legend()
    plt.grid()
    plt.title("Daily Coronavirus count")
    plt.xlabel("Days since first case")
    plt.ylabel("Case count per day")
    plt.show()
    return True


if __name__ == "__main__":
    plot_daily_cases("IN","GB")
