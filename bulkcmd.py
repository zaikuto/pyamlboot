#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from pyamlboot import pyamlboot

if __name__ == "__main__":
    dev = pyamlboot.AmlogicSoC()

    response = dev.bulkCmd(" ".join(sys.argv[1:]))

    print(response.tobytes().decode("utf-8"))
