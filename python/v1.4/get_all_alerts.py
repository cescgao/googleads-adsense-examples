#!/usr/bin/python
#
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Gets all alerts available for on of the logged in user's accounts.

Tags: metadata.alerts.list
"""

__author__ = 'jalc@google.com (Jose Alcerreca)'

import sys

from apiclient import sample_tools
from oauth2client import client
from adsense_util import get_account_id


def main(argv):
  # Authenticate and construct service.
  service, unused_flags = sample_tools.init(
      argv, 'adsense', 'v1.4', __doc__, __file__, parents=[],
      scope='https://www.googleapis.com/auth/adsense')

  try:
    # Let the user pick account if more than one.
    account_id = get_account_id(service)

    # Retrieve alerts list in pages and display data as we receive it.
    request = service.accounts().alerts().list(accountId=account_id)

    if request is not None:
      result = request.execute()
      if 'items' in result:
        alerts = result['items']
        for alert in alerts:
          print ('Alert id "%s" with severity "%s" and type "%s" was found. '
                 % (alert['id'], alert['severity'], alert['type']))
          # Uncomment to dismiss alert. Note that this cannot be undone.
          # service.alerts().delete(alertId=alert['id']).execute()
      else:
        print 'No alerts found!'
  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')

if __name__ == '__main__':
  main(sys.argv)
