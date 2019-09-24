from pprint import pprint
from helpers.utils.logger import Logger
from helpers.parsers.portals.base import BaseJobOfferParser


DEFAULT_CITY = 'bratislava'
DEFAULT_FORM = 'plny-uvazok'
DEFAULT_DAYS = 1


class ProfesiaJobOffersParser(BaseJobOfferParser):

    def __init__(self):
        super().__init__()

        self.logger = Logger(self.__class__.__name__)
        self.weburl = 'https://www.profesia.sk'

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
        offers = parsed_html.find_all('li', class_='list-row')
        if not offers:
            self.logger.warning('No <li> tags with job offers found. Returning None')
            return None

        # Parse the job offers
        result = []
        for offer in offers:
            if offer.find('h2'):
                header = offer.find('h2').find('a', href=True, text=True)
                result.append(
                    {'url': '/'.join((self.weburl, header['href'])),
                     'txt': header.text,
                     'emp': offer.find('span', class_='employer'),
                     'loc': offer.find('span', class_='job-location')}
                )

        return result


def get_job_offers(work_city=DEFAULT_CITY, work_form=DEFAULT_FORM, day_delta=DEFAULT_DAYS, verbose=False):

    # Get the parser
    parser = ProfesiaJobOffersParser()

    # Prepare the API call
    url = f'https://www.profesia.sk/praca/' \
          f'{work_city}/' \
          f'{work_form}/?' \
          f'business_areas[]=11&' \
          f'business_areas[]=67&' \
          f'business_areas[]=22&' \
          f'business_areas[]=51&' \
          f'business_areas[]=35&' \
          f'business_areas[]=73&' \
          f'business_areas[]=72&' \
          f'business_areas[]=36&' \
          f'count_days={day_delta}&' \
          f'education_levels[]=7&' \
          f'offer_agent_flags=8388'

    # Return the job offers
    return parser.parse(url, verbose=verbose)
