# 配置参数 | Mao Wiki

Game-其他游戏菜单教程CS2Midnight 午夜配置参数
配置参数
调优
​

此处只讲在 Trusted mode 模式下，Trusted mode 关闭时可使用一些较为暴力的功能，在这里将不讲解 (Trusted mode 位于 Misc 项 Main 模块)

我大概将绿演的参数分为三类，分别是

1. 小范围快速拉枪 - 适合稍微有 fps 基础的

2. 较大范围中速拉 - 适合打不准，甚至准星没有办法对准到敌人周围

3. 快捷键大范围速拉 - 对枪时按快捷键来大范围快速瞄准敌人

我个人更喜欢用第一种，十分舒适且可以看起来更加合法

既然已经知道了我想要的效果，接下来只需要慢慢调整即可，首先来到全局设置，我将会把自瞄绑定为鼠标侧键5，这是我的鼠标按键图:

由于我需要更好的演技，所以我选择开启 Disable aimbot while flashed 和 Disable aimbot though smoke

我不希望杀死一个敌人后需要等非常久的事件才会再次激活自瞄，所以我选择把 Kill delay 调整到 0.35，太低则会导致非人类一般的拉枪速度

由于我希望高速拉并且基本是点头，所以为了避免我手抖，将 Mouse lock percentage x 与Mouse lock percentage y 调整为 0.5，防止由于手抖打乱自瞄导致看起来十分奇怪

我需要自动压枪来帮我保证扫射时的准度，所以开启 Recoil 但不调整具体参数，因为我觉得默认参数已经十分够用了

另外，我可能需要用到 Triggerbot 架点，有可能是 AWP，所以为了配合演技开启 Disable aimbot while flashed 和 Disable aimbot though smoke，并更改按键为鼠标按键4

接下来转到 WEAPON 项，选择AK47 调整 AK 的具体参数

前面说过了，我希望 AK 更多是点头，所以 Hitboxes 我只选择 Head

为了防止我的自瞄速度过快，在玩家跳的时候准星跟着起飞，所以我选择开启 Ignore jump

同时还是一样，为了防止速度过快，我不希望准星是动态调整的，这样会让我不适应，而且很奇怪的以非人类速度拉到很远的敌人，所以 Fov type 为 Static，Smooth type 为 Constant

AK 我并不需要 Triggerbot，我选择关闭

我希望小范围调整，我只要瞄准到敌人碰撞箱周围即可，甚至直接鼠标甩过去，所以我将 Fov调整到 1.5，如图

因为是小范围快速拉枪，我希望可以有较快的速度，但太快会导致直接锁住产生奇怪的感觉，所以测试后我认为 16.5 最适合我，Smooth 16.5

接下来需要调整扫射，我希望扫射可以在我第一发后进行，并且范围适中，速度不需要太快，测试后我认为 Recoil FOV 2.5，Recoil Smooth 25，Recoil Start 1，最适合我

扫射看起来一切正常，所以我不需要调整 Recoil X/Y Axis

我不需要在多少发子弹后关闭 Aimbot，所以选择将 Aimbot Stop 拉满

调整完成，在实战中我只需要在合适的时机按住侧键，急停，直接把鼠标甩过去，准了后左键，一气呵成，并且看起来十分帅且合法

Visuals

视觉类不过多讲解，需要注意的是，在ESP Preview 内我们可以通过拖拽元素来调整自己喜欢的布局，并且可以右键选择方框种类与颜色

另外，我不希望屏幕周围有白色箭头提示我屏幕外的敌人，所以我选择关闭 offscreen，同时默认配置的人物染色会让我感觉很奇怪，所以我选择关闭 Chams 功能

Chams

Visible - 对可见人物进行染色

Invisible - 对不可见人物进行染色

Type 可自行测试，Bloom 为发光

Hud

Aim target hitbox - 显示瞄准的碰撞箱位置

Aim recoil dot - 显示子弹落点

Aim FOV - 显示 Aimbot 范围

Sniper crosshair - 使用狙时显示辅助十字准星

Remove smoke - 消除烟雾

Bind list - 显示快捷键使用情况

Spectator list - 显示观战你的人

Rador - 雷达

In-game 在游戏内显示

Show bomb - 显示炸弹

Scale - 大小

Alpha - 雷达背景颜色深度

云保存提醒

需要注意，在使用 Cloud，云功能时，创建新的配置并不会自动保存你现有的配置到这个新配置中，大坑