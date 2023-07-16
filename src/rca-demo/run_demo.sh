#!/bin/bash

poetry run spark-submit --packages graphframes:graphframes:0.8.2-spark3.2-s_2.12 ./graphframes_demo.py
