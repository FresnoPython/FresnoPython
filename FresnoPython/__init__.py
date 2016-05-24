import datetime
import webbrowser

import dateutil.rrule

from .compat import quote_plus
from .utils import indent

# What.
name = 'Fresno.py'
description = 'The Fresno Python User Group'

# Where.
location = 'Bitwise Industries'
address = '''
700 Van Ness Ave
Fresno, CA
'''

map = 'https://www.google.com/maps?q={0}'.format(
    quote_plus(' '.join(address.split())))

# When.
schedule = dateutil.rrule.rrule(
    freq=dateutil.rrule.MONTHLY,
    byweekday=dateutil.rrule.TU,
    bysetpos=4
)

# On the web.
website = 'http://FresnoPython.com'
twitter = 'http://twitter.com/FresnoPython'

def open_website():
    return webbrowser.open(website)


def open_twitter():
    return webbrowser.open(twitter)


def open_map():
    return webbrowser.open(map)


def next_meeting_date(date=None):
    if date is None:
        date = datetime.date.today()

    if isinstance(date, datetime.date):
        date = datetime.datetime.combine(date, datetime.datetime.min.time())

    return datetime.datetime.combine(
        schedule.after(date).date(),
        datetime.time(18, 30)
    )


def message():
    template = '''
        {name} -- {description}

        {website}

        Fresno.py's mission is to foster a welcoming and diverse community
        of Python developers and promote the use of the Python programming
        language in the Central Valley. People of all skill levels are welcome;
        if you are interested in Python, we'd love to have you join us!

        Next meeting: {next_meeting}

        {location}
        {address}

        Map: {map}

        Follow us on Twitter!
        {twitter}
    '''

    content = indent(template.format(
        name=name,
        description=description,
        website=website,
        twitter=twitter,
        location=location,
        address=address.strip(),
        map=map,
        next_meeting=next_meeting_date().strftime('%A %B %e, %Y at%l:%M%P'),
    ))
    return content
