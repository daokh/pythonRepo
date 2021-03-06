# -*- coding: utf-8 -*-

import re
from numbers import Integral
from collections import namedtuple

__all__ = ["countries"]

"""
>>> from iso3166 import countries
countries.get('')
"""


def _import_locale(locale):
    return __import__('iso3166.' + locale, {}, {}, ['iso3166'])


Country = namedtuple('Country', 'name, alpha2, alpha3, numeric')
Country.local_name = lambda self, locale: _import_locale(locale
).names.get(self.alpha3, self.name)

_records = [
    Country(u"Afghanistan", "AF", "AFG", "004"),
    Country(u"Åland Islands", "AX", "ALA", "248"),
    Country(u"Albania", "AL", "ALB", "008"),
    Country(u"Algeria", "DZ", "DZA", "012"),
    Country(u"American Samoa", "AS", "ASM", "016"),
    Country(u"Andorra", "AD", "AND", "020"),
    Country(u"Angola", "AO", "AGO", "024"),
    Country(u"Anguilla", "AI", "AIA", "660"),
    Country(u"Antarctica", "AQ", "ATA", "010"),
    Country(u"Antigua and Barbuda", "AG", "ATG", "028"),
    Country(u"Argentina", "AR", "ARG", "032"),
    Country(u"Armenia", "AM", "ARM", "051"),
    Country(u"Aruba", "AW", "ABW", "533"),
    Country(u"Australia", "AU", "AUS", "036"),
    Country(u"Austria", "AT", "AUT", "040"),
    Country(u"Azerbaijan", "AZ", "AZE", "031"),
    Country(u"Bahamas", "BS", "BHS", "044"),
    Country(u"Bahrain", "BH", "BHR", "048"),
    Country(u"Bangladesh", "BD", "BGD", "050"),
    Country(u"Barbados", "BB", "BRB", "052"),
    Country(u"Belarus", "BY", "BLR", "112"),
    Country(u"Belgium", "BE", "BEL", "056"),
    Country(u"Belize", "BZ", "BLZ", "084"),
    Country(u"Benin", "BJ", "BEN", "204"),
    Country(u"Bermuda", "BM", "BMU", "060"),
    Country(u"Bhutan", "BT", "BTN", "064"),
    Country(u"Bolivia, Plurinational State of", "BO", "BOL", "068"),
    Country(u"Bonaire, Sint Eustatius and Saba", "BQ", "BES", "535"),
    Country(u"Bosnia and Herzegovina", "BA", "BIH", "070"),
    Country(u"Botswana", "BW", "BWA", "072"),
    Country(u"Bouvet Island", "BV", "BVT", "074"),
    Country(u"Brazil", "BR", "BRA", "076"),
    Country(u"British Indian Ocean Territory", "IO", "IOT", "086"),
    Country(u"Brunei Darussalam", "BN", "BRN", "096"),
    Country(u"Bulgaria", "BG", "BGR", "100"),
    Country(u"Burkina Faso", "BF", "BFA", "854"),
    Country(u"Burundi", "BI", "BDI", "108"),
    Country(u"Cambodia", "KH", "KHM", "116"),
    Country(u"Cameroon", "CM", "CMR", "120"),
    Country(u"Canada", "CA", "CAN", "124"),
    Country(u"Cape Verde", "CV", "CPV", "132"),
    Country(u"Cayman Islands", "KY", "CYM", "136"),
    Country(u"Central African Republic", "CF", "CAF", "140"),
    Country(u"Chad", "TD", "TCD", "148"),
    Country(u"Chile", "CL", "CHL", "152"),
    Country(u"China", "CN", "CHN", "156"),
    Country(u"Christmas Island", "CX", "CXR", "162"),
    Country(u"Cocos (Keeling) Islands", "CC", "CCK", "166"),
    Country(u"Colombia", "CO", "COL", "170"),
    Country(u"Comoros", "KM", "COM", "174"),
    Country(u"Congo", "CG", "COG", "178"),
    Country(u"Congo, Democratic Republic of the", "CD", "COD", "180"),
    Country(u"Cook Islands", "CK", "COK", "184"),
    Country(u"Costa Rica", "CR", "CRI", "188"),
    Country(u"Côte d'Ivoire", "CI", "CIV", "384"),
    Country(u"Croatia", "HR", "HRV", "191"),
    Country(u"Cuba", "CU", "CUB", "192"),
    Country(u"Curaçao", "CW", "CUW", "531"),
    Country(u"Cyprus", "CY", "CYP", "196"),
    Country(u"Czech Republic", "CZ", "CZE", "203"),
    Country(u"Denmark", "DK", "DNK", "208"),
    Country(u"Djibouti", "DJ", "DJI", "262"),
    Country(u"Dominica", "DM", "DMA", "212"),
    Country(u"Dominican Republic", "DO", "DOM", "214"),
    Country(u"Ecuador", "EC", "ECU", "218"),
    Country(u"Egypt", "EG", "EGY", "818"),
    Country(u"El Salvador", "SV", "SLV", "222"),
    Country(u"Equatorial Guinea", "GQ", "GNQ", "226"),
    Country(u"Eritrea", "ER", "ERI", "232"),
    Country(u"Estonia", "EE", "EST", "233"),
    Country(u"Ethiopia", "ET", "ETH", "231"),
    Country(u"Falkland Islands (Malvinas)", "FK", "FLK", "238"),
    Country(u"Faroe Islands", "FO", "FRO", "234"),
    Country(u"Fiji", "FJ", "FJI", "242"),
    Country(u"Finland", "FI", "FIN", "246"),
    Country(u"France", "FR", "FRA", "250"),
    Country(u"French Guiana", "GF", "GUF", "254"),
    Country(u"French Polynesia", "PF", "PYF", "258"),
    Country(u"French Southern Territories", "TF", "ATF", "260"),
    Country(u"Gabon", "GA", "GAB", "266"),
    Country(u"Gambia", "GM", "GMB", "270"),
    Country(u"Georgia", "GE", "GEO", "268"),
    Country(u"Germany", "DE", "DEU", "276"),
    Country(u"Ghana", "GH", "GHA", "288"),
    Country(u"Gibraltar", "GI", "GIB", "292"),
    Country(u"Greece", "GR", "GRC", "300"),
    Country(u"Greenland", "GL", "GRL", "304"),
    Country(u"Grenada", "GD", "GRD", "308"),
    Country(u"Guadeloupe", "GP", "GLP", "312"),
    Country(u"Guam", "GU", "GUM", "316"),
    Country(u"Guatemala", "GT", "GTM", "320"),
    Country(u"Guernsey", "GG", "GGY", "831"),
    Country(u"Guinea", "GN", "GIN", "324"),
    Country(u"Guinea-Bissau", "GW", "GNB", "624"),
    Country(u"Guyana", "GY", "GUY", "328"),
    Country(u"Haiti", "HT", "HTI", "332"),
    Country(u"Heard Island and McDonald Islands", "HM", "HMD", "334"),
    Country(u"Holy See (Vatican City State)", "VA", "VAT", "336"),
    Country(u"Honduras", "HN", "HND", "340"),
    Country(u"Hong Kong", "HK", "HKG", "344"),
    Country(u"Hungary", "HU", "HUN", "348"),
    Country(u"Iceland", "IS", "ISL", "352"),
    Country(u"India", "IN", "IND", "356"),
    Country(u"Indonesia", "ID", "IDN", "360"),
    Country(u"Iran, Islamic Republic of", "IR", "IRN", "364"),
    Country(u"Iraq", "IQ", "IRQ", "368"),
    Country(u"Ireland", "IE", "IRL", "372"),
    Country(u"Isle of Man", "IM", "IMN", "833"),
    Country(u"Israel", "IL", "ISR", "376"),
    Country(u"Italy", "IT", "ITA", "380"),
    Country(u"Jamaica", "JM", "JAM", "388"),
    Country(u"Japan", "JP", "JPN", "392"),
    Country(u"Jersey", "JE", "JEY", "832"),
    Country(u"Jordan", "JO", "JOR", "400"),
    Country(u"Kazakhstan", "KZ", "KAZ", "398"),
    Country(u"Kenya", "KE", "KEN", "404"),
    Country(u"Kiribati", "KI", "KIR", "296"),
    Country(u"Korea, Democratic People's Republic of", "KP", "PRK", "408"),
    Country(u"Korea, Republic of", "KR", "KOR", "410"),
    Country(u"Kuwait", "KW", "KWT", "414"),
    Country(u"Kyrgyzstan", "KG", "KGZ", "417"),
    Country(u"Lao People's Democratic Republic", "LA", "LAO", "418"),
    Country(u"Latvia", "LV", "LVA", "428"),
    Country(u"Lebanon", "LB", "LBN", "422"),
    Country(u"Lesotho", "LS", "LSO", "426"),
    Country(u"Liberia", "LR", "LBR", "430"),
    Country(u"Libya", "LY", "LBY", "434"),
    Country(u"Liechtenstein", "LI", "LIE", "438"),
    Country(u"Lithuania", "LT", "LTU", "440"),
    Country(u"Luxembourg", "LU", "LUX", "442"),
    Country(u"Macao", "MO", "MAC", "446"),
    Country(u"Macedonia, the former Yugoslav Republic of", "MK", "MKD", "807"),
    Country(u"Madagascar", "MG", "MDG", "450"),
    Country(u"Malawi", "MW", "MWI", "454"),
    Country(u"Malaysia", "MY", "MYS", "458"),
    Country(u"Maldives", "MV", "MDV", "462"),
    Country(u"Mali", "ML", "MLI", "466"),
    Country(u"Malta", "MT", "MLT", "470"),
    Country(u"Marshall Islands", "MH", "MHL", "584"),
    Country(u"Martinique", "MQ", "MTQ", "474"),
    Country(u"Mauritania", "MR", "MRT", "478"),
    Country(u"Mauritius", "MU", "MUS", "480"),
    Country(u"Mayotte", "YT", "MYT", "175"),
    Country(u"Mexico", "MX", "MEX", "484"),
    Country(u"Micronesia, Federated States of", "FM", "FSM", "583"),
    Country(u"Moldova, Republic of", "MD", "MDA", "498"),
    Country(u"Monaco", "MC", "MCO", "492"),
    Country(u"Mongolia", "MN", "MNG", "496"),
    Country(u"Montenegro", "ME", "MNE", "499"),
    Country(u"Montserrat", "MS", "MSR", "500"),
    Country(u"Morocco", "MA", "MAR", "504"),
    Country(u"Mozambique", "MZ", "MOZ", "508"),
    Country(u"Myanmar", "MM", "MMR", "104"),
    Country(u"Namibia", "NA", "NAM", "516"),
    Country(u"Nauru", "NR", "NRU", "520"),
    Country(u"Nepal", "NP", "NPL", "524"),
    Country(u"Netherlands", "NL", "NLD", "528"),
    Country(u"New Caledonia", "NC", "NCL", "540"),
    Country(u"New Zealand", "NZ", "NZL", "554"),
    Country(u"Nicaragua", "NI", "NIC", "558"),
    Country(u"Niger", "NE", "NER", "562"),
    Country(u"Nigeria", "NG", "NGA", "566"),
    Country(u"Niue", "NU", "NIU", "570"),
    Country(u"Norfolk Island", "NF", "NFK", "574"),
    Country(u"Northern Mariana Islands", "MP", "MNP", "580"),
    Country(u"Norway", "NO", "NOR", "578"),
    Country(u"Oman", "OM", "OMN", "512"),
    Country(u"Pakistan", "PK", "PAK", "586"),
    Country(u"Palau", "PW", "PLW", "585"),
    Country(u"Palestine, State of", "PS", "PSE", "275"),
    Country(u"Panama", "PA", "PAN", "591"),
    Country(u"Papua New Guinea", "PG", "PNG", "598"),
    Country(u"Paraguay", "PY", "PRY", "600"),
    Country(u"Peru", "PE", "PER", "604"),
    Country(u"Philippines", "PH", "PHL", "608"),
    Country(u"Pitcairn", "PN", "PCN", "612"),
    Country(u"Poland", "PL", "POL", "616"),
    Country(u"Portugal", "PT", "PRT", "620"),
    Country(u"Puerto Rico", "PR", "PRI", "630"),
    Country(u"Qatar", "QA", "QAT", "634"),
    Country(u"Réunion", "RE", "REU", "638"),
    Country(u"Romania", "RO", "ROU", "642"),
    Country(u"Russian Federation", "RU", "RUS", "643"),
    Country(u"Rwanda", "RW", "RWA", "646"),
    Country(u"Saint Barthélemy", "BL", "BLM", "652"),
    Country(u"Saint Helena, Ascension and Tristan da Cunha",
            "SH", "SHN", "654"),
    Country(u"Saint Kitts and Nevis", "KN", "KNA", "659"),
    Country(u"Saint Lucia", "LC", "LCA", "662"),
    Country(u"Saint Martin (French part)", "MF", "MAF", "663"),
    Country(u"Saint Pierre and Miquelon", "PM", "SPM", "666"),
    Country(u"Saint Vincent and the Grenadines", "VC", "VCT", "670"),
    Country(u"Samoa", "WS", "WSM", "882"),
    Country(u"San Marino", "SM", "SMR", "674"),
    Country(u"Sao Tome and Principe", "ST", "STP", "678"),
    Country(u"Saudi Arabia", "SA", "SAU", "682"),
    Country(u"Senegal", "SN", "SEN", "686"),
    Country(u"Serbia", "RS", "SRB", "688"),
    Country(u"Seychelles", "SC", "SYC", "690"),
    Country(u"Sierra Leone", "SL", "SLE", "694"),
    Country(u"Singapore", "SG", "SGP", "702"),
    Country(u"Sint Maarten (Dutch part)", "SX", "SXM", "534"),
    Country(u"Slovakia", "SK", "SVK", "703"),
    Country(u"Slovenia", "SI", "SVN", "705"),
    Country(u"Solomon Islands", "SB", "SLB", "090"),
    Country(u"Somalia", "SO", "SOM", "706"),
    Country(u"South Africa", "ZA", "ZAF", "710"),
    Country(u"South Georgia and the South Sandwich Islands",
            "GS", "SGS", "239"),
    Country(u"South Sudan", "SS", "SSD", "728"),
    Country(u"Spain", "ES", "ESP", "724"),
    Country(u"Sri Lanka", "LK", "LKA", "144"),
    Country(u"Sudan", "SD", "SDN", "729"),
    Country(u"Suriname", "SR", "SUR", "740"),
    Country(u"Svalbard and Jan Mayen", "SJ", "SJM", "744"),
    Country(u"Swaziland", "SZ", "SWZ", "748"),
    Country(u"Sweden", "SE", "SWE", "752"),
    Country(u"Switzerland", "CH", "CHE", "756"),
    Country(u"Syria", "SY", "SYR", "760"),
    Country(u"Taiwan, Province of China", "TW", "TWN", "158"),
    Country(u"Tajikistan", "TJ", "TJK", "762"),
    Country(u"Tanzania, United Republic of", "TZ", "TZA", "834"),
    Country(u"Thailand", "TH", "THA", "764"),
    Country(u"Timor-Leste", "TL", "TLS", "626"),
    Country(u"Togo", "TG", "TGO", "768"),
    Country(u"Tokelau", "TK", "TKL", "772"),
    Country(u"Tonga", "TO", "TON", "776"),
    Country(u"Trinidad and Tobago", "TT", "TTO", "780"),
    Country(u"Tunisia", "TN", "TUN", "788"),
    Country(u"Turkey", "TR", "TUR", "792"),
    Country(u"Turkmenistan", "TM", "TKM", "795"),
    Country(u"Turks and Caicos Islands", "TC", "TCA", "796"),
    Country(u"Tuvalu", "TV", "TUV", "798"),
    Country(u"Uganda", "UG", "UGA", "800"),
    Country(u"Ukraine", "UA", "UKR", "804"),
    Country(u"United Arab Emirates", "AE", "ARE", "784"),
    Country(u"United Kingdom", "GB", "GBR", "826"),
    Country(u"United States", "US", "USA", "840"),
    Country(u"United States Minor Outlying Islands", "UM", "UMI", "581"),
    Country(u"Uruguay", "UY", "URY", "858"),
    Country(u"Uzbekistan", "UZ", "UZB", "860"),
    Country(u"Vanuatu", "VU", "VUT", "548"),
    Country(u"Venezuela, Bolivarian Republic of", "VE", "VEN", "862"),
    Country(u"Vietnam", "VN", "VNM", "704"),
    Country(u"Virgin Islands, British", "VG", "VGB", "092"),
    Country(u"Virgin Islands, U.S.", "VI", "VIR", "850"),
    Country(u"Wallis and Futuna", "WF", "WLF", "876"),
    Country(u"Western Sahara", "EH", "ESH", "732"),
    Country(u"Yemen", "YE", "YEM", "887"),
    Country(u"Zambia", "ZM", "ZMB", "894"),
    Country(u"Zimbabwe", "ZW", "ZWE", "716")]

