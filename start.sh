#!/usr/bin/env bash
poetry run waitress-serve --host 0.0.0.0 --port 5069 app:app