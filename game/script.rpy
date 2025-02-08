# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define aside = Character(
    None,

    what_size=48,
    what_xalign=0.5,
    what_textalign=0.5,
    what_layout='subtitle')

# Colton Reid k
define k = Character(
    _("Colton"),
)

# Alya Sinclair i
define i = Character(
    _("Alya")
)

# Averill Crowe 奥维尔
define ao = Character(
    _("Averill")
)

define l = Character(
    _("linxia")
)
 

# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bg cafe

    #play music "audio/days_in_bambootown.mp3"

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    show linxia idle :
        xalign 0.25
        yalign 1.0

    # 此处显示各行对话。

    aside "黄昏，咖啡店内"

    l "（擦着咖啡杯微笑）"
    k "你说这里的黄昏藏着秘密，我很好奇，你指的是什么？"
    i "秘密是需要有缘人才能看到的。我可以告诉你，但你确定自己想知道？"
    k "为什么不？既然来到这里，我总要弄清楚这个地方的特别之处。"
    i "特别之处不仅在落日，也在那些从未被人提及的往事。这里的人，都有意无意地忘记了一些事情。"
    k "忘记？还是故意不提？"
    i "也许两者皆有。你刚来，等你待久了，会明白的。不过，画家先生，你的画里似乎也藏着自己的故事。"
    k "画能表达的，未必是故事，可能只是片段。"
    i "那片段里，有你不想面对的过去吗？"

    return

