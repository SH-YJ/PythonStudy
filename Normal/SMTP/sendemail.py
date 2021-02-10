import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import random, string

sender = '2973211152@qq.com'  # 发件人邮箱账号
password = 'udrswmyafeavdfhj'  # 邮箱授权码
receiver = '253480035@qq.com'  # 收件人邮箱账号


def mail():
    ret = True
    ver_code = ''.join(random.sample(string.digits + string.ascii_letters, 6))  # 随机验证码
    content = '<p><h3>您的验证码为：</h3></p></p><h1>{}</h1></p>'.format(ver_code)
    try:
        msg = MIMEText(content, 'html', 'utf-8')  # # 第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        msg['From'] = formataddr(("SH_YJ", sender))  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(("FK", receiver))  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "注册账号 邮箱验证！"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, [receiver, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:
        ret = False
    return ret,ver_code


ret, code = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")