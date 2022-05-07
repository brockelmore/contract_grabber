# What?

Etherscan sucks for exploring multi-file verified contracts. This downloads the source code so you can open in your desired editor.

# Usage

```
python ./grabber.py $SOME_NAME $SOME_ADDRESS $ETHERSCAN_BASED_EXPLORER_APIKEY $CHAIN_NAME
```

Pass in a name to call the directory. Pass in an address that is verified on an etherscan based explorer and is *multifile* (doesn't work with single file/flattened contracts). Pass in your api key corresponding to the specified chain. Optionally pass in a chain name.

By default the following chains are supported:
```
chains = {
  "arbitrum": "api.arbiscan.io",
  "optimism": "api-optimistic.etherscan.io",
  "binance": "api.bscscan.com",
  "avalanche": "api.snowtrace.io",
  "moonbeam": "api-moonbeam.moonscan.io"
}
```

If you dont pass in a chain name, ethereum is used.

Writes to a directory in `/tmp`. No idea if this works on windows, probably not?