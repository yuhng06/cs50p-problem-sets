import sys
import requests

if len(sys.argv) == 1:
    sys.exit('Missing command-line argument')
elif len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit('Command-line argument is not a number')
else:
    sys.exit('Missing command-line argument')

response = requests.get('https://rest.coincap.io/v3/assets/bitcoin?apiKey=76fe88b067d8c1f2092afbe1fbb5b3507c6a3d8c9213333589b348873d3124ba')
data = response.json()

price = float(data['data']['priceUsd'])

print (f"${n*price:,.4f}")
