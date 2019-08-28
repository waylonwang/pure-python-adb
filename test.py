from pyadb.client  import Client as AdbClient

client = AdbClient()
device = client.device("FA6A90302822")
print(device.shell("dumpsys meminfo"))