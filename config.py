"""All your settings live here. Edit this file, never the others."""

# ----- The cards you're tracking -----
CARDS = {
    "Chase Sapphire Preferred": [
        "sapphire preferred", "csp", "chase sapphire", "ultimate rewards",
        "chase offers", "chase travel"
    ],
    "BoA Atmos / Premium Rewards": [
        "atmos", "atmos rewards", "atmos ascent", "atmos summit",
        "alaska airlines visa", "hawaiian airlines visa",
        "bank of america premium rewards", "premium rewards elite",
        "customized cash rewards", "preferred rewards", "bofa rewards",
        "bankamerideals",
    ],
}

# ----- Sources to poll (public, no login needed) -----
RSS_FEEDS = [
    ("Doctor of Credit",  "https://www.doctorofcredit.com/feed/"),
    ("The Points Guy",    "https://thepointsguy.com/feed/"),
    ("Frequent Miler",    "https://frequentmiler.com/feed/"),
    ("One Mile at a Time","https://onemileatatime.com/feed/"),
    ("View From The Wing","https://viewfromthewing.com/feed/"),
]

REDDIT_FEEDS = [
    ("r/CreditCards", "https://www.reddit.com/r/CreditCards/new.json?limit=100"),
    ("r/churning",    "https://www.reddit.com/r/churning/new.json?limit=100"),
]

# ----- Classification keywords -----
KW_NEW       = ["launch", "announce", "added", "now earns", "new benefit",
                "introduces", "unveils", "debut", "rolls out"]
KW_EXPIRING  = ["expire", "expires", "ends ", "last day", "limited time",
                "through ", "deadline", "must use by", "valid until"]
KW_DEVALUE   = ["devalue", "no longer", "removed", "discontinued",
                "nerf", "cuts", "reduces", "ending", "loses"]

EXPIRING_WINDOW_DAYS = 30

# ----- Notifier choice: "discord" or "line" -----
NOTIFIER = "line"
