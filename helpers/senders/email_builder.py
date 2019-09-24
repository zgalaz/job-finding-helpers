from helpers.parsers.websites.parser import get_domain
from helpers.senders.data_formatter import as_html, as_plain


DELIMITERS = {'html': '<br>', 'plain': '\r\n'}


def get_intro(name, link, hours, return_type='html'):
    content = [f'Ahoj {name},', f'toto sú ponuky zverejnené na portáli {link} za posledných {hours} hod.:']
    as_type = DELIMITERS.get(return_type, ' ').join(content)
    return as_type


def get_outro(return_type='html'):
    content = f'Tvoj job finder helper'
    as_type = DELIMITERS.get(return_type, ' ') + content
    return as_type


def get_email_message_html(body, name, link, day):
    intro = get_intro(name, f'<a href="{link}">{get_domain(link)}</a>', int(day * 24), return_type='html')
    offer = as_html(body)
    outro = get_outro(return_type='html')
    return intro + offer + outro


def get_email_message_plain(body, name, link, day):
    intro = get_intro(name, get_domain(link), int(day * 24), return_type='plain')
    offer = as_plain(body)
    outro = get_outro(return_type='plain')
    return intro + offer + outro
