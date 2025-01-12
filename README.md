# [点击获取PikaScript v0.6.0](https://github.com/mimilib/pikascript/releases/download/v0.6.0/pikascript-v0.6.0.zip)

# 1.简介
PikaScript可以为资源受限的mcu提供极易部署和拓展的Python脚本绑定。

支持裸机运行，可运行于 ***RAM > 4kB*** 的mcu中，如stm32f103c8t6，esp32。

使用python3标准语法的子集。

在编译时支持python类和方法定义(基于[Pika预编译器](../../tree/master/pikascript-compiler-rust))。

在运行时支持python方法调用、变量定义、对象构造、对象释放(基于[Pika运行时内核](../../tree/master/src/package/pikascript/pikascript-core))。

支持跨平台，可在linux环境开发、测试内核。

开箱即用，零配置，仅依赖C标准库，完全不使用宏，几乎不使用全局变量。

完整的googletest单元测试。

栈空间少量占用，内存信息可观测。

源码命名规范，可读性强。


## stm32例程
[pikascript-stm32-demo](../../tree/master/demo)

## 开发手册
[1. PikaScript-三分钟快速上手](doc/1.三分钟快速上手.md)

[2. PikaScript-架构与原理](https://mp.weixin.qq.com/s?__biz=MzU4NzUzMDc1OA==&mid=2247484127&idx=1&sn=f66cff49c488e48c52570c7bb570328f&chksm=fdebd5b6ca9c5ca0707fd221c32f3ad63e94aeb6f917a92774b89ea042381ea261990f5cca3c&token=2045971639&lang=zh_CN#rd)

[3. PikaScript-十分钟快速部署](doc/2.十分钟快速部署.md)

[4. PikaScript-标准开发流程](doc/3.PikaScript标准开发流程.md)

## 架构示意图
![K9C)%CZO)X`8VFBKCE8(9@W](https://user-images.githubusercontent.com/88232613/127806449-b476b2fd-9f40-4c53-94a0-e1e965c046c3.png)

# 2.stm32教程视频

[手把手PikaScript教程合集](https://www.bilibili.com/video/BV1mg411L72e)

# 3.交流与技术支持：

## 微信交流群
![image](https://user-images.githubusercontent.com/88232613/131966892-59d89b0c-8068-488a-9015-f1002fa18505.png)

## 官方公众号
![image](https://user-images.githubusercontent.com/88232613/128301451-f0cdecea-6457-4925-b084-42e7796a856e.png)

## Tencent QQ： 645275593

## E-mail: 645275593@qq.com

# 4.内核测试与开发

## linux下测试pikascript内核(推荐ubuntu20.04)：

step1: 拉取项目
``` shell
git clone https://github.com/mimilib/pikascript
cd pikascript
```

step2: 编译项目
```
sh init.sh # 第一次编译前运行，之后就不用运行了 
sh make.sh # 编译项目
```

step3: 运行单元测试
``` shell	
sh test
```

step4: 运行基准测试
``` shell
sh test-banchmark
```

step5: 运行demo
``` shell
./build/src/boot/demo06-pikamain/pikascript_demo06-pikamain
```

step6: 提交修改
``` shell
sh commit.sh
```
