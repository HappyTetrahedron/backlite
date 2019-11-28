# backlite

Remotely change backlight of some device with this simple server application

Actual backlight adjustment is done in a bash script which you provide yourself, this app just interfaces that script
and a HTTP endpoint.

The script should accept a number between 0 and 255 as the intensity to which the backlight is set.

backlite optionally uses `sudo` to execute the script, but you should configure your system so that the script
can be executed without password when `sudo` is used.

This software is guaranteed not safe to use!
