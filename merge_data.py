import os
import sys
import glob
import matplotlib.pyplot as plt
import pickle
import pandas as pd
import numpy as np
import requests
import subprocess
import re
import time
import datetime
import csv
from tqdm import tqdm
from collections import Counter

for b in ['0']:
  files = [
    './data/for_Ilgar_research_2024-Sep_building-0-set-buildingip-ip-isTCP-dns-dnscname-sni-hour-bytes-flows-ports-dns6-17.p', 
    './data/for_Ilgar_research_2024-Sep_building-1-set-buildingip-ip-isTCP-dns-dnscname-sni-hour-bytes-flows-ports-dns6-17.p',
    './data/for_Ilgar_research_2024-Sep_building-2-set-buildingip-ip-isTCP-dns-dnscname-sni-hour-bytes-flows-ports-dns6-17.p', 
    './data/for_Ilgar_research_2024-Sep_building-3-set-buildingip-ip-isTCP-dns-dnscname-sni-hour-bytes-flows-ports-dns6-17.p'
  ]
  print(len(files))

  columns = ['building_ip', 'ip', 'isTCP', 'other_port', 'dns_a', 'dns_name', 'dns_name_orig',
        'sni', 'in_bytes', 'out_bytes', 'nflows', 'duration',
        'DNS6_flows', 'DNS6_bytes', 'DNS17_flows', 'DNS17_bytes',
        'unit_port', 'n_port80', 'n_port443', 'n_no_out', 'hour']
  dfs = []
  for f in files:
      print(f)
      df = pickle.load(open(f, 'rb'))[columns]
      for c in columns:
          if c in ['isTCP']: continue
          elif c in ['other_port', 'unit_port', 'nflows', 'n_port443', 'n_port80', 'n_no_out', 'DNS6_flows', 'DNS17_flows']:
              df[c] = df[c].astype('Int32')
          elif c in ['in_bytes', 'out_bytes', 'DNS6_bytes', 'DNS17_bytes', 'in_packets', 'out_packets']:
              df[c] = df[c].astype('Int64')
          elif c in ['duration']:
              df[c] = df[c].astype('float64')
          else:
              df[c] = df[c].astype('string')
      dfs.append(df)

  df = pd.concat(dfs, ignore_index=True)
  filepath = f'./data/2024-09_building_buildingip-ip-isTCP-dns-dnscname-sni-hour-bytes-flows-ports.p'
  pickle.dump(df, open(filepath, 'wb'))