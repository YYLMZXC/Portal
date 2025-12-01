# System API Module

## 模块说明

System API模块是Portal项目的系统API接口封装模块，提供对Android系统位置服务和传感器服务的访问接口。该模块封装了不同Android版本的系统API差异，为上层应用提供统一的调用接口，简化系统服务的使用。

## 功能特性

### 系统服务封装
- **位置服务**：封装LocationManager和ILocationManager接口
- **传感器服务**：封装SensorManager和各种传感器接口
- **GPS服务**：封装GnssLocationProvider和相关GPS服务接口
- **融合定位**：封装Fused Location Provider接口

### API兼容性
- **版本适配**：适配Android 7.0到Android 15的系统API差异
- **接口统一**：提供统一的调用接口，隐藏版本差异
- **向前兼容**：支持在低版本系统上调用高版本API（优雅降级）

### AIDL接口
- **ILocationManager**：位置管理服务的AIDL接口封装
- **ILocationProvider**：位置提供者的AIDL接口封装
- **IGnssLocationProvider**：GPS位置提供者的AIDL接口封装
- **ISensorManager**：传感器管理服务的AIDL接口封装

### 其他功能
- **反射工具**：提供安全的反射调用工具类
- **版本检测**：提供系统版本检测工具
- **API调用**：提供安全的系统API调用封装

## 技术实现

### 架构设计
- **接口抽象**：定义抽象接口，隐藏具体实现细节
- **工厂模式**：使用工厂模式创建不同版本的实现
- **适配器模式**：使用适配器模式适配不同版本的API
- **代理模式**：使用代理模式包装系统服务调用

### 核心组件

#### 位置服务封装
- **LocationServiceApi**：位置服务API接口
- **LocationManagerApi**：LocationManager API封装
- **ILocationManagerApi**：ILocationManager AIDL接口封装
- **LocationProviderApi**：位置提供者API封装

#### 传感器服务封装
- **SensorServiceApi**：传感器服务API接口
- **SensorManagerApi**：SensorManager API封装
- **SensorApi**：传感器API封装

#### GPS服务封装
- **GnssServiceApi**：GPS服务API接口
- **GnssLocationProviderApi**：GPS位置提供者API封装
- **GnssStatusApi**：GPS状态API封装

### 代码结构

```
system-api/src/main/
├── java/moe/fuqiuluo/portal/systemapi/
│   ├── LocationServiceApi.kt        # 位置服务API接口
│   ├── LocationManagerApi.kt        # LocationManager API封装
│   ├── ILocationManagerApi.kt       # ILocationManager API封装
│   ├── SensorServiceApi.kt          # 传感器服务API接口
│   ├── SensorManagerApi.kt          # SensorManager API封装
│   ├── GnssServiceApi.kt            # GPS服务API接口
│   ├── GnssLocationProviderApi.kt   # GPS位置提供者API封装
│   ├── reflection/                  # 反射工具类
│   │   ├── SafeReflection.kt        # 安全反射工具
│   │   ├── ClassUtils.kt            # 类工具类
│   │   └── MethodUtils.kt           # 方法工具类
│   ├── version/                     # 版本适配
│   │   ├── ApiLevel.kt              # API级别定义
│   │   ├── VersionChecker.kt        # 版本检测工具
│   │   └── VersionAdapter.kt        # 版本适配器
│   └── utils/                       # 其他工具类
└── aidl/moe/fuqiuluo/portal/systemapi/
    └── # AIDL接口文件（从refs目录复制）
```

## 支持的Android版本

- **最低支持**: Android 7.0 (API 24)
- **最高支持**: Android 15 (API 35)

## 构建说明

### 依赖项
- Android SDK
- Android NDK (可选，用于JNI调用)

### 构建命令
```bash
# 构建system-api模块
./gradlew :system-api:build

# 构建包含system-api模块的完整APK
./gradlew assembleRelease
```

## 使用说明

### 位置服务API使用

```kotlin
// 获取位置服务API实例
val locationServiceApi = LocationServiceApi.getInstance(context)

// 获取LocationManager
val locationManager = locationServiceApi.getLocationManager()

// 获取ILocationManager
val iLocationManager = locationServiceApi.getILocationManager()

// 调用系统API
val providers = locationServiceApi.getProviders(true)
val lastLocation = locationServiceApi.getLastLocation()
```

### 传感器服务API使用

```kotlin
// 获取传感器服务API实例
val sensorServiceApi = SensorServiceApi.getInstance(context)

// 获取SensorManager
val sensorManager = sensorServiceApi.getSensorManager()

// 获取传感器列表
val sensors = sensorServiceApi.getSensors()

// 获取特定传感器
val accelerometer = sensorServiceApi.getSensor(Sensor.TYPE_ACCELEROMETER)
```

### GPS服务API使用

```kotlin
// 获取GPS服务API实例
val gnssServiceApi = GnssServiceApi.getInstance(context)

// 获取GPS位置提供者
val gnssLocationProvider = gnssServiceApi.getGnssLocationProvider()

// 获取GPS状态
val gnssStatus = gnssServiceApi.getGnssStatus()
```

## 注意事项

### 权限要求
- **系统服务权限**：部分系统服务调用需要系统权限
- **位置权限**：位置相关API调用需要位置权限
- **传感器权限**：传感器相关API调用需要传感器权限

### 性能影响
- 频繁调用系统API可能会对性能产生影响
- 建议缓存API实例，避免频繁创建

### 兼容性问题
- 不同厂商的定制ROM可能对系统API进行了修改
- 某些系统API可能在特定设备上不可用
- 建议在调用前进行版本检查和可用性验证

## 常见问题

### API调用失败
- 检查系统版本是否支持该API
- 检查是否有足够的权限
- 检查系统服务是否可用

### 版本适配问题
- 确认使用了正确的API版本封装
- 检查是否正确处理了版本差异
- 考虑使用优雅降级策略

### AIDL接口问题
- 确认AIDL接口定义与系统版本匹配
- 检查AIDL接口的调用方式是否正确
- 考虑使用动态代理处理AIDL接口调用

## 致谢

感谢以下项目和开发者对本模块的启发和支持：

- [Android Open Source Project](https://source.android.com/)
- [LSPosed Framework](https://github.com/LSPosed/LSPosed)
- [Xposed Framework](https://github.com/rovo89/XposedBridge)