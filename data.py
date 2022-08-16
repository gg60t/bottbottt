from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("استخراج كود تيرمكس 💂", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 العوده الى الصفحة الرئيسية", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("✨ لتنصيب سورس ايكثون", url="https://t.me/ICTHON")],
        [
            InlineKeyboardButton("طـريـقـة الـإسـتخـدام ❔", callback_data="help"),
            InlineKeyboardButton(" حـول ", callback_data="about")
        ],
        [InlineKeyboardButton("🖥️|قناة الـسـورس", url="https://t.me/ICTHON")],
    ]

    START = """
اهلا {}

مرحبًا في {}

هذا بوت استخراج كود تريمكس وبايروجرام, 
اولأ قم بإرسال الايبي ايدي والايبي هاش 
وبعد ذلك رقم الهاتف الخاص بك وسـيصـلك كود 

لا أزال أقرأ؟
يمكنك استخدامي لإنشاء pyrogram (حتى الإصدار 2) وجلسة ICTHON string. استخدم الأزرار أدناه لمعرفة المزيد!

By @ICTHON
    """

    HELP = """
✨ **الأوامر المنوفرة** ✨

/about - حول هذا البوت
/help - معرفة الاوامر
/start - بدء هذا البوت 
/generate - بدء استخراج الجلسة 
/cancel - إلغاء
/restart - إعادة تشغيل البوت 
"""

    ABOUT = """
**About This Bot** 

هذا بوت استخراج كود تريمكس و بايروجرام مشغل من @ICTHON

المطور : [Click Here](https://t.me/BEEEB5)

برمجة البوت : [Pyrogram](https://docs.pyrogram.org)

لغة البوت : [Python](https://www.python.org)

قناة المطور : @ICTHON
    """
