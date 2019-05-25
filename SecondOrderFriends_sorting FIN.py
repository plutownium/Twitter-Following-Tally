import tweepy
import operator
import time

# 1. access the data in the text files.
# 2. create a histogram from the information.
# 3. convert the SOF IDs to their twitter handles ("screen names").

# 4. display the top 20? top 100? results.
# bonus: show /who/ among my friends is following those top20 people.

CONSUMER_KEY = "jwBq9KApTEU3oghyvgAuAiF6p"
CONSUMER_SECRET = "9BuSjo0h0gOKFEDCPHlfNpJuAH5NoWNnztQJwCemNWtpyLnL52"

my_screen_name = "rolypolyistaken"
my_id = 331107386


def oauth_login(consumer_key, consumer_secret):
    """Authenticate with twitter using OAuth"""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth_url = auth.get_authorization_url()

    verify_code = raw_input("Authenticate at %s and then enter you verification code here > " % auth_url)
    auth.get_access_token(verify_code)

    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

api = oauth_login(CONSUMER_KEY, CONSUMER_SECRET)  # returns an authenticated API object


def splitup_TEST(test_list, which_test):
    if len(test_list) is 11:
        # print "The split worked."
        pass
    else:
        print len(test_list)
        for bit in range(0, (len(test_list))):
            print test_list[bit]
        print "failed on test number: %s" % str(which_test)
        raise Exception("Something went wrong")


def data_to_friends_list(raw):
    splits = raw.split("\n\n")
    print splits[0]


def show_txtfile_contents(readout):
    split = readout.split("\n\n")
    for ent in range(0, 10):
        print split[ent]
    print "^^ split"


