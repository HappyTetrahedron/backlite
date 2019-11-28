#!/usr/bin/env python

from flask import Flask
import yaml
import subprocess
from optparse import OptionParser


app = Flask(__name__)

config = None


@app.route("/backlight/<intensity>", methods = ['POST'])
def handle_action(intensity):
    numeric_intensity = 0
    try:
        numeric_intensity = int(intensity)
    except ValueError:
        return "Invalid intensity"
    if numeric_intensity < 0 or numeric_intensity > 255:
        return "Invalid intensity"

    command = "{} {}".format(config['backlight-action'], numeric_intensity)
    if config['use-sudo']:
        command = "sudo {}".format(command)

    process = subprocess.run(
        command,
        shell=True
    )
    status = process.returncode

    return "Status: {}".format(status)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-c', '--config', dest='config', default='config.yml', type='string',
                      help="Path of configuration file")
    (opts, args) = parser.parse_args()
    with open(opts.config, 'r') as configfile:
        config = yaml.load(configfile)
    app.run(config['host'], config['port'])
