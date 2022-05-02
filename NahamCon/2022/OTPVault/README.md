# OTPVault

Mobile, Medium, 402 Points

> I created my own vault application to store my secrets. It uses OTP to unlock the vault so no one can steal my password!

## Analysis

I extracted the files from the [OTPVault.apk](OTPVault.apk)
```
apktool -d OTPVault.apk
```

I looked at assets and i ding ding we have a react native challenge.

Got `index.android.bundle` and searched for `OTP` and found the part of the unlock.

```js
// File: OTPVault/assets/index.android.bundle
function O () {
    var n
    ;(0, e.default)(this, O)
    for (var o = arguments.length, u = new Array(o), l = 0; l < o; l++)
    u[l] = arguments[l]
    return (
    ((n = b.call.apply(b, [this].concat(u))).state = {
        output: 'Insert your OTP to unlock your vault',
        text: ''
    }),
    (n.s = 'JJ2XG5CIMFRWW2LOM4'),
    (n.url = 'http://congon4tor.com:7777'),
    (n.token = '652W8NxdsHFTorqLXgo='),
    (n.getFlag = function () {
        var e, o
        return t.default.async(
        function (u) {
            for (;;)
            switch ((u.prev = u.next)) {
                case 0:
                return (
                    (u.prev = 0),
                    (e = {
                    headers: {
                        Authorization:
                        'Bearer KMGQ0YTYgIMTk5Mjc2NzZY4OMjJlNzAC0WU2DgiYzE41ZDwN'
                    }
                    }),
                    (u.next = 4),
                    t.default.awrap(p.default.get(n.url + '/flag', e))
                )
                case 4:
                ;(o = u.sent),
                    n.setState({ output: o.data.flag }),
                    (u.next = 12)
                break
                case 8:
                ;(u.prev = 8),
                    (u.t0 = u.catch(0)),
                    console.log(u.t0),
                    n.setState({
                    output: 'An error occurred getting the flag'
                    })
                case 12:
                case 'end':
                return u.stop()
            }
        },
        null,
        null,
        [[0, 8]],
        Promise
        )
    }),
    (n.onChangeText = function (t) {
        n.setState({ text: t })
    }),
    (n.onPress = function () {
        var t = (0, s.default)(n.s)
        console.log(t),
        t === n.state.text
            ? n.getFlag()
            : n.setState({ output: 'Invalid OTP' })
    }),
    n
    )
}
```

## Flag

Then i requested from the server the flag using the credentials we got from the app

```console
➜ ~ curl -H "Authorization: Bearer KMGQ0YTYgIMTk5Mjc2NzZY4OMjJlNzAC0WU2DgiYzE41ZDwN" http://congon4tor.com:7777/flag
{"flag":"flag{5450384e093a0444e6d3d39795dd7ddd}"}

```