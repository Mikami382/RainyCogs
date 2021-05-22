from datetime import datetime, timedelta

import requests
test = {'last-updated': '2021-05-22 13:00:49.378593', 'list': ['202.142.178.98:8080', '94.28.35.7:8080', '168.205.102.26:8080', '93.183.214.121:8080', '110.38.57.243:8080', '80.244.229.199:8080', '139.59.233.24:3128', '140.227.63.136:58888', '36.255.84.213:83', '91.193.253.188:23500', '89.109.252.129:8080', '178.205.169.210:3128', '51.15.217.77:3128', '203.81.95.42:8080', '181.118.145.146:999', '45.173.12.224:999', '178.140.58.34:8080', '103.7.27.186:8080', '164.77.177.30:999', '66.209.54.230:8080', '118.194.236.143:3128', '176.113.157.149:42850', '190.92.25.193:8588', '204.199.67.171:999', '93.170.97.160:8080', '103.236.135.182:8080', '209.33.9.244:8080', '41.190.92.84:48515', '190.85.24.13:999', '41.223.47.187:8080', '96.2.228.18:8080', '41.180.68.195:8080', '217.113.30.218:8080', '144.91.85.172:3128', '168.181.196.76:8080', '24.172.82.94:53281', '14.207.207.123:8080', '45.174.251.6:999', '190.152.5.126:53040', '203.112.209.10:8080', '197.155.83.17:8080', '102.33.21.36:8080', '103.154.190.6:8080', '65.182.5.212:8080', '45.70.59.17:8080', '103.124.97.11:8080', '159.224.166.129:38779', '219.92.3.149:8080', '177.124.168.81:8080', '71.172.1.52:8080', '180.183.0.109:8080', '179.189.226.186:8080', '164.163.12.50:8080', '182.71.146.148:8080', '177.11.84.252:8080', '95.143.220.5:45939', '41.164.68.194:8080', '182.160.119.155:8080', '173.215.67.137:8080', '150.95.89.200:3128', '45.233.143.14:999', '191.5.0.79:53281', '82.147.118.164:8080', '200.29.148.178:8080', '217.195.203.29:3131', '89.96.48.189:8080', '117.211.203.210:3128', '128.199.254.103:23352', '45.185.162.194:999', '207.148.30.112:5566', '69.30.200.146:3128', '102.68.134.130:6666', '138.186.78.1:999', '217.60.194.34:8080', '85.143.254.20:8080', '186.226.184.54:666', '156.67.172.185:3128', '181.48.111.246:49094', '81.33.4.214:61711', '83.238.13.109:8080', '92.245.142.215:8080', '45.182.240.73:3128', '88.255.102.166:9090', '181.78.20.59:999', '194.152.235.171:8080', '193.105.107.155:8080', '93.171.224.5:8080', '103.154.241.252:8080', '5.133.27.61:3129', '79.104.197.58:8080', '98.154.21.253:3128', '143.255.52.102:31158', '179.51.136.50:8080', '89.208.35.81:3128', '61.19.145.66:8080', '103.89.156.13:8080', '109.127.82.66:8080', '150.129.151.62:6666', '37.157.165.115:8080', '46.209.30.12:8080', '143.55.57.18:8080', '143.55.33.218:8080', '62.113.113.155:3128', '46.209.207.146:8080', '45.176.243.116:8080', '111.90.179.74:8080', '183.88.215.252:8080', '209.40.237.43:8080', '177.10.162.222:8080', '68.188.63.149:8080', '181.176.149.155:999', '201.174.173.122:999', '103.89.136.77:3128', '138.122.7.25:32192', '187.60.209.78:8080', '72.50.34.145:999', '180.211.183.178:60604', '47.88.7.115:3129', '165.22.59.84:8080', '31.172.105.144:8080', '109.245.242.105:35659', '81.16.9.51:8080', '212.179.18.75:3128', '45.143.109.118:8080', '45.236.120.253:999', '154.0.2.166:8080', '103.139.194.69:8080', '162.155.10.150:55443', '118.67.221.82:8080', '75.104.15.119:8080', '86.123.166.109:8080', '62.112.118.14:8080', '195.138.90.226:3128', '72.252.4.150:8080', '103.109.36.52:2401', '34.122.40.247:3128', '42.201.134.22:3128', '103.145.185.119:8080', '197.211.45.4:10000', '102.141.197.17:8080', '62.152.75.110:50287', '139.180.165.197:3128', '117.6.161.118:53281', '194.242.98.33:3128', '101.51.106.70:49285', '220.135.165.38:8080', '113.53.60.38:8080', '140.227.68.230:58888', '203.143.33.249:8080', '34.64.136.235:3128', '172.107.159.194:443', '185.189.14.93:1195', '81.91.137.44:8080', '160.16.212.156:3128', '27.131.179.204:10443', '190.53.46.14:38525', '103.152.101.136:8080', '67.206.202.145:999', '125.25.45.181:8080', '45.181.224.78:999', '103.5.232.145:8080', '182.160.108.188:8090', '46.238.230.4:8080', '201.82.2.141:3128', '1.179.144.41:8080', '91.225.226.39:44388', '178.134.157.215:8080', '203.190.2.181:8080', '139.180.188.202:3128', '67.219.125.54:8080', '152.67.1.199:8000', '186.7.232.253:999', '43.250.127.98:9001', '154.113.20.158:8080', '186.157.242.229:8080', '212.174.61.18:8080', '89.20.48.116:8080', '200.54.247.98:8080', '207.180.228.55:80', '188.163.170.130:41209', '181.78.1.106:8080', '193.176.242.144:8080', '161.199.130.1:8080', '195.9.162.186:8080', '85.198.250.135:3128', '102.67.9.146:8080', '88.220.104.178:8080', '94.74.132.129:808', '13.250.215.119:3128', '184.155.36.194:8080', '167.86.114.209:8118', '38.21.36.136:8080', '115.87.154.82:8080', '93.91.162.216:8080', '190.216.129.77:999', '178.183.133.107:8080', '45.117.61.34:8080', '172.94.75.223:8080', '102.141.210.93:53281', '195.201.61.51:8000', '45.185.136.250:8080', '103.196.233.199:8080', '189.39.241.165:3128', '123.253.36.99:8080', '80.93.213.214:3137', '95.47.234.1:8080', '188.138.82.136:80', '197.231.198.172:42461', '5.44.54.16:8080', '204.199.148.155:8080', '78.142.232.116:8080', '1.2.169.101:47477', '103.22.172.49:59458', '212.129.4.22:3128', '181.129.183.19:53281', '14.207.121.64:8080', '46.98.99.128:8080', '159.89.131.73:3128', '44.229.45.197:33128', '103.216.82.37:6666', '41.215.85.74:8080', '117.212.192.97:8080', '200.155.139.242:3128', '179.52.253.165:999', '91.194.239.122:8080', '91.187.113.205:53281', '210.8.81.246:8080', '152.0.224.187:999', '188.133.192.164:8080', '46.238.48.82:8080', '193.232.252.38:8080', '150.107.207.137:61954', '95.165.4.178:8080', '181.143.227.123:8080', '158.46.127.222:52574', '1.179.183.73:50178', '47.254.90.125:8081', '138.0.91.218:999', '193.36.33.3:8080', '181.143.106.162:52151', '165.29.108.250:3128', '139.59.185.55:8080', '136.243.81.120:8080', '188.235.8.5:51729', '103.101.82.122:8080', '3.20.236.208:49205', '109.200.156.102:8080', '186.0.231.140:999', '68.183.54.155:8080', '152.179.12.86:3128', '51.158.123.35:9999', '142.165.167.117:53281', '185.3.213.8:8080', '200.24.159.210:999', '62.27.108.174:8080', '187.49.254.14:8080', '103.35.135.2:82', '138.122.99.102:999', '177.66.112.221:57945', '103.141.158.234:8080', '91.150.189.122:30389', '206.189.146.202:8080', '85.105.139.53:8090', '103.157.249.107:8080', '154.126.60.90:8080', '20.47.98.2:3128', '82.137.247.179:8889', '45.77.249.58:8080', '94.242.59.20:3128', '122.15.131.65:57873', '173.46.67.172:58517', '171.244.50.88:3128', '104.248.249.47:3122', '160.119.125.25:8080', '119.28.71.122:22225', '94.73.239.124:55443', '123.200.3.138:8080', '103.90.238.13:8080', '103.81.114.182:53281', '86.110.27.165:3128', '190.214.27.46:8080', '103.42.195.70:53281', '13.82.88.73:3128', '47.251.13.204:3128', '46.209.210.179:8080', '24.172.34.114:49920', '103.252.117.100:8080', '35.206.150.95:3128', '111.235.65.211:45811', '1.2.254.185:8080', '89.223.90.116:3128', '150.129.171.158:8080', '129.146.180.91:3128', '199.192.126.211:8080', '210.18.133.71:8080', '102.134.220.91:8080', '211.24.105.19:47615', '103.16.71.233:83', '103.255.146.245:82', '80.245.117.130:8080', '180.211.183.138:8080', '104.244.75.218:8080', '103.6.184.222:39241', '41.194.37.106:45381', '212.174.201.70:9090', '107.150.37.83:3128', '181.101.80.226:10809', '5.190.141.144:8080', '52.140.230.28:3128', '180.183.135.177:8080', '107.178.9.186:8080', '103.99.177.32:8080', '81.145.20.214:8080', '118.179.173.253:40836', '103.101.100.26:8080', '45.167.125.33:999', '79.104.25.218:8080', '47.254.90.125:8080', '68.183.129.76:3129', '78.157.254.58:51008', '46.209.106.66:8085', '161.49.215.57:8080', '91.148.120.226:8080', '103.205.15.129:8080', '5.58.97.89:8080', '113.161.130.101:8080', '175.215.29.220:3128', '91.142.12.34:8081', '196.0.34.142:33855', '180.180.171.121:8080', '183.88.213.85:8080', '141.0.180.242:8080', '212.120.186.39:60963', '45.228.48.4:53281', '82.99.217.18:8080', '150.129.250.28:33846', '47.56.9.58:3128', '66.42.67.212:3128', '154.73.159.253:8585', '181.196.205.250:38178', '45.174.248.35:999', '176.63.205.248:54621', '45.184.103.87:999', '68.183.180.222:3128', '206.81.2.180:3128', '192.119.203.124:48678', '212.126.113.34:8080', '172.93.3.22:999', '94.158.165.19:45915', '103.25.47.130:8080', '134.122.84.79:3128', '182.52.229.165:8080', '197.210.143.182:36496', '194.36.145.18:3128', '52.143.81.17:3128', '109.185.243.41:8081', '139.5.31.204:8080', '97.72.253.34:87', '213.216.67.190:8080', '131.108.118.27:8080', '31.173.94.93:43539', '185.23.82.186:8080', '31.192.252.121:53281', '86.34.197.6:23500', '103.110.47.51:8080', '117.121.211.170:8080', '190.145.202.29:999', '92.207.253.226:38157', '91.216.66.70:32306', '83.12.149.202:8080', '183.88.132.252:8080', '45.160.148.103:8080', '190.57.143.66:50719', '95.78.174.219:60473', '175.111.181.26:56297', '95.140.27.135:58901', '187.190.255.192:999', '103.159.67.58:8080', '79.127.56.147:8080', '197.245.17.88:8080', '141.98.112.166:8080', '113.161.58.255:8080', '81.134.57.82:3128', '185.242.113.156:3128', '75.111.123.167:1888', '134.122.22.233:3128', '85.214.83.135:8085', '200.111.182.6:443', '103.224.39.2:83', '109.200.159.26:8080', '94.158.148.50:8080', '1.20.97.181:55285', '158.51.201.249:8080', '173.212.243.113:3128', '36.37.136.171:8080', '193.233.9.167:57625', '203.191.8.67:8080', '46.98.28.24:8080', '77.70.35.87:37475', '62.201.226.186:8080', '']}
url = 'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt'
r = requests.get(url=url)
res = r.text

proxies_list = []
for lines in res.split('\n'):
    proxy = ''.join(lines)
    proxies_list.append(proxy)

proxies = {'last-updated': '2021-05-22 12:40:28.662019', 'list': ['202.142.178.98:8080']}
print(proxies_list)
if len(proxies) == 0 or \
        (datetime.now() - datetime.strptime(proxies['last-updated'], '%Y-%m-%d %H:%M:%S.%f')) > timedelta(1):
    print('yeet')
else:
    print('wat')