# Jelly

Forensics, Hard, 500 Points

> It gets real sticky when you're walking kernel structs... 

## Analysis

I extracted the files from the `jelly.zip`. It contained a `jelly.elf` which was 2.5GiB size.

I extracted strings from from jelly.elf
```
➜ jelly strings jelly.elf > jelly.txt
```

Then looked for a while and found the line
```
echo "bitcoin: G9mzcaHrPAZnkfMCgsNrt5Y8VXSfV74E2kNhYeaWgPYCrtNDzZzC" > flag.txt
```

We know Bitcoin addresses are written base58 and start with 0x80

## Flag

Decoded the hash

```console
➜ jelly echo G9mzcaHrPAZnkfMCgsNrt5Y8VXSfV74E2kNhYeaWgPYCrtNDzZzC | base58 -d
flag{a70f5c001e67e4c26bf20dc457d43459}
```