def keywithmaxval(d):
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value
        *note: copied from stackoverflow"""
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

histogram_dict = {}

target = r"^\d+"


for textnum in range(0, 46):  # change 3 to 46
    filename = "iteration_" + str(textnum) + ".txt"
    f = open(filename, "r")
    data = f.read()
    f.close()

    entry_as_a_list = []

    # NOTE: It comes out to length 11 BECAUSE the file ends with \n\n ... ?
    splitup = data.split("\n\n")
    # Yep, there's a 10th index on all of them that is simply nothing.

    splitup_TEST(splitup, which_test=textnum)

    # there is a set of 10 IDs in each txt file: therefore, (0,10).
    for i in range(0, 10):
        from_here_l = splitup[i].index(": [") + 4

        to_here_l = splitup[i].index("]")
        # creates a list of twitter IDs as strings. fine for now. 10-2000 len.
        too_big = splitup[i][from_here_l:to_here_l].split("', '")
        # getting rid of that annoying " on either side of the last entry.
        # e.g. "'44570946" becomes '44570946' ... somehow ...
        too_big[-1] = too_big[-1][0:-1]

        # except ValueError:
        #     print "You tried to get .index() but thats not possible..."
        #     print "HEY ---> " + str(splitup[i]) + " <--"
        #     print "theres the problem"

        # print "Length of 'too big' is %s" % str(len(too_big))
        for some_ID in range(0, len(too_big)):
            # "If the user ID is already in the dictionary..."
            if too_big[some_ID] in histogram_dict:
                # "...Then add one to its value."
                histogram_dict[too_big[some_ID]] += 1
            # But if the user ID is not already in the dictionary..."
            else:
                # "Then add it to the dictionary for the first time."
                histogram_dict[too_big[some_ID]] = 1

sort_this = {}

for key, value in histogram_dict.items():
    if value > 20:
        sort_this[key] = value

sorted_x = sorted(sort_this.items(), key=operator.itemgetter(1))

my_friends = [66135293, 157675926, 74156661, 787309883343278082L, 50778314, 29764927, 33152005, 1180887055, 177313098, 471672239, 277530193, 42755923, 14207787, 1018209403, 144457402, 330944917, 47747075, 44204171, 68371442, 2701901466L, 2288820930L, 116931426, 313038011, 745273, 3324785167L, 328796286, 76172215, 2854925629L, 1568584344, 22685969, 4792596329L, 408992860, 48054508, 457639679, 28642380, 344494009, 62786088, 512016451, 2222603539L, 358545917, 68951871, 415164542, 8287602, 612823531, 26443701, 20565284, 519848072, 8381682, 131868148, 352673744, 36163202, 719919986060316672L, 59594239, 2610279650L, 2896929926L, 2326507813L, 59399268, 21639792, 190946220, 216148558, 392918817, 250228038, 55693805, 290843574, 232589722, 276822771, 381289719, 2415428186L, 272950920, 457193331, 566395768, 216356776, 480858874, 62821817, 33432257, 1951639321, 22317367, 566910970, 21349639, 204962218, 271282514, 1918514893, 3272620926L, 87576856, 1327571275, 19697415, 30936385, 477041987, 4177697337L, 960930702, 63873759, 271400204, 31489182, 26296261, 77293452, 28227216, 4145624369L, 45975518, 60145605, 2287037810L, 410223318, 2426699984L, 2975472756L, 4717284883L, 1067274240, 2206131, 183749519, 26985102, 18199911, 20570290, 38747193, 2482802780L, 3764301, 116994659, 58562612, 17919972, 37710752, 19725644, 44196397, 185720490, 2853461537L, 139731910, 58133585, 58408094, 282749926, 219438797, 21404171, 37518096, 57301115, 34097500, 80599812, 33491157, 25368602, 414014781, 124251502, 1292253570, 197303950, 1959466267, 24926413, 30797865, 327715460, 418569734, 17825445, 29272446, 606770013, 22785864, 297882651, 2757672041L, 44366597, 20312278, 118599144, 73800720, 628830361, 181212732, 351062478, 22785500, 19103481, 138133234, 108908299, 821119939, 78961363, 504890998, 262817465, 2231207504L, 738250458, 83407812, 23032965, 235754131, 121261716, 3121021459L, 1461204871, 98104345, 23609808, 198086608, 49662449, 2893055443L, 26470215, 31087112, 2980264914L, 28211610, 727193022, 27749259, 52368140, 36746176, 196277177, 50130045, 129323698, 252261660, 7354662, 112427694, 596796769, 393630242, 73020075, 83338113, 1334871110, 38638456, 1323763664, 41859177, 58500819, 91240835, 383047274, 339504540, 1152748446, 86695861, 92324608, 256542586, 69367470, 76791634, 23027648, 389183217, 41162914, 563337136, 240788625, 2342249876L, 1873573326, 160820801, 2166969546L, 19531303, 161511739, 1956134479, 19911874, 2299165788L, 148877599, 44441179, 1689105080, 256569627, 66809538, 573726684, 513288870, 116255906, 45788610, 75853209, 2224115754L, 28987332, 60708374, 567325499, 137417475, 24546836, 269891207, 22143532, 309214184, 281129530, 116380523, 176503155, 19679173, 132271124, 17482855, 608615938, 42596860, 75527068, 1883882869, 2983413820L, 161424825, 213171360, 745057788, 95835790, 143466469, 51813176, 587794023, 251304535, 78912272, 251421434, 399888877, 126089211, 25168459, 18645813, 41784974, 200810888, 113259973, 43833516, 125077669, 122396746, 536399402, 32351549, 100199653, 48272619, 15372840, 34775386, 137573705, 16582578, 62614140, 107483148, 433697321, 2830149035L, 1390550744, 20913964, 156735736, 360869459, 1103170992, 20731695, 810484280, 102687765, 18931600, 189328634, 16151999, 18545862, 47305686, 19011738, 51086473, 19528178, 18988304, 15147748, 14098533, 30513101, 26131703, 23491333, 45777849, 17632756, 69964783, 109973880, 31369541, 69542069, 20940081, 47359148, 21568477, 22838300, 136674424, 18750157, 86131902, 39597481, 159708091, 22147137, 18914814, 37093178, 31093615, 238730481, 17174309, 19520983, 65173646, 23976386, 40101400, 18825961, 300982287, 54709777, 20825047, 144866558, 26452026, 21174888, 25381864, 39603151, 24694525, 134234000, 24693705, 86572842, 21323307, 441069688, 34914032, 17019152, 21787625, 16224717, 18625669, 34464376, 155705264, 22412376, 294636267, 102632870, 18624044, 31398437, 65388780, 16185414, 29990808, 208716386, 28511855, 29512637, 22014324, 31539087, 20846502, 432093, 130151627, 35557242, 57120928, 32185593, 19526972, 65429150, 29381205, 44850810, 26482350, 28823640, 38132559, 32401095, 33623812, 15574534, 160888828, 22541249, 38815826, 22908875, 22649951, 20861443, 21741833, 220387255, 22651969, 59545254, 22613936, 50027817, 24343698, 21001379, 264689298, 28358543, 37807048, 46423061, 19721852, 43859554, 23335282, 46279037, 16303106, 65421315, 19766567, 73365668, 37923035, 8304412, 25347795, 62733022, 116699912, 27476141, 72564538, 19911051, 28604158, 30439207, 15614972, 21086501, 21858647, 37508790, 23122371, 25422041, 37085034, 75049075, 38431215, 20867339, 20541545, 28311839, 27536599, 23016199, 78097360, 23201886, 27310101, 18778913, 14473290, 44108196, 19388771, 28382412, 20696985, 18776605, 22472158, 22611082, 20279934, 21856755, 82199295, 61911466, 57553172, 32470513, 21860331, 37936839, 97174186, 44908881, 31983710, 20692016, 25003557, 19120191, 21905547, 60644641, 65184429, 35727881, 14220688, 25810048, 25524289, 158143919]
# NOTE: NEED TO <REMOVE> THE ID'S OF PEOPLE I CURRENTLY FOLLOW.
sorted_x2 = []
for pair in sorted_x:
    # because its a string initially
    as_number = int(pair[0])
    if as_number not in my_friends:
        sorted_x2.append(pair)

# for thing in sorted_x2:
#     print thing

as_names = []

jibber = 0

# Now need to turn Twitter IDs back into usernames. There's a bunch.
for pair in sorted_x2:
    try:
        user_obj = api.get_user(id=pair[0])
        user_screen_name = user_obj.screen_name
        user_follower_count = user_obj.followers_count
        new_tuple = (user_screen_name, user_follower_count, pair[1])
        as_names.append(new_tuple)
    except:
        print "Suspended or something: %s" % str(pair[0])
        as_names.append("Suspended ")
    print jibber
    jibber += 1

for pair in as_names:
    print pair

print "done"
