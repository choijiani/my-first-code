# my-first-code

## Overview

This repository demonstrates a very small bootable program for x86 machines. The `boot.asm` file assembles into a boot sector that prints a message when run under an emulator like QEMU or on real hardware.

## Building

You will need `nasm` to assemble the boot sector.

```bash
nasm -f bin boot.asm -o boot.img
```

The resulting `boot.img` can be booted directly by QEMU:

```bash
qemu-system-x86_64 -drive format=raw,file=boot.img
```

This will display the text `Hello, OS!` on the screen.
