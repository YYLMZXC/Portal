# Xposed Module

## 模块说明

Xposed模块是Portal项目的核心组件，负责拦截和修改Android系统的定位服务，实现虚拟定位功能。该模块基于LSPosed框架开发，支持多种定位方式的Hook操作。

## 功能特性

### 定位服务Hook
- **GPS定位Hook**: 拦截系统GPS定位服务，提供虚拟GPS数据
- **Fused Location Hook**: 支持Google Fused Location Provider的定位模拟
- **网络定位Hook**: 支持基于网络的定位服务模拟
- **位置管理器Hook**: 拦截LocationManager的各种定位方法

### 传感器模拟
- **加速度传感器**: 模拟设备加速度数据
- **陀螺仪传感器**: 模拟设备陀螺仪数据
- **方向传感器**: 模拟设备方向数据

### 其他功能
- **NMEA数据支持**: 生成和解析NMEA格式的GPS数据
- **AGPS支持**: 模拟AGPS辅助定位功能
- **隐藏模拟标记**: 可选隐藏定位数据中的模拟标记

## 技术实现

### 核心Hook点

#### 系统服务Hook
- `ILocationManager`: 系统位置管理服务的AIDL接口
- `LocationManager`: 应用层位置管理器
- `GnssLocationProvider`: GPS位置提供者
- `AbstractLocationProvider`: 抽象位置提供者

#### 定位数据处理
- 拦截位置报告方法
- 修改位置数据内容
- 添加模拟标记
- 支持多种坐标系统

### 代码结构

```
moe.fuqiuluo.xposed/
├── hooks/                  # 各种Hook实现
│   ├── LocationManagerHook.kt     # LocationManager Hook
│   ├── LocationServiceHook.kt     # 位置服务Hook
│   ├── gnss/                      # GPS相关Hook
│   ├── fused/                     # Fused Location相关Hook
│   ├── sensor/                    # 传感器相关Hook
│   └── provider/                  # 位置提供者相关Hook
├── FakeLocation.kt                # 主Hook入口
└── utils/                         # 工具类
```

## 支持的Android版本

- **最低支持**: Android 7.0 (API 24)
- **最高支持**: Android 15 (API 35)

## 构建说明

### 依赖项
- Xposed API
- Android NDK
- CMake

### 构建命令
```bash
# 构建xposed模块
./gradlew :xposed:build

# 构建包含xposed模块的完整APK
./gradlew assembleRelease
```

## 注意事项

### 性能影响
- Hook操作可能会对系统性能产生轻微影响
- 建议仅在需要时启用虚拟定位功能

### 兼容性问题
- 不同Android版本的系统服务实现可能有所差异
- 部分定制ROM可能对定位服务进行了修改，可能影响Hook效果

## 致谢

感谢以下项目和开发者对本模块的启发和支持：

- [FuckLocation](https://github.com/Mikotwa/FuckLocation/blob/main/app/src/main/java/fuck/location/xposed/location/LocationHookerAfterS.kt)
- [LSPosed Framework](https://github.com/LSPosed/LSPosed)
- [Xposed Framework](https://github.com/rovo89/XposedBridge)