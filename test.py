from finance import Finance

token = '2d794c6f46094ceb96bd719c1c26c984'

f = Finance()
print(f.get_crypto_address(api_key=token,crypto_type = "Bitcoin"))
