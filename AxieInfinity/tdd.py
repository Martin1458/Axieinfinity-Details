from notMain import url
from notMain import getDetails

ListOfAxies = [4368946, 2371, 125947, 137473, 6103603, 10581337, 6967276, 32, 3612, 3228, 2593, 4134]
ListOfNames = ['Axie #4368946', 'Neil Peart', 'UNIQUE DANGO 🍡', 'Sweating Buckets', 'Axie #6103603', 'Axie #10581337',
               'Axie #6967276', 'Stega', 'Axie #3612', 'Axie #3228', 'Basse', 'Axie #4134']
i = 0
works = 0

for stuff in ListOfAxies:
    jsonData = {
        "operation": "GetAxieDetail",
        "variables": {
            "axieId": stuff
        },
        "query": "query GetAxieDetail($axieId: ID!) {\n  axie(axieId: $axieId) {\n    ...AxieDetail\n    __typename\n  }\n}\n\nfragment AxieDetail on Axie {\n  id\n  image\n  class\n  chain\n  name\n  genes\n  owner\n  birthDate\n  bodyShape\n  class\n  sireId\n  sireClass\n  matronId\n  matronClass\n  stage\n  title\n  breedCount\n  level\n  figure {\n    atlas\n    model\n    image\n    __typename\n  }\n  parts {\n    ...AxiePart\n    __typename\n  }\n  stats {\n    ...AxieStats\n    __typename\n  }\n  auction {\n    ...AxieAuction\n    __typename\n  }\n  ownerProfile {\n    name\n    __typename\n  }\n  battleInfo {\n    ...AxieBattleInfo\n    __typename\n  }\n  children {\n    id\n    name\n    class\n    image\n    title\n    stage\n    __typename\n  }\n  __typename\n}\n\nfragment AxieBattleInfo on AxieBattleInfo {\n  banned\n  banUntil\n  level\n  __typename\n}\n\nfragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\nfragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\nfragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\nfragment AxieAuction on Auction {\n  startingPrice\n  endingPrice\n  startingTimestamp\n  endingTimestamp\n  duration\n  timeLeft\n  currentPrice\n  currentPriceUSD\n  suggestedPrice\n  seller\n  listingIndex\n  state\n  __typename\n}\n"
    }
    tableAxieTransactions = getDetails(url, jsonData)
    try:
        if str(tableAxieTransactions.json()['data']['axie']['name']) == str(ListOfNames[i]):
            print(f'\033[92mIt works!!!\033[0m')
            works += 1
        else:
            print(f'\033[91mFix it now!!!\033[0m')

    except:
        print(f'\033[91mFix it now!!!\033[0m')

    print('id: ' + str(ListOfAxies[i]))
    print('name: ' + str(ListOfNames[i]))
    print('i: ' + str(i))

    i += 1
if works == len(ListOfAxies):
    print(f'\033[92mNice everything works!!!\033[0m')
else:
    print(f'\033[91mLol u got error\033[0m')

n = {'dateTime': l1, 'name': l2, 'id': l3, 'price': l4, 'level': l5, 'hp': l6, 'skill': l7, 'speed': l8, 'morale': l9, 'breedCount': l10, 'stage': l11, 'title': l12, 'bodyShape': l13, 'birthDate': l14, 'class': l15}