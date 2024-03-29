import re
import json

blue_active="blue active"
blue_active_config="E:\BLUE SCRIPT\MBA.Cli-win-x64-single-cut\config\config.json"

arknights="arknights"
arknights_config="E:\MAA-v4.10.4-beta.1-win-x64\config\gui.json"

def port_load(display_name):
    # 讀取所有檔案內的內容
    with open(r"D:\BlueStacks_nxt\bluestacks.conf", 'r',encoding="utf-8") as file:
        data = file.read()

    # 找目標模擬器的正規表達式
    BS_name = display_name
    prefix_pattern = rf'(.+).display_name="{BS_name}"'

    # 找目標模擬器
    m = re.search(prefix_pattern, data)
    prefix = m.group(1)

    # 找 port 的正規表達式
    port_pattern = rf'{prefix}.status.adb_port="(\d+)"'

    # 找 port
    m = re.search(port_pattern, data)
    port = int(m.group(1))
    return port

def json_replace(fileName,new_port,game_name):
    with open(fileName, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 提取原始地址
    if(game_name==blue_active):
        old_address = data['Core']['AdbAddress']
    else:
        old_address = data['Configurations']['Default']['Connect.Address']

    # 提取原始端口号
    port_number = old_address.split(":")[1]

    # 定義新的連接埠號碼（這裡假設替換為"12345"）
    new_port_number = str(new_port)

    # 替換連接埠號
    new_address = old_address.replace(port_number, new_port_number)

    # 更新JSON資料中的位址
    if(game_name==blue_active):
        data['Core']['AdbAddress']= new_address
    else:
        data['Configurations']['Default']['Connect.Address'] = new_address
    

    # 将修改后的数据写回JSON文件
    with open(fileName, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("替换完成!")


json_replace(blue_active_config,port_load(blue_active),blue_active)
json_replace(arknights_config,port_load(arknights),arknights)