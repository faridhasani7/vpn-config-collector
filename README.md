# Configuration of VPN

```markdown
config_downloader.py / دانلود کننده کانفیگ وی‌پی‌ان

## معرفی / Introduction

فارسی:
این اسکریپت پایتون، کانفیگ‌های وی‌پی‌ان مثل vmess، vless و ss رو از منبع آنلاین دانلود می‌کنه و در فایل‌های متنی داخل پوشه Configs/ ذخیره می‌کنه. به زبان ساده، با این برنامه می‌تونی به راحتی کانفیگ‌های وی‌پی‌ان مورد نظر رو جمع‌آوری کنی.

English:
This Python script downloads VPN configurations such as vmess, vless, and ss from an online source and saves them in text files inside the **Configs/** folder. In simple terms, it helps you easily collect the VPN configs you need.

## ساختار فایل‌ها / File Structure


vpn-config-collector/
├── Configs/
│   ├── vmess.txt      # Stores vmess configs
│   ├── vless.txt      # Stores vless configs
│   └── ss.txt         # Stores shadowsocks configs
├── config_downloader.py # Main script for downloading VPN configs
└── requirements.txt   # Dependencies needed for the script
```

## نصب و اجرا / Installation & Usage

## نصب وابستگی‌ها / Installing Dependencies

```bash
pip install -r requirements.txt
```

## اجرای اسکریپت / Running the Script

برای اجرای اسکریپت کافیست این دستور رو وارد کنی:
```bash
python config_downloader.py
```
## نکات تکمیلی / Additional Notes

- مطمئن شو پوشه Configs/ کنار فایل‌های اصلی موجود باشه، چون خروجی‌ها توی همون پوشه ذخیره می‌شن.
- در صورت بروز مشکل یا سوال، می‌تونی به قسمت Issues ریپازیتوری مراجعه کنی.

مشارکت / Contributing

اگر ایده یا پیشنهادی برای بهبود این اسکریپت داری، خوشحال می‌شیم از طریق Issues یا Pull Request با ما در میان بذاری.

## مجوز / License

این اسکریپت تحت مجوز MIT منتشر شده است.  
This script is released under the MIT License.
```
