# 股市监控技能 - 使用示例

## 基本查询

### 查询单只股票
```bash
python3 scripts/stock_check.py --stock 000001
```

### 查询多只股票
```bash
python3 scripts/stock_check.py --stocks 000001,399001,HSI
```

### 设置自定义监控列表
创建 `config/monitor.json`:
```json
{
  "stocks": ["000001", "00700", "AAPL"],
  "alert_rules": {
    "change_threshold": 5.0,
    "price_break_high": {
      "000001": 4200,
      "00700": 350
    },
    "check_interval": 1800
  }
}
```

然后运行:
```bash
python3 scripts/stock_check.py --config config/monitor.json
```

## 集成到OpenClaw

### 方法1: 直接调用
在OpenClaw技能中调用:
```python
import subprocess
result = subprocess.run(["python3", "scripts/stock_check.py"], 
                       capture_output=True, text=True)
print(result.stdout)
```

### 方法2: 定时任务
设置cron定时检查:
```bash
# 每30分钟检查一次
*/30 * * * * cd /path/to/stock-monitor && python3 scripts/stock_check.py >> logs/stock.log
```

### 方法3: QQ Bot集成
在QQ Bot技能中添加:
```python
def stock_command(stock_code):
    # 调用股票查询
    data = get_stock_data(stock_code)
    if data:
        return f"{data['name']}: {data['price']} ({data['change_percent']}%)"
    return "查询失败"
```

## 提醒配置

### 价格突破提醒
```json
{
  "price_break_high": {
    "000001": 4200,
    "399001": 15000
  },
  "price_break_low": {
    "000001": 4000,
    "HSI": 25000
  }
}
```

### 涨跌幅提醒
```json
{
  "change_threshold": 3.0,  # 涨跌3%提醒
  "volume_alert": true      # 成交量异常提醒
}
```

## 输出格式

### 控制台输出
```
📈 股票监控报告 2026-03-12 09:17:25
==================================================
上证指数 (000001):
  当前: 4133.43 | 涨跌: +10.29 (+0.25%)
  昨收: 4123.14 | 今开: 4123.67
  最高: 4135.84 | 最低: 4112.80
  时间: 2026-03-12 09:17:25
----------------------------------------
```

### JSON格式输出
```bash
python3 scripts/stock_check.py --format json
```
输出:
```json
{
  "timestamp": "2026-03-12 09:17:25",
  "stocks": [
    {
      "name": "上证指数",
      "code": "000001",
      "price": "4133.43",
      "change": "+10.29",
      "change_percent": "+0.25%"
    }
  ],
  "alerts": []
}
```

## 高级功能

### 技术指标计算
```bash
# 计算移动平均线
python3 scripts/technical.py --stock 000001 --indicator ma

# 计算RSI
python3 scripts/technical.py --stock 000001 --indicator rsi
```

### 数据导出
```bash
# 导出为CSV
python3 scripts/stock_check.py --export csv --output data/stocks.csv

# 导出为Excel
python3 scripts/stock_check.py --export excel --output data/stocks.xlsx
```

## 故障排除

### 常见问题
1. **数据获取失败**: 检查网络连接和API状态
2. **解析错误**: 确保股票代码格式正确
3. **权限问题**: 确保脚本有执行权限

### 日志查看
```bash
# 查看详细日志
tail -f logs/stock.log

# 查看错误日志
grep ERROR logs/stock.log
```

## 更新与维护

### 检查更新
```bash
git pull origin main
```

### 添加新功能
1. 在 `scripts/` 目录添加新脚本
2. 更新 `SKILL.md` 文档
3. 添加测试用例
4. 提交更新