_aliases = {
    u"Ivory Coast": u"Côte d'Ivoire",
    u"Cote D'Ivoire": u"Côte d'Ivoire",
    u"Federated States of Micronesia": u"Micronesia, Federated States of",
    u"British Virgin Islands": u"Virgin Islands, British",
    u"Macau": u"Macao",
    u"Saint Helena": u"Saint Helena, Ascension and Tristan da Cunha",
    u"Aland Islands": u"Åland Islands",
    u"Palestinian Territory": u"Palestine, State of",
    u"Occupied Palestinian Territory": u"Palestine, State of",
    u"United States Virgin Islands": u"Virgin Islands, U.S.",
    u"Vietnam": u"Viet Nam",
    u"Reunion": u"Réunion",
    u"Macedonia": u"Macedonia, The Former Yugoslav Republic of",
    u"Korea, Republic of (South Korea)": u"Korea, Republic of",
    u"South Korea": u"Korea, Republic of",
    u"Republic of Congo": u"Congo, Democratic Republic of the",
    u"Vatican City": u"Holy See (Vatican City State)",
    u"Taiwan": u"Taiwan, Province of China",
    u"Bolivia": u"Bolivia, Plurinational State of",
    u"Venezuela": u"Venezuela, Bolivarian Republic of",
}

