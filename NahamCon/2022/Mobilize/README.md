# Mobilize

Mobile, Easy, 50 Points

> Autobots. ROLLL OUTTT!!!!! 

## Analysis

I extracted the files from the [mobilize.apk](mobilize.apk)
```
apktool -d mobilize.apk
```

Looked up at strings resources first

## Flag

```xml
<!-- File: mobilize/res/values/strings.xml -->
<string name="flag">flag{e2e7fd4a43e93ea679d38561fa982682}</string>
```