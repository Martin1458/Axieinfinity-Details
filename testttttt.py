import requests
tableAxieTransactions = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"models": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
    }
  ]
}

#print(str(x))

print(tableAxieTransactions)
print(tableAxieTransactions['cars'])
print(tableAxieTransactions['cars'][0])
print(tableAxieTransactions['cars'][0]['models'])


for car in tableAxieTransactions['cars'][0]['models']:
    print(car['model'])

exit()
jsonData = {
    "operation": "GetAxieDetail",
    "variables": {
        "axieId": 2371
    },
    "query": "query GetAxieDetail($axieId: ID!) {\n  axie(axieId: $axieId) {\n    ...AxieDetail\n    __typename\n  }\n}\n\nfragment AxieDetail on Axie {\n  id\n  image\n  class\n  chain\n  name\n  genes\n  owner\n  birthDate\n  bodyShape\n  class\n  sireId\n  sireClass\n  matronId\n  matronClass\n  stage\n  title\n  breedCount\n  level\n  figure {\n    atlas\n    model\n    image\n    __typename\n  }\n  parts {\n    ...AxiePart\n    __typename\n  }\n  stats {\n    ...AxieStats\n    __typename\n  }\n  auction {\n    ...AxieAuction\n    __typename\n  }\n  ownerProfile {\n    name\n    __typename\n  }\n  battleInfo {\n    ...AxieBattleInfo\n    __typename\n  }\n  children {\n    id\n    name\n    class\n    image\n    title\n    stage\n    __typename\n  }\n  __typename\n}\n\nfragment AxieBattleInfo on AxieBattleInfo {\n  banned\n  banUntil\n  level\n  __typename\n}\n\nfragment AxiePart on AxiePart {\n  id\n  name\n  class\n  type\n  specialGenes\n  stage\n  abilities {\n    ...AxieCardAbility\n    __typename\n  }\n  __typename\n}\n\nfragment AxieCardAbility on AxieCardAbility {\n  id\n  name\n  attack\n  defense\n  energy\n  description\n  backgroundUrl\n  effectIconUrl\n  __typename\n}\n\nfragment AxieStats on AxieStats {\n  hp\n  speed\n  skill\n  morale\n  __typename\n}\n\nfragment AxieAuction on Auction {\n  startingPrice\n  endingPrice\n  startingTimestamp\n  endingTimestamp\n  duration\n  timeLeft\n  currentPrice\n  currentPriceUSD\n  suggestedPrice\n  seller\n  listingIndex\n  state\n  __typename\n}\n"
}
url = 'https://graphql-gateway.axieinfinity.com/graphql'

ableOfA = requests.post(url, json=jsonData)
print(ableOfA.json()['data']['axie']['parts'][2]['abilities'][0])
#print(ableOfA.json()['data']['axie']['parts'])  # ```
for i in range(len(ableOfA.json()['data']['axie']['parts'])):
    try:
        if "id" in ableOfA.json()['data']['axie']['parts'][i]['abilities'][0]:
            print(str(ableOfA.json()['data']['axie']['parts'][i]['id']), ':', str(ableOfA.json()['data']['axie']['parts'][i]['abilities'][0]['id']))
    except:
        print(ableOfA.json()['data']['axie']['parts'][i]['id'])
