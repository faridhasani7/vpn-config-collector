import requests


def main_config_downloader():

    url = "https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/All_Configs_Sub.txt"

    save_path_vmess = 'Configs/vmess.txt'
    save_path_vless = 'Configs/vless.txt'
    save_path_ss = 'Configs/ss.txt'

    clear_config_files(save_path_vmess, save_path_vless, save_path_ss)
    vmess_downloader(url, save_path_vmess)
    vless_downloader(url, save_path_vless)
    ss_downloader(url, save_path_ss)


def vmess_downloader(url, save_path_vmess):
    print("Downloading &&  Creating Vmess File")
    vmess_list = []
    response = requests.get(url).text
    for config in response.splitlines():
        if config.startswith("vmess"):
            open(save_path_vmess, "a").write(config + "\n")

    # make vmess list for use with telegram bot
    with open(save_path_vmess, "r") as file:
        data = file.readlines()
        vmess_list.append(data)

    return vmess_list


def ss_downloader(url, save_path_ss):
    print("Downloading &&  Creating ss File")
    ss_list = []
    response = requests.get(url).text
    for config in response.splitlines():
        if config.startswith("ss"):
            open(save_path_ss, "a").write(config + "\n")

    # make ss list for use with telegram bot
    with open(save_path_ss, "r") as file:
        data = file.readlines()
        ss_list.append(data)

    return ss_list


def vless_downloader(url, save_path_vless):
    print("Downloading &&  Creating Vless File")
    vless_list = []
    response = requests.get(url).text
    for config in response.splitlines():
        if config.startswith("vless"):
            open(save_path_vless, "a", encoding='utf-8').write(config + "\n")

    # make vmess list for use with telegram bot
    with open(save_path_vless, "r") as file:
        data = file.readline()
        vless_list.append(data)

    return vless_list
# clear vmess.txt && vless.txt files


def clear_config_files(save_path_vmess, save_path_vless, save_path_ss):
    print("Clear Vmess && Vless Files")
    new_data = ""
    with open(save_path_vmess, 'w') and open(save_path_vless, 'w') and open(save_path_ss, 'w') as file_config:
        file_config.write(new_data)
        file_config.close()


if __name__ == "__main__":
    main_config_downloader()
