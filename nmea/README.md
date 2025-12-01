# NMEA Module

## 模块说明

NMEA模块是Portal项目的NMEA数据处理模块，负责生成和解析NMEA（National Marine Electronics Association）格式的GPS数据。该模块提供完整的NMEA语句生成、解析和验证功能，支持多种NMEA语句类型，为虚拟定位功能提供真实的GPS数据模拟。

## 功能特性

### NMEA语句生成
- **GGA语句**：全球定位系统固定数据语句生成
- **GLL语句**：地理定位系统位置数据语句生成
- **GSA语句**：GPS精度因子和活性卫星数据语句生成
- **GSV语句**：GPS卫星可见性数据语句生成
- **RMC语句**：推荐最小定位信息语句生成
- **VTG语句**：地面速度信息语句生成
- **ZDA语句**：日期和时间数据语句生成
- **HDT语句**：航向真数据语句生成

### NMEA语句解析
- **语句解析**：解析各种NMEA语句格式
- **数据提取**：提取语句中的定位、时间、速度等信息
- **格式验证**：验证NMEA语句的格式和校验和
- **错误处理**：处理格式错误和数据异常

### 其他功能
- **校验和计算**：计算和验证NMEA语句的校验和
- **语句格式化**：格式化NMEA语句，确保符合标准
- **坐标转换**：支持不同坐标系统间的转换
- **模拟数据生成**：生成逼真的模拟GPS数据

## 技术实现

### 架构设计
- **命令模式**：使用命令模式处理不同类型的NMEA语句
- **工厂模式**：使用工厂模式创建NMEA语句实例
- **观察者模式**：使用观察者模式监听NMEA数据变化
- **建造者模式**：使用建造者模式构建复杂的NMEA语句

### 核心组件

#### NMEA语句生成器
- **NmeaGenerator**：NMEA语句生成器基类
- **GgaGenerator**：GGA语句生成器
- **GllGenerator**：GLL语句生成器
- **GsaGenerator**：GSA语句生成器
- **GsvGenerator**：GSV语句生成器
- **RmcGenerator**：RMC语句生成器
- **VtgGenerator**：VTG语句生成器
- **ZdaGenerator**：ZDA语句生成器
- **HdtGenerator**：HDT语句生成器

#### NMEA语句解析器
- **NmeaParser**：NMEA语句解析器基类
- **GgaParser**：GGA语句解析器
- **GllParser**：GLL语句解析器
- **GsaParser**：GSA语句解析器
- **GsvParser**：GSV语句解析器
- **RmcParser**：RMC语句解析器
- **VtgParser**：VTG语句解析器
- **ZdaParser**：ZDA语句解析器
- **HdtParser**：HDT语句解析器

#### NMEA数据模型
- **NmeaData**：NMEA数据基类
- **GgaData**：GGA语句数据模型
- **GllData**：GLL语句数据模型
- **GsaData**：GSA语句数据模型
- **GsvData**：GSV语句数据模型
- **RmcData**：RMC语句数据模型
- **VtgData**：VTG语句数据模型
- **ZdaData**：ZDA语句数据模型
- **HdtData**：HDT语句数据模型

### 代码结构

```
nmea/src/main/
├── java/moe/fuqiuluo/portal/nmea/
│   ├── NmeaManager.kt              # NMEA管理器
│   ├── generator/                  # NMEA语句生成器
│   │   ├── NmeaGenerator.kt        # 生成器基类
│   │   ├── GgaGenerator.kt         # GGA语句生成器
│   │   ├── GllGenerator.kt         # GLL语句生成器
│   │   ├── GsaGenerator.kt         # GSA语句生成器
│   │   ├── GsvGenerator.kt         # GSV语句生成器
│   │   ├── RmcGenerator.kt         # RMC语句生成器
│   │   ├── VtgGenerator.kt         # VTG语句生成器
│   │   ├── ZdaGenerator.kt         # ZDA语句生成器
│   │   └── HdtGenerator.kt         # HDT语句生成器
│   ├── parser/                     # NMEA语句解析器
│   │   ├── NmeaParser.kt           # 解析器基类
│   │   ├── GgaParser.kt            # GGA语句解析器
│   │   ├── GllParser.kt            # GLL语句解析器
│   │   ├── GsaParser.kt            # GSA语句解析器
│   │   ├── GsvParser.kt            # GSV语句解析器
│   │   ├── RmcParser.kt            # RMC语句解析器
│   │   ├── VtgParser.kt            # VTG语句解析器
│   │   ├── ZdaParser.kt            # ZDA语句解析器
│   │   └── HdtParser.kt            # HDT语句解析器
│   ├── data/                       # NMEA数据模型
│   │   ├── NmeaData.kt             # 数据基类
│   │   ├── GgaData.kt              # GGA数据模型
│   │   ├── GllData.kt              # GLL数据模型
│   │   ├── GsaData.kt              # GSA数据模型
│   │   ├── GsvData.kt              # GSV数据模型
│   │   ├── RmcData.kt              # RMC数据模型
│   │   ├── VtgData.kt              # VTG数据模型
│   │   ├── ZdaData.kt              # ZDA数据模型
│   │   └── HdtData.kt              # HDT数据模型
│   └── utils/                      # 工具类
│       ├── NmeaUtils.kt            # NMEA工具类
│       ├── ChecksumUtils.kt        # 校验和工具类
│       └── CoordinateUtils.kt      # 坐标工具类
└── native/                         # 原生代码（可选）
    ├── jni/
    ├── cpp/
    └── CMakeLists.txt
```

