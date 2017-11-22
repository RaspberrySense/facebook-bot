from random import choice, randint


def randomly_capitalize(text):
    if randint(0, 1):   # randomly decide whether to capitalize
        return text.capitalize()
    return text


def random_smiley(can_be_empty=True):
    # NOTE: `☺` is more probable if smiley cannot be empty
    return choice([':)', '☺', '😇', '' if can_be_empty else '☺'])


def random_exclamation(can_be_empty=True):
    # NOTE: `!` is more probable if exclamation cannot be empty
    return choice(['!', '.', '' if can_be_empty else '!'])


hello = [
    'hello'
    'hey there'
    'hey',
    'hi',
]


def get_hello():
    randomly_capitalize(choice(hello))


thanks = [
    'thank you'
    'thanks',
]


def get_thank():
    return randomly_capitalize(choice(thanks)) + random_smiley()


thank_replies = [
    "you're welcome",
    'happy to help',
    'my pleasure'
    'no problem',
    'no probs',
]


def get_thank_reply():
    return randomly_capitalize(choice(thank_replies)) + random_exclamation()


fine_replies = [
    "i'm good",
    "i'm fine",
    "i'm OK"
]


def get_fine_reply():
    return randomly_capitalize(choice(fine_replies)) + random_exclamation()


yes = [
    'yes',
    'yeah',
    'yep'
]


def get_yes():
    return choice(yes)


no = [
    'no',
    'nah',
    'nope'
]


def get_no():
    return choice(no)


sensor_replies = {
    'temperature': {
        'get_temp': [
            "It is {value}°C in here",
            "It's {value}°C",
            "The temperature is {value}°C in here",
            "The temperature is {value}°C",
            "{value}°C",
        ],
        'check_temp_high': {
            'true': [
                "{yes}",
                "{yes}, it is",
                "{yes}, it's quite hot",
                "{yes}, it's hot in here",
                "{yes}, it's quite hot in here",
            ],
            'false': [
                "{no}",
                "{no}, it's not",
                "{no}, it's rather quite cold",
                "{no}, it's actually quite cold",
                "{no}, it's actually quite cold in here",
            ],
            'other': [
                "{no}",
                "{no}, it's warm",
                "{no}, it's actually quite warm",
                "{no}, it's actually quite warm in here",
            ]
        },
        'check_temp_low': {
            'true': [
                "{yes}",
                "{yes}, it is",
                "{yes}, it's quite cold",
                "{yes}, it's cold in here",
                "{yes}, it's quite cold in here",
            ],
            'false': [
                "{no}",
                "{no}, it's not",
                "{no}, it's rather quite hot",
                "{no}, it's actually quite hot",
                "{no}, it's actually quite hot in here",
            ],
            'other': [
                "{no}",
                "{no}, it's warm",
                "{no}, it's actually quite warm",
                "{no}, it's actually quite warm in here",
            ]
        },
        'check_temp_value_above': {
            'true': [
                "{yes}",
                "{yes}, it is",
                "{yes}, it's above {value}°C",
                "{yes}, it's above {value}°C in here",
            ],
            'false': [
                "{no}",
                "{no}, it's not",
                "{no}, it's below {value}°C",
                "{no}, it's below {value}°C in here",
            ]
        },
        'check_temp_value_below': {
            'true': [
                "{yes}",
                "{yes}, it is",
                "{yes}, it's below {value}°C",
                "{yes}, it's below {value}°C in here",
            ],
            'false': [
                "{no}",
                "{no}, it's not",
                "{no}, it's above {value}°C",
                "{no}, it's above {value}°C in here",
            ]
        },
    },

    # Humidity ----------------------------------------------------------------
    'humidity': {
        'get_humidity': [
            "It is {value}%% in here",
            "It's {value}%%",
            "The humidity is {value}%% in here",
            "The humidity is {value}%%",
            "{value}%%",
        ],
        'check_humidity_high': {
            'true': [
                "{yes}",
                "{yes}, it is",
                "{yes}, it's quite humid",
                "{yes}, it's humid in here",
                "{yes}, it's quite humid in here",
            ],
            'false': [
                "{no}",
                "{no}, it's not",
                "{no}, it's rather quite dry",
                "{no}, it's actually quite dry",
                "{no}, it's actually quite dry in here",
            ],
            'other': [
                "{no}",
                "{no}, it's pleasant",
                "{no}, it's actually quite pleasant",
                "{no}, it's actually quite pleasant in here",
            ]
        },
        'check_humidity_low': {
            'true': [
                "{yes}",
                "{yes}, it is",
                "{yes}, it's quite dry",
                "{yes}, it's dry in here",
                "{yes}, it's quite dry in here",
            ],
            'false': [
                "{no}",
                "{no}, it's not",
                "{no}, it's rather quite humid",
                "{no}, it's actually quite humid",
                "{no}, it's actually quite humid in here",
            ],
            'other': [
                "{no}",
                "{no}, it's pleasant",
                "{no}, it's actually quite pleasant",
                "{no}, it's actually quite pleasant in here",
            ]
        },
        'check_humidity_value_above': {
            'true': [
                "{yes}",
                "{yes}, it is",
                "{yes}, it's above {value}%%",
                "{yes}, it's above {value}%% in here",
            ],
            'false': [
                "{no}",
                "{no}, it's not",
                "{no}, it's below {value}%%",
                "{no}, it's below {value}%% in here",
            ]
        },
        'check_humidity_value_below': {
            'true': [
                "{yes}",
                "{yes}, it is",
                "{yes}, it's below {value}%%",
                "{yes}, it's below {value}%% in here",
            ],
            'false': [
                "{no}",
                "{no}, it's not",
                "{no}, it's above {value}%%",
                "{no}, it's above {value}%% in here",
            ]
        },
    },

    # TODO: replies for other sensors
}


def get_sensor_reply(sensor_type, intent, condition, value=''):
    reply = choice(sensor_replies[sensor_type][intent][condition])

    if '{yes}' in reply:
        if '{value}' in reply:
            reply = reply.format(yes=get_yes(), value=value)
        else:
            reply = reply.format(yes=get_yes())
    elif '{no}' in reply:
        if '{value}' in reply:
            reply = reply.format(no=get_no(), value=value)
        else:
            reply = reply.format(no=get_no())
    elif '{value}' in reply:
        reply = reply.format(value=value)

    return randomly_capitalize(reply)
