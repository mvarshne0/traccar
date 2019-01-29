#Python script to get the devices data from traccar portal.
# How many devices are online in a group?
# How many devices are offline in a group?
# How many devices are Unknown in a group?

import csv
import requests
import json
import uuid


if __name__ == "__main__":

        
        URL = ''
        userName = ''
        password = ''
        
        headers = {
                'Content-Type': 'application/json',
        }        
        response = requests.get(URL, headers=headers,
                                     auth=(userName, password))
        response = response.json()
        
        groupId = None 
        onlineDevices, offlineDevicesPortal, unknownDevices = [], [], []      
        onlineCount, offlineCount, unknownCount = 0, 0, 0

        for r in response:
            if r["status"] == "online" and r["groupId"] == groupId:
                onlineCount += 1
                onlineDevices.append(r["uniqueId"])
            elif r["status"] == "unknown" and r["groupId"] == groupId:
                unknownCount += 1
                unknownDevices.append(r["uniqueId"])
            elif r["status"] == "offline" and r["groupId"] == groupId:
                offlineCount +=1
                offlineDevicesPortal.append(r["uniqueId"])

        print("Total Online Devices are: {}".format(onlineCount))
        print("Total Unknown Devices are: {}".format(unknownCount))
        print("Total Offline Devices are: {}".format(offlineCount))
        print("Total Devices are: {}".format(onlineCount + unknownCount + offlineCount))

