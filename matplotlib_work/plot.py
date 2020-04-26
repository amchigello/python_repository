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


def plot_daily_cases_bar(country_code, **kwargs):
    first_n_days = kwargs.get('first_n_days', None)
    last_n_days = kwargs.get('last_n_days', None)
    data = get_country_timeline(country_code)

    if (first_n_days != None):
        y_axis = data[1][:first_n_days]
        xlabel = "First {} days".format(first_n_days)
    elif (last_n_days != None):
        y_axis = data[1][-last_n_days:]
        xlabel = "Last {} days".format(last_n_days)
    else:
        y_axis = data[1]
        xlabel = "Days since the first case"

    x_axis = range(len(y_axis))
    label = data[2]
    plt.bar(x_axis, y_axis, label=label)
    plt.legend()
    plt.grid()
    plt.title("Daily Coronavirus count")
    plt.xlabel(xlabel)
    plt.ylabel("Case count per day")
    plt.show()
    return True


def main():
    # plot_daily_cases("IN", "GB")
    plot_daily_cases_bar("IN", last_n_days=30)


if __name__ == "__main__":
    main()