import requests

url = 'https://graphql-gateway.axieinfinity.com/graphql'
params = {
        "axieId": 1027,
        "from": 0,
        "size": 10
}
jsonData = """query GetAxieTransferHistory($axieId: ID!, $from: Int!, $size: Int!) {
                  axie(axieId: $axieId) {
                    id
                    transferHistory(from: $from, size: $size) {
                      ...TransferRecords
                      __typename
                    }
                    ethereumTransferHistory(from: $from, size: $size) {
                     ...TransferRecords
                     __typename
                    }
                    __typename
                  }
                }
                fragment TransferRecords on TransferRecords {
                  total
                  results {
                    from
                    to
                    timestamp
                    txHash
                    withPrice
                    __typename
                  }
                  __typename
                }"""
tableAxieTransactions = requests.post(url, json={"query": jsonData, "variables": params})



l02 = [str(1044)]  # id
l03 = [str(tableAxieTransactions.json()['data']['axie']['ethereumTransferHistory']['results'][0]['withPrice'])]  # howMuch
l04 = [str(tableAxieTransactions.json()['data']['axie']['ethereumTransferHistory']['results'][0]['timestamp'])]  # timeStamp
l05 = [str(tableAxieTransactions.json()['data']['axie']['ethereumTransferHistory']['results'][0]['from'])]  # from
l06 = [str(tableAxieTransactions.json()['data']['axie']['ethereumTransferHistory']['results'][0]['to'])]

print(l02)
print(l03)
print(l04)
print(l05)
print(l06)
