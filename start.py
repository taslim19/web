#!/bin/bash
uvicorn main:fast_app --host 0.0.0.0 --port $PORT
