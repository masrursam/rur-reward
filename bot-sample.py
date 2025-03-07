import aiohttp
import asyncio
import json
import string
import random
from loguru import logger
import platform
import os
import time

i = 1
while i < 10:
  print("✅ test looping", i)
  time.sleep(1)
  i += 1