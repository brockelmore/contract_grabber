# What?

Etherscan sucks for exploring multi-file verified contracts. This downloads the source code so you can open in your desired editor.

# Usage

```
python ./grabber.py $SOME_NAME $SOME_ADDRESS $ETHERSCAN_BASED_EXPLORER_APIKEY $CHAIN_NAME $FOUNDRY_COMPATIBLE
```

Pass in a name to call the directory. Pass in an address that is verified on an etherscan based explorer and is *multifile* (doesn't work with single file/flattened contracts). Pass in your api key corresponding to the specified chain. Optionally pass in a chain name. If a chain was passed, you can also pass in a boolean `True` at the end. This will make the directory compatible with Foundry by adding the necessary config.

By default the following chains are supported:
```
chains = {
  "arbitrum": "api.arbiscan.io",
  "optimism": "api-optimistic.etherscan.io",
  "binance": "api.bscscan.com",
  "avalanche": "api.snowtrace.io",
  "moonbeam": "api-moonbeam.moonscan.io",
  "ethereum": "api.etherscan.io"
}
```

If you dont pass in a chain name, ethereum is used.

Writes to a directory in `/tmp`. No idea if this works on windows, probably not?

# Example

Get Uniswap V3 router, and make it foundry compatible so that you can compile it immediately with forge.

```
python ./grabber.py UniV3Router 0xE592427A0AEce92De3Edee1F18E0157C05861564 BADMAD1111111111111111111111111111 ethereum True
```