## 支持的NMEA语句

| 语句类型 | 语句名 | 描述 |
|---------|-------|------|
| GGA | Global Positioning System Fix Data | 全球定位系统固定数据 |
| GLL | Geographic Position - Latitude/Longitude | 地理定位系统位置数据 |
| GSA | GPS DOP and Active Satellites | GPS精度因子和活性卫星数据 |
| GSV | GPS Satellites in View | GPS卫星可见性数据 |
| RMC | Recommended Minimum Navigation Information | 推荐最小定位信息 |
| VTG | Course Over Ground and Ground Speed | 地面速度信息 |
| ZDA | Time & Date - UTC, Day, Month, Year and Local Time Zone | 日期和时间数据 |
| HDT | Heading - True | 航向真数据 |

## 构建说明

### 依赖项
- Kotlin Standard Library
- Android SDK
- Android NDK (可选，用于JNI调用)

### 构建命令
```bash
# 构建nmea模块
./gradlew :nmea:build

# 构建包含nmea模块的完整APK
./gradlew assembleRelease
```

## 使用说明

### NMEA语句生成

```kotlin
// 创建NMEA管理器
val nmeaManager = NmeaManager()

// 设置位置信息
nmeaManager.setPosition(latitude = 39.9087, longitude = 116.3975)

// 设置时间信息
nmeaManager.setTime(System.currentTimeMillis())

// 设置速度信息
nmeaManager.setSpeed(speed = 10.5f)

// 设置航向信息
nmeaManager.setHeading(heading = 90.0f)

// 生成GGA语句
val gga = nmeaManager.generateGga()
println(gga) // $GPGGA,123456.789,3954.5222,N,11623.8500,E,1,8,1.0,100.0,M,10.0,M,,*5B

// 生成RMC语句
val rmc = nmeaManager.generateRmc()
println(rmc) // $GPRMC,123456.789,A,3954.5222,N,11623.8500,E,10.5,90.0,010123,0.0,E,A*6F

// 生成完整的NMEA数据序列
val nmeaData = nmeaManager.generateFullNmeaData()
for (sentence in nmeaData) {
    println(sentence)
}
```

### NMEA语句解析

```kotlin
// 创建NMEA解析器
val parser = NmeaParser()

// 解析GGA语句
val ggaSentence = "$GPGGA,123456.789,3954.5222,N,11623.8500,E,1,8,1.0,100.0,M,10.0,M,,*5B"
val ggaData = parser.parseGga(ggaSentence)
println("Latitude: ${ggaData.latitude}, Longitude: ${ggaData.longitude}")

// 解析RMC语句
val rmcSentence = "$GPRMC,123456.789,A,3954.5222,N,11623.8500,E,10.5,90.0,010123,0.0,E,A*6F"
val rmcData = parser.parseRmc(rmcSentence)
println("Speed: ${rmcData.speed}, Heading: ${rmcData.heading}")

// 解析任意NMEA语句
val anySentence = "$GPGLL,3954.5222,N,11623.8500,E,123456.789,A*43"
val result = parser.parse(anySentence)
when (result) {
    is GllData -> {
        println("GLL Data: ${result.latitude}, ${result.longitude}")
    }
    // 处理其他类型的解析结果
}
```

### 坐标转换

```kotlin
// 坐标转换工具
val coordUtils = CoordinateUtils()

// 转换经纬度格式（度分秒 -> 十进制度）
val latDms = "3954.5222"
val latDir = 'N'
val latDecimal = coordUtils.dmsToDecimal(latDms, latDir)
println("Latitude (decimal): $latDecimal") // 39.9087

// 转换经纬度格式（十进制度 -> 度分秒）
val latDecimal2 = 39.9087
val latDir2 = 'N'
val latDms2 = coordUtils.decimalToDms(latDecimal2, latDir2)
println("Latitude (DMS): $latDms2") // 3954.5222
```

## 注意事项

### 性能影响
- 频繁生成NMEA语句可能会对性能产生影响
- 建议批量生成和处理NMEA语句
- 避免在UI线程中执行大量NMEA数据处理

### 精度问题
- NMEA语句的精度受输入数据精度的限制
- 模拟数据的逼真程度取决于输入参数的合理性
- 建议使用真实的GPS数据作为参考来调整模拟参数

### 格式兼容性
- 不同的GPS设备可能对NMEA语句格式有细微差异
- 某些设备可能只支持部分NMEA语句类型
- 建议在使用前测试目标设备对NMEA语句的兼容性

## 常见问题

### 生成的NMEA语句格式不正确
- 检查输入参数是否有效
- 验证校验和计算是否正确
- 确保语句格式符合NMEA标准

### 解析NMEA语句失败
- 检查语句格式是否正确
- 验证校验和是否匹配
- 确保语句类型被支持

### 模拟数据不逼真
- 调整位置、速度、航向等参数的变化率
- 添加适当的随机噪声
- 参考真实GPS数据的变化模式

## 致谢

感谢以下资源和标准对本模块的启发和支持：

- [NMEA 0183 Standard](https://www.nmea.org/)
- [GPS NMEA Sentence Information](http://aprs.gids.nl/nmea/)
- [NMEA Message Formats](https://www.trimble.com/oem_receiverhelp/v4.44/en/nmea-0183messages.html)