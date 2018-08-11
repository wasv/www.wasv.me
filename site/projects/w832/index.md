title: w832
description: Learning how emulators and assemblers work with a fictional architecture.
template: template.html
siteroot: ../..
image: /img/w832.png

---

# w832
Learning how emulators and assemblers work with a fictional architecture.

![Sreenshot of code for w832](w832_code.png){class="primary" style="width:80%;display:block;"}

<i class="fa fa-gitlab"></i> Code: <a target="_blank" href="https://gitlab.com/wasv/w832">wasv/w832</a>

I spent some time this past summer and spring working on learning the basics of designing an instruction set.
I didn't formally learn these topics for a year or two in my college.
However, I found myself with enough time to design an emulator and assembler for a fictional
instruction set that I designed based on the architecture of the
[Manchester SSEM](https://en.wikipedia.org/wiki/Manchester_Small-Scale_Experimental_Machine){target="\_blank"}
The instruction set is named W832, short for "WASV's 8-bit, 32-address Instruction Set".

The process of deciding on an architecture was essentially a really long [Wikipeida Rabbit Hole](https://www.xkcd.com/214){target="\_blank"}
ranging from [orthogonality](https://en.wikipedia.org/wiki/Orthogonal_instruction_set){target="\_blank"}
to [one instruction set architectures](https://en.wikipedia.org/wiki/One_instruction_set_computer){target="\_blank"}.
The one instruction architectures were very useful to look at as an example of the bare minimum needed for a useful instruction set.
Eventually I got my instruction set down to 8 instructions, leaving 5 bits to address 32 bytes of memory.
I might also make a W816 instruction set with support for immediate operands, however this would reduce the address bits to 4, leaving only 16 bytes to address memory.

I also have a JavaScript emulator for a different architecture, [C1616](https://gitlab.com/wasv/c1616-js){target="\_blank"}.
C1616 is an extension of Daniel Bailey's [C88](https://github.com/danieljabailey/C88){target="\_blank"}, which was also based on the SSEM.
I've found that either W832 or C88 can be useful in learning the basics programming in an assembly language, without the need to have dedicated hardware.
