#!/usr/bin/env sh

binary_path=$(dirname $0)/
project_path=${binary_path}../
assets_path=${project_path}assets

[ ! -d "${assets_path}" ] && mkdir "${assets_path}"

db_url=http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz

cd "${assets_path}" &&
wget "${db_url}" || curl -O "${db_url}" &&
gunzip $(basename "${db_url}")

