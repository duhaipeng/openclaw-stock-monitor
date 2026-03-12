# 📈 OpenClaw 股市监控技能

一个功能强大的OpenClaw技能，用于实时监控股票市场、设置价格提醒和进行技术分析。

![版本](https://img.shields.io/badge/版本-v1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![OpenClaw](https://img.shields.io/badge/OpenClaw-2026.3.8+-orange)

## ✨ 功能特性

### 🎯 核心功能
- **实时监控**：支持A股、港股、美股实时行情
- **智能提醒**：价格突破、涨跌幅、成交量异常提醒
- **技术分析**：移动平均线、RSI、趋势判断
- **多格式输出**：控制台、JSON、CSV、Excel

### 🚀 高级功能
- **自定义监控列表**：支持JSON配置
- **定时任务**：Cron定时检查
- **API集成**：易于与其他系统集成
- **数据导出**：支持多种数据格式

## 🛠️ 快速开始

### 安装
```bash
# 克隆仓库
git clone https://github.com/yourusername/openclaw-stock-monitor.git
cd openclaw-stock-monitor

# 安装依赖
pip install -r requirements.txt
```

### 基本使用
```bash
# 查询单只股票
python3 scripts/stock_check.py --stock 000001

# 查询多只股票
python3 scripts/stock_check.py --stocks 000001,399001,HSI

# 使用配置文件
python3 scripts/stock_check.py --config config/monitor.json
```

### OpenClaw集成
将技能目录复制到OpenClaw技能目录：
```bash
cp -r stock-monitor ~/.openclaw/workspace/skills/
```

然后在OpenClaw中调用：
```
查询贵州茅台股价
当腾讯突破350元时提醒我
分析上证指数技术指标
```

## 📋 配置说明

### 监控配置 (`config/monitor.json`)
```json
{
  "stocks": ["000001", "00700", "AAPL", "HSI"],
  "alert_rules": {
    "change_threshold": 5.0,
    "price_break_high": {
      "000001": 4200,
      "00700": 350
    },
    "check_interval": 1800,
    "notify_channels": ["qq", "email"]
  }
}
```

### 提醒规则
- **价格突破**：设置上下限价格
- **涨跌幅**：设置百分比阈值
- **成交量**：成交量异常检测
- **技术指标**：RSI超买超卖提醒

## 📊 输出示例

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
🔔 提醒通知:
  • 上证指数上涨0.25%
```

### JSON输出
```json
{
  "timestamp": "2026-03-12 09:17:25",
  "stocks": [
    {
      "name": "上证指数",
      "code": "000001",
      "price": "4133.43",
      "change": "+10.29",
      "change_percent": "+0.25%",
      "volume": "707727169"
    }
  ],
  "alerts": ["上证指数上涨0.25%"]
}
```

## 🔧 技术架构

### 数据源
- **A股**：腾讯财经API
- **港股**：腾讯财经API
- **美股**：雅虎财经API（计划中）

### 技术栈
- **Python 3.8+**：核心逻辑
- **Requests**：HTTP请求
- **Pandas**：数据处理
- **Schedule**：定时任务

### 目录结构
```
stock-monitor/
├── SKILL.md              # 技能文档
├── README.md             # 项目说明
├── scripts/
│   ├── stock_check.py    # 主监控脚本
│   ├── technical.py      # 技术分析脚本
│   └── alert.py          # 提醒处理脚本
├── config/
│   ├── monitor.json      # 监控配置
│   └── rules.json        # 提醒规则
├── examples/             # 使用示例
├── tests/               # 测试用例
└── requirements.txt     # 依赖列表
```

## 🚀 部署方案

### 方案一：本地部署
```bash
# 1. 克隆项目
git clone https://github.com/yourusername/openclaw-stock-monitor.git

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置监控
cp config/monitor.example.json config/monitor.json
# 编辑config/monitor.json

# 4. 运行监控
python3 scripts/stock_check.py
```

### 方案二：Docker部署
```dockerfile
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python3", "scripts/stock_check.py"]
```

### 方案三：云函数部署
支持AWS Lambda、阿里云函数计算等Serverless平台。

## 📈 路线图

### v1.1.0 (计划中)
- [ ] 添加更多技术指标（MACD, Bollinger Bands）
- [ ] 支持加密货币监控
- [ ] 添加图表生成功能
- [ ] 支持Webhook通知

### v1.2.0 (规划中)
- [ ] 机器学习预测模型
- [ ] 回测系统
- [ ] 移动端应用
- [ ] 多语言支持

## 🤝 贡献指南

欢迎贡献代码！请阅读[贡献指南](CONTRIBUTING.md)。

### 开发流程
1. Fork项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## ⚠️ 免责声明

**投资有风险，入市需谨慎！**

本工具提供的股票数据仅供参考，不构成任何投资建议。使用者应自行判断并承担投资风险。作者不对因使用本工具而产生的任何投资损失负责。

## 🙏 致谢

- 感谢OpenClaw团队提供的优秀平台
- 感谢所有贡献者的辛勤工作
- 感谢用户的支持和反馈

## 📞 支持与反馈

- 问题反馈：[GitHub Issues](https://github.com/yourusername/openclaw-stock-monitor/issues)
- 功能请求：[GitHub Discussions](https://github.com/yourusername/openclaw-stock-monitor/discussions)
- 文档更新：欢迎提交PR

---
**让AI助手帮你智能投资，把握每一个市场机会！** 🚀