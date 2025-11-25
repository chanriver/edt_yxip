#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GitHub Actions 数据转换工具 - 优化版
"""

import os
import pandas as pd

def get_file_paths():
    """获取输入输出文件路径"""
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return (
        os.path.join(repo_root, 'data', 'result.csv'),
        os.path.join(repo_root, 'data', 'result.txt')
    )

def load_airport_mapping():
    """加载机场码映射"""
    return {
        # 亚洲
        "SIN": "新加坡", "HKG": "中国香港", "NRT": "日本", "KIX": "日本",
        "ICN": "韩国", "GMP": "韩国", "TPE": "台湾", "KUL": "马来西亚",
        "BKK": "泰国", "MNL": "菲律宾", "HAN": "越南", "SGN": "越南",
        "DEL": "印度", "BOM": "印度", "DXB": "阿联酋", "DOH": "卡塔尔",
        # 欧洲
        "LHR": "英国", "LGW": "英国", "CDG": "法国", "ORY": "法国",
        "FRA": "德国", "MUC": "德国", "AMS": "荷兰", "MAD": "西班牙",
        "BCN": "西班牙", "FCO": "意大利", "MXP": "意大利", "ZRH": "瑞士",
        "CPH": "丹麦", "ARN": "瑞典", "OSL": "挪威",
        # 美洲
        "JFK": "美国", "LGA": "美国", "EWR": "美国", "ORD": "美国",
        "LAX": "美国", "SFO": "美国", "MIA": "美国", "YYZ": "加拿大",
        "YVR": "加拿大", "GRU": "巴西", "GIG": "巴西", "EZE": "阿根廷",
        "SCL": "智利", "MEX": "墨西哥", "LIM": "秘鲁",
    }

def convert_data(input_file, output_file):
    """执行数据转换"""
    try:
        airport_map = load_airport_mapping()
        df = pd.read_csv(input_file)
        
        results = []
        for _, row in df.iterrows():
            ip = row['IP 地址']
            port = row['端口']
            region_code = row['地区码']
            country = airport_map.get(region_code, "未知")
            results.append(f"{ip}:{port}#{country}")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(results))
        
        print(f"✅ 转换完成！共处理 {len(results)} 条记录")
        return True
        
    except Exception as e:
        print(f"❌ 转换失败: {str(e)}")
        return False

if __name__ == "__main__":
    input_file, output_file = get_file_paths()
    
    print("="*60)
    print(f"开始转换 {input_file} → {output_file}")
    print("="*60)
    
    if convert_data(input_file, output_file):
        print("\n🎉 转换成功！")
    else:
        print("\n❌ 转换失败！")
        exit(1)
