#!/bin/bash

# Simple DNS lookup tool using dig

echo "Enter hostnames or IP addresses (separated by space):"
read -a HOSTNAMES

echo "Enter DNS record type (e.g., A, AAAA, MX, NS, TXT, etc.):"
read TYPE

echo "Use custom nameserver? (y/n)"
read USE_NS

if [[ "$USE_NS" == "y" ]]; then
    echo "Enter nameserver (e.g., 8.8.8.8):"
    read NAMESERVER
    NS_OPTION="@$NAMESERVER"
else
    NS_OPTION=""
fi

echo "Enable DNSSEC? (y/n)"
read DNSSEC
[[ "$DNSSEC" == "y" ]] && DNSSEC_OPTION="+dnssec" || DNSSEC_OPTION=""

echo "Enable short output? (y/n)"
read SHORT
[[ "$SHORT" == "y" ]] && SHORT_OPTION="+short" || SHORT_OPTION=""

echo "Enable trace? (y/n)"
read TRACE
[[ "$TRACE" == "y" ]] && TRACE_OPTION="+trace" || TRACE_OPTION=""

for HOST in "${HOSTNAMES[@]}"; do
    echo -e "\nQuerying $HOST..."
    dig $NS_OPTION $HOST $TYPE $DNSSEC_OPTION $SHORT_OPTION $TRACE_OPTION
done

