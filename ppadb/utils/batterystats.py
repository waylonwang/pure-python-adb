# This csv is converted from https://developer.android.com/studio/command-line/dumpsys#battery
raw_batterystats_fields = """
vers,Version,"checkin version, parcel version, start platform version, end platform version"
uid,UID,"uid, package name"
apk,APK,"wakeups, APK, service, start time, starts, launches"
pr,Process,"process, user, system, foreground, starts"
sr,Sensor,"sensor number, time, count"
vib,Vibrator,"time, count"
fg,Foreground,"time, count"
st,State Time,"foreground, active, running"
wl,Wake lock,"wake lock, full time, 'f', full count, partial time, 'p', partial count, window time, 'w', window count"
sy,Sync,"sync, time, count"
jb,Job,"job, time, count"
kwl,Kernel Wake Lock,"kernel wake lock, time, count"
wr,Wakeup Reason,"wakeup reason, time, count"
nt,Network,"mobile bytes RX, mobile bytes TX, Wi-Fi bytes RX, Wi-Fi bytes TX, mobile packets RX, mobile packets TX, Wi-Fi packets RX, Wi-Fi packets TX, mobile active time, mobile active count"
ua,User Activity,"other, button, touch"
bt,Battery,"start count, battery realtime, battery uptime, total realtime, total uptime, start clock time, battery screen off realtime, battery screen off uptime"
dc,Battery Discharge,"low, high, screen on, screen off"
lv,Battery Level,"start level, current level"
wfl,Wi-Fi,"full Wi-Fi lock on time, Wi-Fi scan time, Wi-Fi running time, Wi-Fi scan count, Wi-Fi idle time, Wi-Fi receive time, Wi-Fi transmit time"
gwfl,Global Wi-Fi,"Wi-Fi on time, Wi-Fi running time, Wi-Fi idle time, Wi-Fi receive time, Wi-Fi transmit time, Wi-Fi power (mAh)"
gble,Global Bluetooth,"BT idle time, BT receive time, BT transmit time, BT power (mAh)"
m,Misc,"screen on time, phone on time, full wakelock time total, partial wakelock time total, mobile radio active time, mobile radio active adjusted time, interactive time, power save mode enabled time, connectivity changes, device idle mode enabled time, device idle mode enabled count, device idling time, device idling count, mobile radio active count, mobile radio active unknown time"
gn,Global Network,"mobile RX total bytes, mobile TX total bytes, Wi-Fi RX total bytes, Wi-Fi TX total bytes, mobile RX total packets, mobile TX total packets, Wi-Fi RX total packets, Wi-Fi TX total packets"
br,Screen Brightness,"dark, dim, medium, light, bright"
sst,Signal Scanning Time,signal scanning time
sgt,Signal Strength Time,"none, poor, moderate, good, great"
sgc,Signal Strength Count,"none, poor, moderate, good, great"
dct,Data Connection Time,"none, GPRS, EDGE, UMTS, CDMA, EVDO_0, EVDO_A, 1xRTT, HSDPA, HSUPA, HSPA, IDEN, EVDO_B, LTE, EHRPD, HSPAP, other"
dcc,Data Connection Count,"none, GPRS, EDGE, UMTS, CDMA, EVDO_0, EVDO_A, 1xRTT, HSDPA, HSUPA, HSPA, IDEN, EVDO_B, LTE, EHRPD, HSPAP, other"
wst,Wi-Fi State Time,"off, off scanning, on no networks, on disconnected, on connected STA, on connected P2P, on connected STA P2P, soft AP"
wsc,Wi-Fi State Count,"off, off scanning, on no networks, on disconnected, on connected STA, on connected P2P, on connected STA P2P, soft AP"
wsst,Wi-Fi Supplicant State Time,"invalid, disconnected, interface disabled, inactive, scanning, authenticating, associating, associated, four-way handshake, group handshake, completed, dormant, uninitialized"
wssc,Wi-Fi Supplicant State Count,"invalid, disconnected, interface disabled, inactive, scanning, authenticating, associating, associated, four-way handshake, group handshake, completed, dormant, uninitialized"
wsgt,Wi-Fi Signal Strength Time,"none, poor, moderate, good, great"
wsgc,Wi-Fi Signal Strength Count,"none, poor, moderate, good, great"
bst,Bluetooth State Time,"inactive, low, med, high"
bsc,Bluetooth State Count,"inactive, low, med, high"
"""


class BatteryStatsSection:
    def __init__(self, id, description, fields):
        self.id = id
        self.description = description
        self.remaining_fields = fields

    @staticmethod
    def Load(raw):
        sections = []
        for line in raw.split('\n'):
            if not line:
                continue
            id, description, raw_fields = line.split(",", 2)

            if raw_fields.strip().startswith('"'):
                remaining_fields = list(map(lambda item: item.strip(), raw_fields[1:-1].split(",")))
            else:
                remaining_fields = [raw_fields.strip()]

            sections.append(BatteryStatsSection(id, description, remaining_fields))

        return sections



if __name__ == "__main__":
    sections = BatteryStatsSection.Load(raw_batterystats_fields)

    for section in sections:
        print(section.id, section.description, section.remaining_fields)
