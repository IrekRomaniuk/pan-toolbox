#!/usr/bin/env python

import requests
import argparse
requests.packages.urllib3.disable_warnings()


'''
    This is a quick script to grab a backup a firewall with a known API key.  Next iteration will pull a username and
    password as needed to gen the API key on it's own for use.  This was a quick script though used out of a private
    server with cron to pull these.

    - Tighe Schlottog workape<at>gmail<dot>com
'''


def parse_args():
    parser = argparse.ArgumentParser(description='Quick Backup of onboard firewall configuration')
    parser.add_argument('-fw', type=str, help='IP Address of Firewall', required=True)
    parser.add_argument('-k', '--api_key', type=str, help='API Key with access to Firewall', required=True)
    parser.add_argument('-out', type=str, help='Output file where the configuration should be written', required=True)
    args = parser.parse_args()
    return parser, args


def pull_backup(fw, api_key, outfile):
    config_out = open(outfile, 'w')
    backup_headers = {'type': 'export', 'key': api_key, 'category': 'configuration'}
    backup_req = requests.get('https://%s/api' % fw, params=backup_headers, verify=False)
    config_out.write(backup_req.content)
    config_out.close()


def control():
    backup_parser, backup_args = parse_args()
    pull_backup(backup_args.fw, backup_args.api_key, backup_args.out)


if __name__ == '__main__':
    control()