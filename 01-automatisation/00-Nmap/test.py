#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exemple de script pour scanner les ports les plus courants sur un hôte
"""

import nmap3
import json

nmap = nmap3.Nmap()
result = nmap.nmap_subnet_scan("192.168.1.1/27")

print(json.dumps(result, indent=2))


