# Peanutbutter

Forensics, Hard, 500 Points

> Gary was setting up a challenge, ... I think?

## Analysis

I extracted the files from the `peanutbutter.zip`. It contained a `peanutbutter.elf` which was 2.1GiB size.

I extracted strings from from peanutbutter.elf
```
➜ peanutbutter strings peanutbutter.elf > peanutbutter.txt
```

Then looked for a while and found the line
```
echo Z2l0IGNsb25lIGh0dHBzOi8vb2F1dGgyOmdscGF0LWpXQmdDUnR0WkdneHN0R3hOYjVyQGdpdGxhYi5jb20vY3RmZmxhZzEzMzcvc3NoLXZvbC5naXQK | base64 -d | sh 2&> /dev/null
```

Decoded Base64
```console
➜ peanutbutter echo Z2l0IGNsb25lIGh0dHBzOi8vb2F1dGgyOmdscGF0LWpXQmdDUnR0WkdneHN0R3hOYjVyQGdpdGxhYi5jb20vY3RmZmxhZzEzMzcvc3NoLXZvbC5naXQK | base64 -d
git clone https://oauth2:glpat-jWBgCRttZGgxstGxNb5r@gitlab.com/ctfflag1337/ssh-vol.git
```

If we clone the repository it contains a file named `flag.txt`

## Flag

```console
➜ peanutbutter cat ssh-vol/flag.txt
flag{698789979201a0ae066ce0f780f1a751}
```