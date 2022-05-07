import requests as r
import os
import sys
import json

api_key_base = "&apikey="
endpoint = "/api?module=contract&action=getsourcecode&address="
default_chain = "api.etherscan.io"

chains = {
  "arbitrum": "api.arbiscan.io",
  "optimism": "api-optimistic.etherscan.io",
  "binance": "api.bscscan.com",
  "avalanche": "api.snowtrace.io",
  "moonbeam": "api-moonbeam.moonscan.io",
  "ethereum": default_chain,
}

def constructApiUrl(chain, addr, api_key):
  return "https://" + chain + endpoint + addr + api_key

def main():
  name = sys.argv[1]
  addr = sys.argv[2]
  api_key = sys.argv[3]
  if len(sys.argv) == 5:
    chain = chains[sys.argv[4]]
  else:
    chain = default_chain

  api_key = api_key_base + api_key

  url = constructApiUrl(chain, addr, api_key)
  api_resp = getEtherscan(url)
  sources = getMultiSource(api_resp)
  directory = mkdir(name)
  writeContracts(directory, sources)
  print("Wrote contracts to: ", directory)

def writeContracts(directory, sources):
  for source in sources.keys():
    dirs = source.split("/")
    for i in range(len(dirs[:-1])):
      subdir = "/".join(dirs[:i+1])
      mksub_dir(directory, subdir)
    with open(directory+"/"+source, "w") as f:
      f.write(sources[source]["content"])

def mkdir(name):
  try:
    os.mkdir("/tmp/"+name)
  except:
    pass
  return "/tmp/"+name

def mksub_dir(directory, name):
  try:
    os.mkdir(directory+"/"+name)
  except:
    pass
  return directory+"/"+name

def getEtherscan(url):
  resp = r.get(url).json()
  return resp

def getMultiSource(resp):
  sources = json.loads(resp['result'][0]["SourceCode"][1:-1])['sources']
  return sources

if __name__ == "__main__":
  main()