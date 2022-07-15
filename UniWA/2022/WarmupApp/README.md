# WarmupApp 

Mobile, Very Easy, 200 Points 🗡️🩸First Blood🩸🗡️

>  A new game is released, but not everyone are allowed to play. Can you get the access code? 

## Analysis

Decompiled the [WarmupApp.apk](WarmupApp.apk) with JADX:

First step, we go to **Resources** > **AndroidManifest.xml** to find the location of MainActivity

```xml
<activity android:name="com.example.warmupapp.MainActivity" android:exported="true">
```

`class MainActivity`:
```java
...
button.setOnClickListener(new View.OnClickListener() { // from class: com.example.warmupapp.MainActivity.1
    @Override // android.view.View.OnClickListener
    public void onClick(View view) {
        if (MainActivity.this.isUser) {
            Toast.makeText(MainActivity.this, "UNIWA{w4rm1ng_my_4pp_up!!}", 0).show();
        } else {
            Toast.makeText(MainActivity.this, "I can see your face through the camera. You are not chosen to play this game.", 0).show();
        }
    }
});
...
```

## Solution

That was it, we can clearly see the flag in plain text in MainActivity

```
UNIWA{w4rm1ng_my_4pp_up!!}
```