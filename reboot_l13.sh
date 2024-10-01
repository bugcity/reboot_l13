#!/usr/bin/bash

touch /var/log/zte_l13/reboot
uv run python src/reboot_l13.py
