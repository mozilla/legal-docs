# Privacy Notice for Mozilla Location Services

Last updated February 3, 2021
{: datetime="2021-02-03" }

[Mozilla Location Services](https://location.services.mozilla.com) (MLS) is an
open, crowdsourced geolocation service that can estimate your device’s
location. MLS works on apps, websites, and services that are authorized to use
MLS and that you have given permission to request your device’s location.

In this Privacy Notice, we explain what data Mozilla Location Services collects
and shares, and why. We also adhere to the practices outlined in the Mozilla
[Privacy Policy](https://www.mozilla.org/privacy/) for how we receive, handle
and share information we collect from MLS.

## What Data MLS Collects

Mozilla estimates your location when you choose to share your location with an
application, or website, or service. Here’s the data MLS may receive when a
request is made:

__Location data__: Information about the publicly observable Wi-Fi access
points, cell towers and Bluetooth beacons closest to you. We may also
determine your location from your device’s (e.g., computer, phone, tablet) IP
address.  You can prevent your Wi-Fi access points from being reported to
Mozilla - see how to disable this on the
[Opt-Out page](https://location.services.mozilla.com/optout) on MLS.

__Technical data__: Technical data like the time you made a location request
and an approximation of how close you are to a Wi-Fi access point, cell
tower, or Bluetooth beacon.

You can see a
[complete list](https://ichnaea.readthedocs.io/en/latest/api/geolocate.html)
of the technical data we collect.

__Crash reports__: If MLS crashes, we receive information about what may have
caused the crash. Crash reports include information about MLS at the time of
a crash, which may contain data that identifies you or is otherwise sensitive
to you. This could include your IP address, location information, and the
time of the crash.

We use the information we collect to provide the service to you, and to improve
the service.

## How Your Data is Shared

__Cloud Storage Provider__: We use
[Amazon Web Services](https://aws.amazon.com/privacy/) (AWS) as our cloud
storage provider to store and process MLS data.


__Authorized applications and websites that request your location__: If you (or
a [product or service](https://location.services.mozilla.com/terms) you’re
using) makes a request for your location, Mozilla will share your approximate
location with the product or service.

__Publicly__: We publish data on public cell tower locations on our website for
public use and benefit. We will not publicly share Bluetooth or Wi-Fi location
data, which can be more sensitive. You can
[view the reports](https://location.services.mozilla.com/downloads) on MLS.

## Mozilla Stumbler App

_Note: The Mozilla Stumbler app was decommissioned on February 8, 2021, and is
no longer supported. See the announcement
[Retiring Mozilla Stumbler](https://discourse.mozilla.org/t/retiring-mozilla-stumbler/75206)
for more information._

Mozilla Stumbler (Stumbler) is an open-source Android application that collects
GPS data to improve the
[Mozilla Location Service](https://location.services.mozilla.com).
Stumbler (and authorized applications that use
[the geosubmit API](https://ichnaea.readthedocs.io/en/latest/api/geosubmit2.html))
*automatically* records location data when the app is open and you move around.
In addition to the data MLS collects, Stumbler also receives your device’s GPS
location and additional technical data, like your device’s altitude and speed.

The information is stored locally on your device until an internet connection
is established. The data is then deleted from your device and sent to Mozilla.
If you do not want to report data to Mozilla, you can delete the Android app or
change your Firefox for Android (versions 69 and earlier) preference under
Settings / Privacy / Data Choices.

We aggregate location points sent to Mozilla from users around the world in our
[data map](https://location.services.mozilla.com/map).  Location points are
blurred to promote anonymity.

