"""All your settings live here."""

CARDS = {
    "Chase Sapphire Preferred": [
        "sapphire preferred", "csp", "chase sapphire", "ultimate rewards",
        "chase offers", "chase travel", "hyatt", "united airlines",
        "aeroplan", "flying blue", "singapore airlines", "british airways",
    ],
    "BoA Atmos / Premium Rewards": [
        "atmos", "atmos rewards", "atmos ascent", "atmos summit",
        "alaska airlines", "hawaiian airlines", "oneworld",
        "cathay pacific", "japan airlines", "jal",
    ],
    "Amex": [
        "amex", "american express", "membership rewards",
        "amex gold", "amex platinum", "amex transfer",
        "ana", "all nippon", "cathay", "singapore airlines",
        "eva air", "hilton", "marriott",
    ],
    "Citi": [
        "citi", "citibank", "thankyou points", "citi premier",
        "citi strata", "citi transfer", "eva air", "singapore airlines",
        "cathay pacific", "turkish airlines",
    ],
    "Asia Miles": [
        "asia miles", "cathay pacific", "eva air", "長榮",
        "ana mileage", "jal mileage", "star alliance",
        "oneworld", "skyteam", "taipei", "tokyo", "shanghai",
        "beijing", "hong kong", "taiwan", "japan", "china",
        "asia award", "asia route", "transpacific",
    ],
}

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
    ("r/awardtravel", "https://www.reddit.com/r/awardtravel/new.json?limit=100"),
]

KW_NEW       = ["launch", "announce", "added", "now earns", "new benefit",
                "introduces", "unveils", "debut", "rolls out", "new route",
                "bonus transfer", "transfer bonus"]
KW_EXPIRING  = ["expire", "expires", "ends ", "last day", "limited time",
                "through ", "deadline", "must use by", "valid until"]
KW_DEVALUE   = ["devalue", "no longer", "removed", "discontinued",
                "nerf", "cuts", "reduces", "ending", "loses"]

EXPIRING_WINDOW_DAYS = 30

NOTIFIER = "line"
