# ezSubstitution

> You have received a weird message from your lecturer, saying that it is a hint for the upcoming exam.

### Files

- [challenge.txt](challenge.txt)

## Description

Challenge gives a [text file](challenge.txt) containing a ciphertext which contains the flag.

## Solution

The challenge title said "substitution", so it must be a form of substitution cipher. Trying ROT13 in CyberChef didn't work, so I went and paste the text in an online [substitution solver](https://www.guballa.de/substitution-solver), which yielded the flag.

Input:
```
Cxetgoaslelzn Appgpprgtz lp a tyt-ltzoxplcg auuoyadk zkaz pgocgp zy uoyfxdg a uolyolzlpgf elpz yh pgdxolzn cxetgoaslelzlgp. A dyrsltazlyt yh axzyrazgf atf ratxae pdat ran sg ugohyorgf yt zkg yojatlpazlyt’p LZ pnpzgrp yo tgzvyow, zy lfgtzlhn heavp zkaz ran sg gbueylzgf fxoltj at azzadw. Zkg pnpzgrazld auuoyadk yh lfgtzlhnltj, ixatzlhnltj, atf oatwltj pgdxolzn cxetgoaslelzlgp gtasegp yojatlpazlyt zy pgegdz dolzldae cxetgoaslelzlgp zy ogpyecg sapgf yt zkglo acaleaseg ogpyxodgp. Vlzkyxz pxdk appgpprgtzp, zkgog lp a olpw zkaz LZ lthoapzoxdzxog aog tyz pxhhldlgtzen pgdxogf. Lz lp ogdyrrgtfgf zkaz yojatlpazlytp pkyxef ugohyor a cxetgoaslelzn appgpprgtz yt zkglo LZ lthoapzoxdzxog yt a ixaozgoen saplp, atf ap vgee ap zy appgpp zkglo auueldazlytp yt a ngaoen saplp.



Ugtgzoazlyt Zgpzltj yt zkg yzkgo katf, xpgp at ltzoxplcg auuoyadk zy flpdycgo pgdxolzn vgawtgppgp lt zkg yojatlpazlyt’p LZ lthoapzoxdzxog atf auueldazlytp. Ugtgzoazlyt zgpzgop vyxef azzgruz zy gbueylz lfgtzlhlgf pgdxolzn vgawtgppgp zy jalt uolclegjgf addgpp ltzy zkg LZ lthoapzoxdzxog atf auueldazlytp. Pxdk auuoyadk grxeazgp a ogae azzadw, atf vyxef fgzgorltg zkg oysxpztgpp yh zkg yojatlpazlyt’p LZ lthoapzoxdzxog lt uoyzgdzltj pgtplzlcg lthyorazlyt.

HEAJ{aTaENmLtJ_pXspZlZxzLyT_dLuk3o}
```

Output:
```
Substitution Key: asdfghjklqwertyuiopzxcvbnm
```
```
Vulnerability Assessment is a non-intrusive approach that serves to produce a prioritised list of security vulnerabilities. A combination of automated and manual scan may be performed on the organisation’s IT systems or network, to identify flaws that may be exploited during an attack. The systematic approach of identifying, quantifying, and ranking security vulnerabilities enables organisation to select critical vulnerabilities to resolve based on their available resources. Without such assessments, there is a risk that IT infrastructure are not sufficiently secured. It is recommended that organisations should perform a vulnerability assessment on their IT infrastructure on a quarterly basis, and as well as to assess their applications on a yearly basis.



Penetration Testing on the other hand, uses an intrusive approach to discover security weaknesses in the organisation’s IT infrastructure and applications. Penetration testers would attempt to exploit identified security weaknesses to gain privileged access into the IT infrastructure and applications. Such approach emulates a real attack, and would determine the robustness of the organisation’s IT infrastructure in protecting sensitive information.

FLAG{aNaLYzInG_sUbsTiTutIoN_cIph3r}
```

Flag Captured: `FLAG{aNaLYzInG_sUbsTiTutIoN_cIph3r}`
