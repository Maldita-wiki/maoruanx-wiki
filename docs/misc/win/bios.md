---
sidebar_position: 1
title: éè¦å¯ç¨ JavaScript
slug: /misc/win/bios
---

<article><div class="theme-doc-markdown markdown"><header><h1>BIOS ä¸ç³»ç»è®¾ç½®</h1></header>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="preface">åçè¿é<a aria-label="åçè¿éçç´æ¥é¾æ¥" class="hash-link" href="#preface" title="åçè¿éçç´æ¥é¾æ¥" translate="no">â</a></h2>
<p><strong>åªæ¹äº§åæç¡®è¦æ±çé¡¹ç®ã</strong> æ¬é¡µä¸æ¯âå¨é¨ç§åâçæ¸åï¼å·²ç»ç¬¦åè¦æ±çè®¾ç½®ä¸ç¨æ¹ã</p>
<p>BIOS çé¢å ä¸»æ¿åå·åçæ¬èå¼ãæ¾ä¸å°éé¡¹æ¶ï¼æ¥ä¸»æ¿å®æ¹è¯´æä¹¦ï¼ä¸è¦å°è¯åå­ç¸è¿çå¼å³ã</p>
<div class="theme-admonition theme-admonition-warning admonition_LJt0 alert alert--warning"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 16 16"><path d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z" fill-rule="evenodd"></path></svg></span>ä¿®æ¹ååå¤</div><div class="admonitionContent__XZN"><p>è®°å½åè®¾ç½®ãæ¶å Secure BootãTPM æå¯å¨æ¨¡å¼æ¶ï¼åä¿å­ BitLocker æ¢å¤å¯é¥ï¼å¯ç¨äº BitLocker ççµèï¼è¿éæå®æ¹æå¼æåä¿æ¤ãç£çè½¬æ¢åå¦åå®æ´æ°æ®å¤ä»½ã</p></div></div>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="bios-entry-keys">ææ ·è¿å¥ BIOS<a aria-label="ææ ·è¿å¥ BIOSçç´æ¥é¾æ¥" class="hash-link" href="#bios-entry-keys" title="ææ ·è¿å¥ BIOSçç´æ¥é¾æ¥" translate="no">â</a></h2>
<details class="details_B75C details_r1OI" data-collapsed="true"><summary>æ¥çå¸¸è§ä¸»æ¿çå¼æºæé®</summary><div><div class="collapsibleContent_vi_q"><p>å¼æºåç«å³è¿ç»­ç¹æï¼ç´å°è¿å¥ BIOS / UEFI è®¾ç½®ãä¸æ¯éæ©å¯å¨çç Boot Menuã<ul>
<li class=""><strong>åç¡</strong>ï¼<code>Del</code> æ <code>F2</code>ã</li>
<li class=""><strong>å¾®æãæåãé­çãä¸å½©è¹</strong>ï¼éå¸¸ä¸º <code>Del</code>ã</li>
<li class=""><strong>åæ</strong>ï¼<code>F2</code> æ <code>Del</code>ã</li>
</ul><p>æé®æ ææ¶ï¼ä»¥è¯¥åå·çå®æ¹è¯´æä¹¦ä¸ºåãç¬è®°æ¬ååçæ´æºä¸ä¸å®ä½¿ç¨ä¸è¿°æé®ã</p></p></div></div></details>
<details class="details_B75C details_r1OI" data-collapsed="true"><summary>æ¥ä¸åæé®ï¼ä» Windows è¿å¥ UEFI</summary><div><div class="collapsibleContent_vi_q"><p>åä¿å­å·¥ä½ï¼åæå¼ï¼<ul>
<li class=""><strong>Windows 11</strong>ï¼è®¾ç½® â ç³»ç» â æ¢å¤ â é«çº§å¯å¨ â ç«å³éå¯ã</li>
<li class=""><strong>Windows 10</strong>ï¼è®¾ç½® â æ´æ°åå®å¨ â æ¢å¤ â é«çº§å¯å¨ â ç«å³éæ°å¯å¨ã</li>
</ul><p>éå¯åéæ© <strong>çé¾è§£ç­ â é«çº§éé¡¹ â UEFI åºä»¶è®¾ç½® â éå¯</strong>ã<p>æ²¡æâUEFI åºä»¶è®¾ç½®âæ¶ï¼æ¹ç¨ä¸»æ¿çå¼æºæé®ï¼ä¸è¦ä¸ºæ¾ç¤ºè¿ä¸ªæé®åæ¹å¯å¨æ¨¡å¼ã</p></p></p></div></div></details>
<p>ä¸ç¥éä¸»æ¿åå·ï¼å¨ PowerShell æ§è¡ï¼</p>
<div class="language-powershell codeBlockContainer_Y94m theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_IRmN"><pre class="prism-code language-powershell codeBlock_rbdZ thin-scrollbar" style="color:#393A34;background-color:#f6f8fa" tabindex="0"><code class="codeBlockLines_bJRA"><div class="token-line" style="color:#393A34"><span class="token plain">Get-CimInstance Win32_BaseBoard | Select-Object Manufacturer, Product</span><br/></div></code></pre></div></div>
<p><code>Manufacturer</code> æ¯ååï¼<code>Product</code> æ¯åå·ãåé¢ç BIOS æä½é½ä»æ¬èè¿å¥ï¼ä¸åéå¤è¯´æã</p>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="disable-fast-startupv">å³é­å¿«éå¯å¨<a aria-label="å³é­å¿«éå¯å¨çç´æ¥é¾æ¥" class="hash-link" href="#disable-fast-startupv" title="å³é­å¿«éå¯å¨çç´æ¥é¾æ¥" translate="no">â</a></h2>
<p>åªå³é­å¿«éå¯å¨ï¼å¯æ<a class="" href="/misc/win/quickstart/">çµæºè®¾ç½®æç¨</a>æä½ã</p>
<p>å¦æäº§ååæ¶è¦æ±å³é­ä¼ç ï¼ä»¥ç®¡çåèº«ä»½æå¼ PowerShellï¼æ§è¡ï¼</p>
<div class="language-powershell codeBlockContainer_Y94m theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_IRmN"><pre class="prism-code language-powershell codeBlock_rbdZ thin-scrollbar" style="color:#393A34;background-color:#f6f8fa" tabindex="0"><code class="codeBlockLines_bJRA"><div class="token-line" style="color:#393A34"><span class="token plain">powercfg /h off</span><br/></div></code></pre></div></div>
<p>éå¯åæµè¯ã<strong>è¿æ¡å½ä»¤ä¹ä¼å³é­ä¼ç ï¼ä¸åªæ¯å¿«éå¯å¨ã</strong></p>
<p>éè¦æ¢å¤ä¼ç æ¶æ§è¡ <code>powercfg /h on</code>ï¼å¿«éå¯å¨æ¯å¦å¯ç¨ï¼åå°çµæºè®¾ç½®ç¡®è®¤ã</p>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="disable-secure-boot">å³é­å®å¨å¯å¨<a aria-label="å³é­å®å¨å¯å¨çç´æ¥é¾æ¥" class="hash-link" href="#disable-secure-boot" title="å³é­å®å¨å¯å¨çç´æ¥é¾æ¥" translate="no">â</a></h2>
<p>å®å¨å¯å¨ï¼Secure Bootï¼ç¨äºä¿æ¤å¼æºè¿ç¨ï¼ä»å¨äº§åæç¡®è¦æ±æ¶å³é­ã</p>
<p><strong>â  åçæ¯å¦éè¦å³é­</strong></p>
<p>ä»¥ç®¡çåèº«ä»½æå¼ PowerShellï¼æ§è¡ï¼</p>
<div class="language-powershell codeBlockContainer_Y94m theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_IRmN"><pre class="prism-code language-powershell codeBlock_rbdZ thin-scrollbar" style="color:#393A34;background-color:#f6f8fa" tabindex="0"><code class="codeBlockLines_bJRA"><div class="token-line" style="color:#393A34"><span class="token plain">Confirm-SecureBootUEFI</span><br/></div></code></pre></div></div>
<ul>
<li class=""><code>True</code>ï¼å·²å¼å¯ã</li>
<li class=""><code>False</code>ï¼å·²å³é­ï¼ä¸ç¨åæ¹ã</li>
<li class="">æ¥éææ²¡æç»æï¼å°ç³»ç»ä¿¡æ¯æ BIOS ç¡®è®¤ï¼ä¸è½å½ä½å·²å³é­ã</li>
</ul>
<p><strong>â¡ æ¥æ¸ä¸»æ¿åçåå®æ´åå·</strong></p>
<p>å¨ PowerShell æ§è¡ï¼</p>
<div class="language-powershell codeBlockContainer_Y94m theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_IRmN"><pre class="prism-code language-powershell codeBlock_rbdZ thin-scrollbar" style="color:#393A34;background-color:#f6f8fa" tabindex="0"><code class="codeBlockLines_bJRA"><div class="token-line" style="color:#393A34"><span class="token plain">Get-CimInstance Win32_BaseBoard | Select-Object Manufacturer, Product</span><br/></div></code></pre></div></div>
<p><code>Manufacturer</code> æ¯ååï¼<code>Product</code> æ¯åå·ãæè¿ä¸¤é¡¹è®°ä¸æ¥ææªå¾ãä¸è¦åªè®°âåç¡ââå¾®æâï¼<strong>ååçä¸ååå·çè®¾ç½®ä½ç½®ä¹å¯è½ä¸å</strong>ãç¬è®°æ¬æåçæ´æºä¹è¯·è®°ä¸çµèçå®æ´åå·ã</p>
<p><strong>â¢ æ¾å¯¹åºåå·çå¾ææè§é¢æç¨</strong></p>
<p>å¯ä»¥å¨ <strong>æé³</strong> æç´¢ï¼ä¹å¯ä»¥é® <strong>è±åç­ AI å·¥å·</strong>ãä¾å¦æ¥å°æ¯åç¡ä¸»æ¿ï¼å°±æä¸é¢çâå®æ´åå·âæ¢æå®éåå·ï¼</p>
<blockquote>
<p>åç¡ãå®æ´åå·ãä¸»æ¿å¦ä½å³é­å®å¨å¯å¨ Secure Bootï¼</p>
</blockquote>
<p>é® AI æ¶å¯ä»¥æ´å·ä½ä¸ç¹ï¼</p>
<blockquote>
<p>æçä¸»æ¿æ¯ãåçï¼å®æ´åå·ãï¼æ³å³é­å®å¨å¯å¨ Secure Bootãè¯·åè¯ææä¹è¿å¥ BIOSãå¨åªéè®¾ç½®ãææ ·ä¿å­éåºï¼ä»¥åéå¯åæä¹ç¡®è®¤å·²å³é­ãè¯·ä¼ååèè¿ä¸ªåå·çå®æ¹è¯´æã</p>
</blockquote>
<p>ä¼åé<strong>åå·ç¸åãBIOS çé¢ç¸è¿</strong>çæç¨ï¼åä¸æ­¥æ­¥æä½ãå¦æç»é¢ä¸ä¸æ ·ï¼å¯ä»¥æå½å BIOS é¡µé¢æç» AIï¼é®âæç°å¨åºè¯¥ç¹åªéâã<strong>AI å¯è½è®¤éï¼æ¿ä¸åæ¶ååä¸ï¼ä»¥ä¸»æ¿å®æ¹è¯´æä¹¦ä¸ºåã</strong></p>
<p><strong>â£ ææç¨å³é­ï¼éå¯ååç¡®è®¤</strong></p>
<p>è¿å¥ BIOS åï¼æå¯¹åºåå·çæ¹æ³å³é­ <strong>Secure Boot</strong>ï¼ä¿å­éåºãé¨åä¸»æ¿æ¾ç¤ºä¸º <strong>Disabled / Off</strong>ï¼ä¹æä¸åçè®¾ç½®æ¹å¼ï¼ä¸è¦ç¡¬å¥å¶ä»åå·çæ­¥éª¤ã</p>
<p>åå° Windows åï¼åè¿è¡ä¸é¢ç <code>Confirm-SecureBootUEFI</code>ãæ¾ç¤º <code>False</code>ï¼æç¡®è®¤å·²å³é­ï¼æ¥éä¸ç®æåã</p>
<div class="theme-admonition theme-admonition-warning admonition_LJt0 alert alert--warning"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 16 16"><path d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z" fill-rule="evenodd"></path></svg></span>è¿å é¡¹ä¸è¦è·çä¹±æ¹</div><div class="admonitionContent__XZN"><p>æä½åä¿å­ BitLocker æ¢å¤å¯é¥ï¼å¯ç¨äº BitLocker çï¼åæå®æ¹æå¼æåä¿æ¤ã<strong>ä¸è¦æ¸é¤å®å¨å¯å¨å¯é¥ï¼ä¹ä¸è¦ä¸ºäºå³é­å®å¨å¯å¨é¡ºææ´æ¹ TPMãCSM æç£çååºã</strong></p></div></div>
<p>ä¸åéè¦å³é­æ¶ï¼æåè·¯å¾æ¢å¤ä¹åçè®¾ç½®ï¼ç¡®è®¤è½æ­£å¸¸å¯å¨åï¼æ¢å¤æ­¤åæåç BitLocker ä¿æ¤ã</p>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="disable-kernel-isolation-v">å³é­åå­å®æ´æ§<a aria-label="å³é­åå­å®æ´æ§çç´æ¥é¾æ¥" class="hash-link" href="#disable-kernel-isolation-v" title="å³é­åå­å®æ´æ§çç´æ¥é¾æ¥" translate="no">â</a></h2>
<p>è¿å¥ <strong>Windows å®å¨ä¸­å¿ â è®¾å¤å®å¨æ§ â æ ¸å¿éç¦»è¯¦ç»ä¿¡æ¯ â åå­å®æ´æ§</strong>ï¼å³é­åéå¯ãå¯æ¥ç<a class="" href="/misc/win/kernel/">éå¾æç¨</a>ã</p>
<p>å¦æäº§åè¿æç¡®è¦æ±å³é­ Hypervisor èªå¨å¯å¨ï¼åä»¥ç®¡çåèº«ä»½æ§è¡ï¼</p>
<div class="language-powershell codeBlockContainer_Y94m theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_IRmN"><pre class="prism-code language-powershell codeBlock_rbdZ thin-scrollbar" style="color:#393A34;background-color:#f6f8fa" tabindex="0"><code class="codeBlockLines_bJRA"><div class="token-line" style="color:#393A34"><span class="token plain">bcdedit /set hypervisorlaunchtype off</span><br/></div></code></pre></div></div>
<p>è¿å¯è½å½±å Hyper-VãWSL2ãWindows æ²çç­åè½ï¼æ§è¡åéè¦éå¯ãå®ä¸ BIOS ä¸­ç CPU èæåå¼å³ä¸æ¯åä¸é¡¹ã</p>
<p>æ¢å¤æ¶æ§è¡ <code>bcdedit /set hypervisorlaunchtype auto</code>ï¼å¹¶å¨å®å¨ä¸­å¿éæ°å¼å¯éè¦çåå­å®æ´æ§ï¼ç¶åéå¯ã</p>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="gpt-partition">æ£æ¥ MBR / GPT ååºæ ¼å¼<a aria-label="æ£æ¥ MBR / GPT ååºæ ¼å¼çç´æ¥é¾æ¥" class="hash-link" href="#gpt-partition" title="æ£æ¥ MBR / GPT ååºæ ¼å¼çç´æ¥é¾æ¥" translate="no">â</a></h2>
<p>ä»¥ç®¡çåèº«ä»½æå¼ PowerShellï¼æ£æ¥ Windows æå¨ç£çï¼</p>
<div class="language-powershell codeBlockContainer_Y94m theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_IRmN"><pre class="prism-code language-powershell codeBlock_rbdZ thin-scrollbar" style="color:#393A34;background-color:#f6f8fa" tabindex="0"><code class="codeBlockLines_bJRA"><div class="token-line" style="color:#393A34"><span class="token plain">Get-Partition -DriveLetter C | Get-Disk | Select-Object Number, PartitionStyle</span><br/></div></code></pre></div></div>
<p>Windows ä¸å¨ C çæ¶ï¼å°å½ä»¤ä¸­ç <code>C</code> æ¢æå®éçç¬¦ã</p>
<ul>
<li class=""><code>GPT</code>ï¼å·²ç»æ¯ GPTï¼ä¸ç¨è½¬æ¢ã</li>
<li class=""><code>MBR</code>ï¼ä»æ¯ MBRï¼ä»å¨ç¡®å®éè¦ UEFI ç­åè½æ¶èèè½¬æ¢ã</li>
</ul>
<div class="theme-admonition theme-admonition-danger admonition_LJt0 alert alert--danger"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 12 16"><path d="M5.05.31c.81 2.17.41 3.38-.52 4.31C3.55 5.67 1.98 6.45.9 7.98c-1.45 2.05-1.7 6.53 3.53 7.7-2.2-1.16-2.67-4.52-.3-6.61-.61 2.03.53 3.33 1.94 2.86 1.39-.47 2.3.53 2.27 1.67-.02.78-.31 1.44-1.13 1.81 3.42-.59 4.78-3.42 4.78-5.56 0-2.84-2.53-3.22-1.25-5.61-1.52.13-2.03 1.13-1.89 2.75.09 1.08-1.02 1.8-1.86 1.33-.67-.41-.66-1.19-.06-1.78C8.18 5.31 8.68 2.45 5.05.32L5.03.3l.02.01z" fill-rule="evenodd"></path></svg></span>è½¬æ¢ååå¤ä»½</div><div class="admonitionContent__XZN"><p>åç¡®è®¤ä¸»æ¿æ¯æ UEFIãæ°æ®å·²å¤ä»½ï¼åæå®æ´è½¬æ¢æç¨æä½ãè½¬æ¢åéå¸¸è¿è¦åæ¢ä¸º UEFI å¯å¨ï¼åªåå¶ä¸­ä¸åï¼å¯è½æ æ³å¼æºã</p></div></div>
<div class="custom-link-card-container"><a href="https://www.bilibili.com/video/BV1Fm4y1n7rS" rel="noreferrer noopener" style="color:#0A84FF;font-weight:700" target="_blank">åèè§é¢: MBR è½¬ GPT</a></div>
<p>è§é¢ä»ä½åèï¼æä½åæ ¸å¯¹èªå·±çç£çåä¸»æ¿ï¼ä¸è¦ç§æç£çç¼å·ã</p>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="uefi">ä» Legacy åæ¢å° UEFI<a aria-label="ä» Legacy åæ¢å° UEFIçç´æ¥é¾æ¥" class="hash-link" href="#uefi" title="ä» Legacy åæ¢å° UEFIçç´æ¥é¾æ¥" translate="no">â</a></h2>
<p>æ <code>Win + R</code>ï¼è¾å¥ <code>msinfo32</code>ï¼æå¼ç³»ç»ä¿¡æ¯ï¼æ¥ç <strong>BIOS æ¨¡å¼</strong>ã</p>
<ul>
<li class=""><strong>UEFI</strong>ï¼æ éä¿®æ¹ã</li>
<li class=""><strong>ä¼ ç» / Legacy</strong>ï¼æéè¦è¿ä¸æ­¥æ£æ¥ã</li>
</ul>
<p><strong>ä¸è¦ç´æ¥åæ¢ã</strong> åå®æä¸é¢çç£çæ£æ¥ï¼Legacy + MBR å®è£ç Windows ç´æ¥åæ¢å¯è½æ æ³å¯å¨ã</p>
<p>ç¡®è®¤ç³»ç»çåå¼å¯¼å·²åå¤å¥½ãä¸»æ¿æ¯æ UEFI åï¼åæè¯¥åå·è¯´æä¹¦è°æ´ <strong>Boot Mode / CSM / Legacy Support</strong>ï¼ä¿å­éåºãåç§°åç»åå ä¸»æ¿èå¼ï¼ä¸è¦æææ Boot éé¡¹ä¸èµ·æ¹æã</p>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="disable-tpm">å³é­ TPM<a aria-label="å³é­ TPMçç´æ¥é¾æ¥" class="hash-link" href="#disable-tpm" title="å³é­ TPMçç´æ¥é¾æ¥" translate="no">â</a></h2>
<p>TPM ç¨äº BitLocker ç­å®å¨åè½ãåªæäº§åæç¡®è¦æ±æ¶ææ¹ï¼åä¿å­æ¢å¤å¯é¥å¹¶å¤ç BitLocker ä¿æ¤ã</p>
<ol>
<li class="">è¿å¥ BIOSï¼å¨ <strong>Security / Advanced / Trusted Computing</strong> ç­é¡µé¢æ¾ TPM è®¾ç½®ã</li>
<li class="">Intel å¹³å°å¯è½å« <strong>PTT</strong>ï¼AMD å¹³å°å¯è½å« <strong>fTPM</strong>ã</li>
<li class="">åªå°å¯¹åºå¼å³è®¾ä¸º <strong>Disabled / Off</strong>ï¼ä¿å­å¹¶éåºã</li>
</ol>
<p><strong>ä¸è¦éæ© Clear TPMï¼æ¸é¤ TPMï¼</strong>ï¼å®ä¸æ¯âå³é­âçåä¹æä½ã</p>
<p>éè¦æ¢å¤æ¶æ¹ååå¼ï¼éå¸¸æ¯ <strong>Enabled / On</strong>ï¼ï¼éå¯å¹¶æ£æ¥ç³»ç»ï¼åæ¢å¤æ­¤åæåç BitLocker ä¿æ¤ã</p>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="vt">å¼å¯ CPU èæå<a aria-label="å¼å¯ CPU èæåçç´æ¥é¾æ¥" class="hash-link" href="#vt" title="å¼å¯ CPU èæåçç´æ¥é¾æ¥" translate="no">â</a></h2>
<p>åæå¼ <strong>ä»»å¡ç®¡çå¨ â æ§è½ â CPU</strong>ï¼æ¥ç <strong>èæå</strong>ã</p>
<ul>
<li class=""><strong>å·²å¯ç¨</strong>ï¼ä¸ç¨æ¹ã</li>
<li class=""><strong>å·²ç¦ç¨</strong>ï¼äº§åéè¦æ¶ï¼åè¿å¥ BIOS å¼å¯ã</li>
</ul>
<h3 class="anchor anchorTargetStickyNavbar_lorJ" id="intel-å¹³å°">Intel å¹³å°<a aria-label="Intel å¹³å°çç´æ¥é¾æ¥" class="hash-link" href="#intel-å¹³å°" title="Intel å¹³å°çç´æ¥é¾æ¥" translate="no">â</a></h3>
<p>å¨ BIOS ç CPU ç¸å³è®¾ç½®ä¸­æ¾å° <strong>Intel Virtualization Technology / Intel VT-x</strong>ï¼è®¾ä¸º <strong>Enabled / On</strong>ï¼ä¿å­éåºã</p>
<h3 class="anchor anchorTargetStickyNavbar_lorJ" id="amd-å¹³å°">AMD å¹³å°<a aria-label="AMD å¹³å°çç´æ¥é¾æ¥" class="hash-link" href="#amd-å¹³å°" title="AMD å¹³å°çç´æ¥é¾æ¥" translate="no">â</a></h3>
<p>å¨ BIOS ç CPU ç¸å³è®¾ç½®ä¸­æ¾å° <strong>SVM Mode</strong>ï¼è®¾ä¸º <strong>Enabled / On</strong>ï¼ä¿å­éåºã</p>
<p>åå°ä»»å¡ç®¡çå¨ï¼ç¡®è®¤èæåæ¾ç¤ºä¸º <strong>å·²å¯ç¨</strong>ãæ¾ä¸å°éé¡¹æ¶ï¼ç¨å®æ´ä¸»æ¿åå·æ¥è¯¢å®æ¹è¯´æä¹¦ã</p>
<div style="margin-top:32px"><span style="color:#8E8E93;font-size:13px">ä¿®æ¹æ¥æï¼2026-10-10ï¼åäº¬æ¶é´ï¼</span></div></div></article>