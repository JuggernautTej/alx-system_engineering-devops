#!/usr/bin/env bash
# Stop me!!

script_id=$(pgrep -fo 4-to_infinity_and_beyond)
kill "$script_id"
