import requests

from utils.coinranking_api.config import RAPID_API_KEY, RAPID_API_URL


def get_all_coins(
        add_url: str = 'coins',
        referenceCurrencyUuid: str = 'yhjMzLPhuIDl',
        timePeriod: str = '24h',
        tiers: str = '1',
        orderBy: str = 'price',
        orderDirection: str = 'asc',
        limit: str = '10',
        offset: str = '0',
) -> dict:
    """
    Get a list of coins from Coinranking.com API.

    :param add_url: additional text to url
    :param referenceCurrencyUuid: UUID of reference currency, in which all the prices are calculated.
    This includes the price, the change and the sparkline. Defaults to US Dollar
    :param timePeriod: By setting the timePeriod the change percentage and sparkline in the response will be
    calculated accordingly
        Default value: 24h
        Allowed values:
        1h 3h 12h 24h 7d 30d 3m 1y 3y 5y
    :param tiers: With this parameter you can filter coins on the tiers you need. Read more about out our tiers in
    methodology https://support.coinranking.com/article/56-what-is-our-ranking-methodology
    :param orderBy: Index to order by. All sortings excluding listedAt still take our different tiers of coins into
    account.
        Default value: price
        Allowed values:
        price marketCap 24hVolume change listedAt
    :param orderDirection: Applies direction to the orderBy query, which can be in ascending or descending order.
        Default value: desc
        Allowed values:
        desc asc
    :param limit: Limit. Used for pagination. The maximum amount of results you can fetch in one request is 5000 for
     the Startup and Professional plan, and 100 for the Free plan.
        Default value: 50
        Size range: 0-5000
    :param offset: Offset. Used for pagination.
        Default value: 0

    :return: JSON response from Coinranking.com
    """

    url = RAPID_API_URL + add_url

    querystring = {
        "referenceCurrencyUuid": referenceCurrencyUuid,
        "timePeriod": timePeriod,
        "tiers[0]": tiers,
        "orderBy": orderBy,
        "orderDirection": orderDirection,
        "limit": limit,
        "offset": offset
    }

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()


if __name__ == '__main__':
    print(get_all_coins())