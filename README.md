# my-first-code
첫 저장소

## Simple Bootloader

This repository includes a tiny boot sector written in assembly. It prints
"Hello, world!" when executed in a PC emulator.

### Building

```
make boot.bin
```

This uses `nasm` to assemble `boot.asm` into `boot.bin`.

### Running (with QEMU)

```
qemu-system-x86_64 -drive format=raw,file=boot.bin
```

This requires `qemu-system-x86_64` to be installed.
