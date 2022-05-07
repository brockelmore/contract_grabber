import requests as r
import os
import sys
import json
import toml

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
  if len(sys.argv) >= 5:
    chain = chains[sys.argv[4]]
  else:
    chain = default_chain

  init_forge_repo = False
  if len(sys.argv) >= 6:
    init_forge_repo = bool(sys.argv[5])

  api_key = api_key_base + api_key

  url = constructApiUrl(chain, addr, api_key)
  api_resp = getEtherscan(url)
  sources = getMultiSource(api_resp)
  directory = mkdir(name)
  writeContracts(directory, sources)
  print("Wrote contracts to: ", directory)
  if init_forge_repo:
    curr_dir = os.getcwd()
    os.chdir(directory)
    os.system("forge config > foundry.toml")
    with open("./foundry.toml", "r+") as config:
      conf = toml.loads(config.read())
      for d in os.listdir(directory):
        if os.path.isdir(d):
          if d.startswith("src") or d.startswith("contracts"):
            continue
          else:
            conf["default"]["libs"].append(d)
      config.seek(0)
      config.write(toml.dumps(conf))
    os.chdir(curr_dir)


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