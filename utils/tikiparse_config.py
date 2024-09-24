import os
import yaml

class ConfigObject:
    def __init__(self, website_path, save_path, page_number, datafame):
        self.website_path = website_path
        self.save_path = save_path
        self.page_number = page_number
        self.datafame = datafame

    def __str__(self):
        return f"save_path: {self.save_path}, website_path: {self.website_path}, page_number: {self.page_number}, dataframe: {self.dataframe}"

# Lấy đường dẫn hiện tại của tệp tin (nơi chứa file tikiparse_config.py)
script_dir = os.path.dirname(__file__)
# Xây dựng đường dẫn đến file YAML cấu hình (parse_config.yml) 
yaml_path = os.path.join(script_dir,'parse_config.yml')

# Mở và đọc file YAML chứa cấu hình
with open(yaml_path, 'r') as ymlfile:
    cfg =  yaml.safe_load(ymlfile)# Đọc và parse nội dung của file YAML thành một cấu trúc dữ liệu Python

    config_object_list = []

     # Lặp qua từng phần trong file YAML để lấy các thông số cần thiết
    for section in cfg:
        website_path = cfg[section]['path']['website_path']
        save_path = cfg[section]['path']['save_path']
        page_number = cfg[section]['page']['page_number']
        datafame = cfg[section]['datafame']
        config_object_list.append(ConfigObject(website_path, save_path, page_number, datafame))


# Hàm này trả về các giá trị cấu hình quan trọng
def get_config():
    return{
        'website_path': website_path,
        'save_path':save_path,
        'page_number':page_number,
        'datafame':datafame
    }


