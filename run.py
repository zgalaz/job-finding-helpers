import argparse
from datetime import datetime
from helpers.parsers.portals import profesia
from helpers.parsers.portals import kariera
from helpers.senders.email_sender import send_email, prepare_email
from helpers.senders.email_builder import get_email_message_html, get_email_message_plain


# Analytical portal-specific data translator (more settings can be added as needed/moved to JSON settings)
translator = {
    'city': {
        'bratislava': {
            'profesia': 'bratislava',
            'kariera': '0;r_1'
        },
    },
    'form': {
        'fulltime': {
            'profesia': 'plny-uvazok',
            'kariera': '1;1'
        },
    },
}

# Analytical timestamp
today = datetime.now()
today = f'{today.day}. {today.month}. {today.year}'


def run_for_profesia(args):

    # Parse the job offers
    offers = profesia.get_job_offers(work_city=translator.get('city').get(args.city, {}).get('profesia', None),
                                     work_form=translator.get('form').get(args.form, {}).get('profesia', None),
                                     day_delta=args.delta)

    if offers:

        # Prepare the e-mail message with the job offers
        profesia_parser = profesia.ProfesiaJobOffersParser()
        profesia_message_text = get_email_message_plain(offers, args.name, profesia_parser.weburl, args.delta)
        profesia_message_html = get_email_message_html(offers, args.name, profesia_parser.weburl, args.delta)

        # Send the offers
        send_email(from_address='job.finder.helpers@gmail.com',
                   to_address={'display_name': args.name, 'username': u_name, 'domain': d_name},
                   subject=f'profesia.sk {today}',
                   plaintext=profesia_message_text,
                   html=profesia_message_html)


def run_for_kariera(args):

    # Parse the job offers
    offers = kariera.get_job_offers(work_city=translator.get('city').get(args.city, {}).get('kariera', None),
                                    work_form=translator.get('form').get(args.form, {}).get('kariera', None),
                                    day_delta=args.delta)

    if offers:

        # Prepare the e-mail message with the job offers
        kariera_parser = kariera.KarieraJobOffersParser()
        kariera_message_text = get_email_message_plain(offers, args.name, kariera_parser.weburl, args.delta)
        kariera_message_html = get_email_message_html(offers, args.name, kariera_parser.weburl, args.delta)

        # Send the offers
        send_email(from_address='job.finder.helpers@gmail.com',
                   to_address={'display_name': args.name, 'username': u_name, 'domain': d_name},
                   subject=f'kariera.sk {today}',
                   plaintext=kariera_message_text,
                   html=kariera_message_html)


if __name__ == '__main__':

    # -------------------------
    # Parse the input arguments
    # -------------------------

    arg_parser = argparse.ArgumentParser(description='profesia.sk parser')
    arg_parser.add_argument('-c', '--city', type=str, help='job city')
    arg_parser.add_argument('-f', '--form', type=str, help='job form')
    arg_parser.add_argument('-n', '--name', type=str, help='name of the recipient')
    arg_parser.add_argument('-e', '--email', type=str, help='email of the recipient')
    arg_parser.add_argument('-d', '--delta', type=int, help='day delta')
    arg_parser.add_argument('--profesia', help='use profesia.sk', action='store_true')
    arg_parser.add_argument('--kariera', help='use kariera.sk', action='store_true')
    args = arg_parser.parse_args()

    # ---------------------
    # Prepare the machinery
    # ---------------------

    # Continue only if any portal is to be analyzed
    if not any((args.profesia, args.kariera)):
        print('No portal to analyze, exiting.')
        exit(0)

    # Prepare e-mail sending
    u_name, d_name = prepare_email(args.email)

    # -----------
    # profesia.sk
    # -----------
    if args.profesia: run_for_profesia(args)

    # -----------------
    # kariera.zoznam.sk
    # -----------------
    if args.kariera: run_for_kariera(args)
