# REFS

该项目用于挂钩Android系统组件，需要参考不同版本Android源代码的实现。它旨在方便维护兼容多个Android版本的接口。

## 项目结构

项目按Android版本号组织，每个目录包含该特定版本所需的AIDL文件和文档：

```
refs/
├── 7.0.0_r1/
│   ├── IGnssStatusListener.aidl
│   ├── ILocationManager.aidl
│   └── README.md
├── 7.1.1_r6/
│   ├── ILocationManager.aidl
│   └── README.md
├── 8.0.0_r4/
│   ├── ILocationManager.aidl
│   └── README.md
├── 9.0.0_r3/
│   ├── ILocationManager.aidl
│   └── README.md
├── 10.0.0/
│   └── README.md
├── 11.0.0/
│   └── README.md
├── 12.0.0/
│   └── README.md
├── 13.0.0/
│   └── README.md
├── 14.0.0/
│   └── README.md
└── 15.0.0/
    └── README.md
```

## 目录命名约定

- Android 7.0.0 至 9.0.0：使用完整的Android版本标签格式（例如：`7.0.0_r1`）
- Android 10.0.0 及以上：使用简化的版本号格式（例如：`10.0.0`）

## 内容说明

每个版本目录包含：

1. **AIDL文件**：Android系统服务的接口定义文件（例如：`ILocationManager.aidl`、`IGnssStatusListener.aidl`）
2. **README.md**：包含该版本官方Android源代码链接的文档

## 使用方法

1. 根据目标设备导航到相应的Android版本目录
2. 参考AIDL文件获取您需要挂钩的系统服务接口
3. 使用README.md中的链接访问官方源代码以获取更多上下文
4. 根据版本之间的差异实现兼容层

## 目的

该仓库作为多个版本Android系统服务接口的集中参考，使开发者能够：
- 维护不同Android版本之间的兼容性
- 实现可在各种设备上可靠工作的系统挂钩
- 及时了解Android系统API的变化
- 减少在单个项目中支持多个Android版本所需的工作量

## 注意事项

- 早期版本（7.0.0_r1）使用androidxref.com链接作为源代码参考
- 较新版本（10.0.0+）使用android.googlesource.com链接作为源代码参考
- 实现挂钩前请务必验证接口的兼容性
- 有关系统服务的更多信息，请参考官方Android文档