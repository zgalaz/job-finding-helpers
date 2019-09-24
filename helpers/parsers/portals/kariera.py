from pprint import pprint
from helpers.utils.logger import Logger
from helpers.parsers.portals.base import BaseJobOfferParser


DEFAULT_CITY = '0;r_1'
DEFAULT_FORM = '1;1'
DEFAULT_DAYS = 1


class KarieraJobOffersParser(BaseJobOfferParser):

    def __init__(self):
        super().__init__()

        self.logger = Logger(self.__class__.__name__)
        self.weburl = 'https://kariera.sk'

    def parse(self, url, verbose=False):

        # Get the parsed HTML content of the input URL
        parsed = self.content(url)

        # Get the job offers
        offers = self.offers(parsed)

        if verbose: pprint(offers)
        return offers

    def content(self, url):
        return self.parser.parse(url)

    def offers(self, parsed_html):

        # Validate the input data
        if not parsed_html:
            return None

        # Parse the HTML for job offers
        offers = parsed_html.find_all('div', class_='column2 offer-list-info')
        if not offers:
            self.logger.warning('No <div> tags with job offers found. Returning None')
            return None

        # Parse the job offers
        result = []
        for offer in offers:
            if offer.find('h2'):
                header = offer.find('h2').find('a', href=True, text=True)
                result.append(
                    {'url': header['href'],
                     'txt': header.text,
                     'emp': offer.find('a', class_='employer', href=True, text=True).text,
                     'loc': offer.find('span', class_='place').text}
                )

        return result


def get_job_offers(work_city=DEFAULT_CITY, work_form=DEFAULT_FORM, day_delta=DEFAULT_DAYS, verbose=False):

    # Get the parser
    parser = KarieraJobOffersParser()

    # Prepare the API call
    url = f'https://kariera.zoznam.sk/pracovne-ponuky/?' \
          f's=:absolvent:1:' \
          f'age:{day_delta}:' \
          f'category:0;c_28|1;c_1|2;c_17|3;c_19|4;c_39|:' \
          f'city:{work_city}|' \
          f'pomery:{work_form}|' \
          f'school:7'

    # Return the job offers
    return parser.parse(url, verbose=verbose)
