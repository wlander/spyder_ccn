#!/bin/sh
# Автоматическая смена НИМа в TOR
echo -e 'AUTHENTICATE "1982god39"\r\nsignal NEWNYM\r\nQUIT' | nc 127.0.0.1 9051


