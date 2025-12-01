# App Module

## 模块说明

App模块是Portal项目的用户界面部分，提供直观的操作界面，用于控制和配置虚拟定位功能。该模块使用Kotlin开发，基于AndroidX架构，支持多种定位方式的设置和管理。

## 功能特性

### 用户界面
- **主页**：显示当前位置信息和主要控制按钮
- **地图控制**：集成百度地图，支持地图浏览、缩放、定位
- **位置搜索**：支持地址搜索和位置选择
- **摇杆控制**：提供虚拟摇杆，用于手动调整位置
- **设置面板**：提供详细的功能配置选项

### 定位管理
- **GPS模拟**：控制GPS定位的开启和关闭
- **位置设置**：手动输入或地图选择目标位置
- **坐标系统**：支持WGS84、GCJ02、BD09等多种坐标系统
- **历史位置**：保存和快速恢复历史定位点
- **收藏位置**：支持收藏常用位置

### 传感器模拟
- **传感器控制**：开启和关闭传感器模拟
- **传感器参数**：调整传感器模拟参数
- **传感器预设**：提供常用传感器状态预设

### 其他功能
- **运行通知**：显示服务运行状态通知
- **调试信息**：显示定位调试信息
- **数据导出**：导出定位数据
- **崩溃报告**：集成Bugly崩溃报告

## 技术实现

### 架构设计
- **MVVM架构**：采用Model-View-ViewModel架构模式
- **组件化**：使用Fragment和Activity组件化开发
- **服务分离**：定位服务与UI分离，支持后台运行
- **响应式编程**：使用Kotlin Coroutines和Flow进行异步操作

### 核心组件

#### 主要Activity
- **MainActivity**：应用主入口，管理Fragment切换
- **SplashActivity**：应用启动页

#### 主要Fragment
- **HomeFragment**：主页，显示当前位置和主要控制
- **GnssMockFragment**：GPS模拟控制界面
- **SettingsFragment**：应用设置界面
- **MapFragment**：地图浏览和位置选择界面
- **SensorFragment**：传感器模拟控制界面

#### 服务组件
- **MockService**：虚拟定位服务
- **NotificationService**：通知管理服务
- **SensorService**：传感器模拟服务

### 代码结构

```
app/src/main/
├── java/moe/fuqiuluo/portal/
│   ├── MainActivity.kt             # 应用主入口
│   ├── Portal.kt                   # Application类
│   ├── fragments/                  # Fragment组件
│   │   ├── HomeFragment.kt         # 主页Fragment
│   │   ├── GnssMockFragment.kt     # GPS模拟Fragment
│   │   ├── SettingsFragment.kt     # 设置Fragment
│   │   └── ...                     # 其他Fragment
│   ├── services/                   # 服务组件
│   │   ├── MockService.kt          # 虚拟定位服务
│   │   ├── NotificationService.kt  # 通知服务
│   │   └── ...                     # 其他服务
│   ├── models/                     # 数据模型
│   │   ├── LocationData.kt         # 位置数据模型
│   │   ├── SensorData.kt           # 传感器数据模型
│   │   └── ...                     # 其他数据模型
│   ├── utils/                      # 工具类
│   │   ├── LocationUtils.kt        # 位置工具类
│   │   ├── SensorUtils.kt          # 传感器工具类
│   │   └── ...                     # 其他工具类
│   └── views/                      # 自定义视图
│       ├── JoystickView.kt         # 虚拟摇杆视图
│       ├── MapView.kt              # 地图视图
│       └── ...                     # 其他自定义视图
└── res/                            # 资源文件
    ├── layout/                     # 布局文件
    ├── drawable/                   # 图片资源
    ├── values/                     # 字符串、样式等
    └── ...                         # 其他资源
```

## 支持的Android版本

- **最低支持**: Android 8.0 (API 26)
- **最高支持**: Android 15 (API 35)

## 构建说明

### 依赖项
- AndroidX
- 百度地图SDK
- OkHttp
- FastJson
- Bugly
- Kotlin Coroutines
- Android Navigation Component

### 构建命令
```bash
# 构建app模块
./gradlew :app:build

# 构建指定风味的APK
./gradlew assembleAppRelease    # 通用版本
./gradlew assembleArm64Release  # ARM64版本
./gradlew assembleX64Release    # X86_64版本

# 构建所有版本
./gradlew assembleRelease
```

## 安装说明

### 常规安装
1. 下载构建好的APK文件
2. 安装到Android设备
3. 启用应用的定位权限
4. 在LSPosed中激活模块

### 开发环境安装
```bash
# 安装到连接的设备
./gradlew installAppRelease
```

## 功能配置

### 位置设置
- **经纬度输入**：手动输入目标位置的经纬度
- **地址搜索**：搜索并选择目标地址
- **地图选择**：在地图上直接选择目标位置
- **坐标系统**：选择合适的坐标系统

### 传感器设置
- **加速度传感器**：开启/关闭加速度传感器模拟
- **陀螺仪传感器**：开启/关闭陀螺仪传感器模拟
- **方向传感器**：开启/关闭方向传感器模拟
- **传感器参数**：调整传感器模拟的灵敏度、范围等参数

### 其他设置
- **运行通知**：开启/关闭运行状态通知
- **调试信息**：开启/关闭调试信息显示
- **隐藏模拟标记**：开启/关闭隐藏定位模拟标记
- **坐标转换**：开启/关闭坐标自动转换

## 注意事项

### 权限要求
- **位置权限**：需要访问设备位置权限
- **存储权限**：需要读取和写入存储权限（用于导出数据）
- **通知权限**：需要发送通知权限（用于运行通知）

### 性能影响
- 地图渲染可能会消耗较多电量
- 后台运行的服务可能会增加电池消耗
- 建议在不需要时关闭应用或服务

### 兼容性问题
- 部分设备可能不支持某些传感器模拟
- 不同Android版本的权限管理可能有所差异
- 部分定制ROM可能对定位服务进行了修改，可能影响功能

## 常见问题

### 无法启动虚拟定位
- 检查LSPosed是否正确激活了模块
- 检查应用是否获得了必要的权限
- 检查设备系统版本是否在支持范围内

### 地图显示异常
- 检查网络连接是否正常
- 检查百度地图SDK是否正确配置
- 检查设备是否支持地图渲染

### 定位数据不准确
- 检查坐标系统是否正确选择
- 检查输入的经纬度是否准确
- 检查是否开启了坐标转换功能

## 致谢

感谢以下项目和开发者对本模块的启发和支持：

- [百度地图SDK](https://lbsyun.baidu.com/)
- [AndroidX](https://developer.android.com/jetpack/androidx)
- [Bugly](https://bugly.qq.com/)
- [OkHttp](https://square.github.io/okhttp/)
- [FastJson](https://github.com/alibaba/fastjson)