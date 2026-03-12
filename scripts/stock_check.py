#!/usr/bin/env python3
"""
股票监控脚本
支持A股、港股、美股实时数据查询
"""

import json
import sys
import time
from datetime import datetime
import subprocess

def get_stock_data(stock_code):
    """获取股票数据"""
    # A股: sh000001, sz399001
    # 港股: hkHSI
    # 美股: .DJI, .IXIC, .INX
    
    mapping = {
        "000001": "sh000001",  # 上证指数
        "399001": "sz399001",  # 深证成指
        "HSI": "hkHSI",        # 恒生指数
        "DJI": ".DJI",         # 道琼斯
        "IXIC": ".IXIC",       # 纳斯达克
        "INX": ".INX",         # 标普500
        "00700": "hk00700",    # 腾讯控股
        "AAPL": "AAPL",        # 苹果
    }
    
    code = mapping.get(stock_code, stock_code)
    
    try:
        # 使用腾讯财经API
        cmd = f'curl -s "https://qt.gtimg.cn/q={code}" | iconv -f gbk -t utf-8 2>/dev/null'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0 and result.stdout:
            data = result.stdout.strip()
            if 'v_' in data:
                # 解析数据格式: v_sh000001="1~上证指数~000001~4133.43~4123.14~..."
                parts = data.split('=')[1].strip('"').split('~')
                if len(parts) > 30:
                    return {
                        'name': parts[1],
                        'code': stock_code,
                        'price': parts[3],
                        'prev_close': parts[4],
                        'open': parts[5],
                        'high': parts[33],
                        'low': parts[34],
                        'change': parts[31],
                        'change_percent': parts[32],
                        'volume': parts[6],
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
    except Exception as e:
        print(f"获取股票数据失败: {e}", file=sys.stderr)
    
    return None

def check_alert_rules(stock_data, rules):
    """检查提醒规则"""
    alerts = []
    
    if not stock_data:
        return alerts
    
    try:
        current_price = float(stock_data['price'])
        prev_close = float(stock_data['prev_close'])
        change_percent = float(stock_data['change_percent'])
        
        # 价格突破提醒
        if 'price_break_high' in rules and rules['price_break_high'] and current_price > rules['price_break_high']:
            alerts.append(f"价格突破: {stock_data['name']} 突破 {rules['price_break_high']}元")
        
        if 'price_break_low' in rules and rules['price_break_low'] and current_price < rules['price_break_low']:
            alerts.append(f"价格跌破: {stock_data['name']} 跌破 {rules['price_break_low']}元")
        
        # 涨跌幅提醒
        if 'change_threshold' in rules and abs(change_percent) > rules['change_threshold']:
            direction = "上涨" if change_percent > 0 else "下跌"
            alerts.append(f"大幅{direction}: {stock_data['name']} {change_percent}%")
        
        # 成交量异常提醒 (简化版)
        if 'volume_alert' in rules and rules['volume_alert']:
            # 这里可以添加成交量分析逻辑
            pass
            
    except (ValueError, KeyError) as e:
        print(f"解析数据错误: {e}", file=sys.stderr)
    
    return alerts

def main():
    """主函数"""
    # 默认监控列表
    default_stocks = ["000001", "399001", "HSI", "DJI"]
    
    # 默认提醒规则
    default_rules = {
        'change_threshold': 3.0,  # 涨跌3%提醒
        'price_break_high': None,
        'price_break_low': None,
        'volume_alert': False
    }
    
    print(f"📈 股票监控报告 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    all_alerts = []
    
    for stock in default_stocks:
        data = get_stock_data(stock)
        if data:
            print(f"{data['name']} ({data['code']}):")
            print(f"  当前: {data['price']} | 涨跌: {data['change']} ({data['change_percent']}%)")
            print(f"  昨收: {data['prev_close']} | 今开: {data['open']}")
            print(f"  最高: {data['high']} | 最低: {data['low']}")
            print(f"  时间: {data['timestamp']}")
            print("-" * 40)
            
            # 检查提醒
            alerts = check_alert_rules(data, default_rules)
            all_alerts.extend(alerts)
        else:
            print(f"无法获取 {stock} 的数据")
            print("-" * 40)
    
    # 输出提醒
    if all_alerts:
        print("\n🔔 提醒通知:")
        for alert in all_alerts:
            print(f"  • {alert}")
    
    print(f"\n监控完成于 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()