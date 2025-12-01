# Portal
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Ffuqiuluo%2FPortal.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Ffuqiuluo%2FPortal?ref=badge_shield)

秋夜长，殊未央，月明白露澄清光，层城绮阁遥相望。

Telegram: https://t.me/portal_fuqiuluo

## 项目概述

Portal是一个基于LSPosed框架的虚拟定位模块，主要用于帮助Android应用开发者调试和测试需要使用定位信息的应用程序。该项目通过Hook系统服务来实现虚拟定位功能，支持多种定位方式的模拟，包括GPS、网络定位等。

### 主要用途
- 开发者调试定位相关功能
- 模拟不同地理位置进行应用测试
- 开发和测试基于位置的服务

## 架构说明

Portal项目采用模块化架构设计，主要包含以下几个核心模块：

### 1. app模块
- 主应用程序，提供用户界面和交互功能
- 集成百度地图SDK，提供地图显示和定位功能
- 提供设置界面，允许用户配置虚拟定位参数

### 2. xposed模块
- 核心Hook模块，负责拦截和修改系统定位服务
- 支持多种定位方式的Hook，包括GPS、Fused Location等
- 实现传感器信息模拟功能

### 3. system-api模块
- 提供对系统API的访问接口
- 适配不同Android版本的系统服务差异

### 4. nmea模块
- 处理NMEA格式的GPS数据
- 支持NMEA数据的解析和生成

## 技术栈

- **开发语言**: Kotlin, Java, C++
- **框架**: Android SDK, LSPosed, Xposed API
- **地图服务**: 百度地图SDK
- **网络请求**: OkHttp
- **数据解析**: Fastjson, Kotlinx Serialization
- **崩溃收集**: Bugly
- **构建工具**: Gradle Kotlin DSL
- **编译环境**: Android Studio, NDK

## 功能特性

### 已实现功能
- [x] 运行时创建通知，显示当前状态
- [x] 在模拟位置中添加标记，便于检测
- [x] 支持多种场景下的定位模拟
- [x] 传感器信息模拟
- [x] 通过摇杆控制位置移动
- [x] 可设置移动速度
- [x] 可设置海拔高度
- [x] 可设置定位精度
- [x] 移动时自动调整方位角

### 计划实现功能
- [ ] GPS状态模拟
- [ ] 手机基站信息模拟
- [ ] WiFi信息模拟

## 安装和使用

### 安装要求
- Android 8.0 (API 26) 及以上版本
- 已安装 LSPosed 框架
- 支持的架构: arm64-v8a, x86_64

### 安装步骤
1. 安装 Portal APK 文件
2. 在 LSPosed 管理器中启用 Portal 模块
3. 重启设备以应用模块

### 使用方法
1. 打开 Portal 应用
2. 在地图上选择要模拟的位置，或输入具体的经纬度坐标
3. 点击开始按钮启用虚拟定位
4. 可以通过设置界面调整定位参数，如速度、海拔等
5. 使用摇杆功能可以控制位置移动

## 如何检测 Portal

### 方法一：检查通知
- Portal 运行时会在状态栏创建通知，可以通过检查通知栏查看 Portal 是否在运行

### 方法二：检查 Location 对象
- Portal 会在模拟的 Location 对象中添加额外标记，可以通过代码检查这些标记

```kotlin
if (location.extras != null && location.extras!!.getBoolean("portal.enable", false)) {
    // Portal 正在模拟定位
}

if (location.extras != null && location.extras!!.getBoolean("is_mock", false)) {
    // 检测到模拟定位
}
```

## 注意事项

> [!note]
> 
> 中文地区特供：
> 
> 1. 本项目根据Apache 2.0许可证开放，可用于任何符合法律的目的，包括商业和非商业用途。我们特别鼓励将其用于学习和研究。使用者应遵守相关法律法规，禁止用于任何违法行为。
> 2. 根据Apache 2.0许可证，您可以自由修改、分发本代码及创建衍生作品，但需遵守以下条件：
>     * 保留原始版权声明和附带的NOTICE文件
>     * 提供Apache 2.0许可证副本
>     * 说明您所做的重大修改
> 3. 使用者需承诺遵守相关法律法规，因使用本软件导致的任何后果由使用者自行承担，与本项目开发者无关。
> 4. 开发者保留在使用者违反Apache 2.0许可证条款时追究法律责任的权利。

## 免责声明

- 如发现任何人利用Portal进行违法活动，请收集证据并向有关部门举报。
- 使用者应遵守所有适用的法律法规。任何企业/组织/个人对因违法使用Portal而产生的后果需自行承担责任。
- Portal开发者对任何因使用本软件而导致的法律纠纷不承担责任。
- 若有企业/组织/个人因使用Portal遇到技术问题导致损失或业务中断，Portal开发团队将在合理范围内提供技术支持和协助。
- Portal开发团队保留对本软件技术实现细节的最终解释权。

## 开发和贡献

### 开发环境搭建
1. 克隆项目仓库
2. 使用Android Studio打开项目
3. 确保安装了最新的Android SDK和NDK
4. 同步Gradle依赖

### 构建项目
```bash
# 构建所有架构的APK
./gradlew assembleRelease

# 构建特定架构的APK
./gradlew assembleAppRelease  # 所有架构
./gradlew assembleArm64Release  # 仅arm64-v8a
./gradlew assembleX64Release  # 仅x86_64
```

### 贡献指南
1. Fork项目仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开Pull Request

## 致谢

感谢以下项目和库对Portal的支持：

- [GoGoGo](https://github.com/ZCShou/GoGoGo)
- [Baidu Map SDK](https://lbsyun.baidu.com/faq/api?title=androidsdk)
- [LSPosed Framework](https://github.com/LSPosed/LSPosed)
- [Xposed Framework](https://github.com/rovo89/XposedBridge)

## 许可证

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Ffuqiuluo%2FPortal.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Ffuqiuluo%2FPortal?ref=badge_large)

Portal项目采用Apache 2.0许可证开源。详情请参阅[LICENSE](LICENSE)文件。

## 版本历史

Portal项目的版本历史记录可以在[refs目录](refs/)中查看，每个版本都有对应的说明文档。

## 联系方式

- Telegram群组: https://t.me/portal_fuqiuluo
- 如有问题或建议，欢迎提交Issue或Pull Request