def _build_index(idx):
    return dict((r[idx].upper(), r) for r in _records)


_by_alpha2 = _build_index(1)
_by_alpha3 = _build_index(2)
_by_numeric = _build_index(3)
_by_name = _build_index(0)
_by_alias = dict((a.upper(), c) for (a, c) in _aliases.items())


class _CountryLookup(object):
    def __init__(self, approx=False):
        self.approx = approx


    def __getitem__(self, key):
        if isinstance(key, Integral):
            return _by_numeric["%03d" % key]

        k = key.upper()
        if k=='UAE':
            return _by_name[u"UNITED ARAB EMIRATES"]
        elif len(k) == 2:
            return _by_alpha2[k]
        elif len(k) == 3 and re.match(r"[0-9]{3}", k):
            return _by_numeric[k]
        elif len(k) == 3:
            return _by_alpha3[k]
        else:
            if not self.approx:
                return _by_name[k]
            else:
                try:
                    if k in _by_name:
                        return _by_name[k]
                    else:
                        canonical = _by_alias[k]
                        return _by_name[canonical.upper()]
                except:
                    raise ValueError('could not retrieve Country record for %s' % key.encode('utf-8'))

    get = __getitem__

    def __iter__(self):
        return iter(_records)


countries = _CountryLookup()
approx_countries = _CountryLookup(approx=True)
