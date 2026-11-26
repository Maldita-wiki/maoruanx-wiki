---
sidebar_position: 1
title: éè¦å¯ç¨ JavaScript
slug: /misc/win/disable-secure-boot
---

<article><div class="theme-doc-markdown markdown"><header><h1>å³é­å®å¨å¯å¨</h1></header>
<p>å®å¨å¯å¨ï¼Secure Bootï¼ç¨äºä¿æ¤å¼æºè¿ç¨ï¼ä»å¨äº§åæç¡®è¦æ±æ¶å³é­ã</p>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="1-åçæ¯å¦éè¦å³é­">1. åçæ¯å¦éè¦å³é­<a aria-label="1. åçæ¯å¦éè¦å³é­çç´æ¥é¾æ¥" class="hash-link" href="#1-åçæ¯å¦éè¦å³é­" title="1. åçæ¯å¦éè¦å³é­çç´æ¥é¾æ¥" translate="no">â</a></h2>
<p>ä»¥ç®¡çåèº«ä»½æå¼ PowerShellï¼æ§è¡ï¼</p>
<div class="language-powershell codeBlockContainer_Y94m theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_IRmN"><pre class="prism-code language-powershell codeBlock_rbdZ thin-scrollbar" style="color:#393A34;background-color:#f6f8fa" tabindex="0"><code class="codeBlockLines_bJRA"><div class="token-line" style="color:#393A34"><span class="token plain">Confirm-SecureBootUEFI</span><br/></div></code></pre></div></div>
<ul>
<li class=""><code>True</code>ï¼å·²å¼å¯ã</li>
<li class=""><code>False</code>ï¼å·²å³é­ï¼ä¸ç¨åæ¹ã</li>
<li class="">æ¥éææ²¡æç»æï¼å°ç³»ç»ä¿¡æ¯æ BIOS ç¡®è®¤ï¼ä¸è½å½ä½å·²å³é­ã</li>
</ul>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="2-æ¥æ¸ä¸»æ¿åçåå®æ´åå·">2. æ¥æ¸ä¸»æ¿åçåå®æ´åå·<a aria-label="2. æ¥æ¸ä¸»æ¿åçåå®æ´åå·çç´æ¥é¾æ¥" class="hash-link" href="#2-æ¥æ¸ä¸»æ¿åçåå®æ´åå·" title="2. æ¥æ¸ä¸»æ¿åçåå®æ´åå·çç´æ¥é¾æ¥" translate="no">â</a></h2>
<p>å¨ PowerShell æ§è¡ï¼</p>
<div class="language-powershell codeBlockContainer_Y94m theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_IRmN"><pre class="prism-code language-powershell codeBlock_rbdZ thin-scrollbar" style="color:#393A34;background-color:#f6f8fa" tabindex="0"><code class="codeBlockLines_bJRA"><div class="token-line" style="color:#393A34"><span class="token plain">Get-CimInstance Win32_BaseBoard | Select-Object Manufacturer, Product</span><br/></div></code></pre></div></div>
<p><code>Manufacturer</code> æ¯ååï¼<code>Product</code> æ¯åå·ãæè¿ä¸¤é¡¹è®°ä¸æ¥ææªå¾ãä¸è¦åªè®°âåç¡ââå¾®æâï¼<strong>ååçä¸ååå·çè®¾ç½®ä½ç½®ä¹å¯è½ä¸å</strong>ãç¬è®°æ¬æåçæ´æºä¹è¯·è®°ä¸çµèçå®æ´åå·ã</p>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="3-æ¾å¯¹åºåå·çå¾ææè§é¢æç¨">3. æ¾å¯¹åºåå·çå¾ææè§é¢æç¨<a aria-label="3. æ¾å¯¹åºåå·çå¾ææè§é¢æç¨çç´æ¥é¾æ¥" class="hash-link" href="#3-æ¾å¯¹åºåå·çå¾ææè§é¢æç¨" title="3. æ¾å¯¹åºåå·çå¾ææè§é¢æç¨çç´æ¥é¾æ¥" translate="no">â</a></h2>
<p>å¯ä»¥å¨ <strong>æé³</strong> æç´¢ï¼ä¹å¯ä»¥é® <strong>è±åç­ AI å·¥å·</strong>ãä¾å¦æ¥å°æ¯åç¡ä¸»æ¿ï¼å°±æä¸é¢çâå®æ´åå·âæ¢æå®éåå·ï¼</p>
<blockquote>
<p>åç¡ãå®æ´åå·ãä¸»æ¿å¦ä½å³é­å®å¨å¯å¨ Secure Bootï¼</p>
</blockquote>
<p>é® AI æ¶å¯ä»¥æ´å·ä½ä¸ç¹ï¼</p>
<blockquote>
<p>æçä¸»æ¿æ¯ãåçï¼å®æ´åå·ãï¼æ³å³é­å®å¨å¯å¨ Secure Bootãè¯·åè¯ææä¹è¿å¥ BIOSãå¨åªéè®¾ç½®ãææ ·ä¿å­éåºï¼ä»¥åéå¯åæä¹ç¡®è®¤å·²å³é­ãè¯·ä¼ååèè¿ä¸ªåå·çå®æ¹è¯´æã</p>
</blockquote>
<p>ä¼åé<strong>åå·ç¸åãBIOS çé¢ç¸è¿</strong>çæç¨ï¼åä¸æ­¥æ­¥æä½ãå¦æç»é¢ä¸ä¸æ ·ï¼å¯ä»¥æå½å BIOS é¡µé¢æç» AIï¼é®âæç°å¨åºè¯¥ç¹åªéâã<strong>AI å¯è½è®¤éï¼æ¿ä¸åæ¶ååä¸ï¼ä»¥ä¸»æ¿å®æ¹è¯´æä¹¦ä¸ºåã</strong></p>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="4-ææç¨å³é­éå¯ååç¡®è®¤">4. ææç¨å³é­ï¼éå¯ååç¡®è®¤<a aria-label="4. ææç¨å³é­ï¼éå¯ååç¡®è®¤çç´æ¥é¾æ¥" class="hash-link" href="#4-ææç¨å³é­éå¯ååç¡®è®¤" title="4. ææç¨å³é­ï¼éå¯ååç¡®è®¤çç´æ¥é¾æ¥" translate="no">â</a></h2>
<p>è¿å¥ BIOS åï¼æå¯¹åºåå·çæ¹æ³å³é­ <strong>Secure Boot</strong>ï¼ä¿å­éåºãé¨åä¸»æ¿æ¾ç¤ºä¸º <strong>Disabled / Off</strong>ï¼ä¹æä¸åçè®¾ç½®æ¹å¼ï¼ä¸è¦ç¡¬å¥å¶ä»åå·çæ­¥éª¤ã</p>
<p>åå° Windows åï¼åè¿è¡ä¸é¢ç <code>Confirm-SecureBootUEFI</code>ãæ¾ç¤º <code>False</code>ï¼æç¡®è®¤å·²å³é­ï¼æ¥éä¸ç®æåã</p>
<div class="theme-admonition theme-admonition-warning admonition_LJt0 alert alert--warning"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 16 16"><path d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z" fill-rule="evenodd"></path></svg></span>è¿å é¡¹ä¸è¦è·çä¹±æ¹</div><div class="admonitionContent__XZN"><p>æä½åä¿å­ BitLocker æ¢å¤å¯é¥ï¼å¯ç¨äº BitLocker çï¼åæå®æ¹æå¼æåä¿æ¤ã<strong>ä¸è¦æ¸é¤å®å¨å¯å¨å¯é¥ï¼ä¹ä¸è¦ä¸ºäºå³é­å®å¨å¯å¨é¡ºææ´æ¹ TPMãCSM æç£çååºã</strong></p></div></div>
<p>ä¸åéè¦å³é­æ¶ï¼æåè·¯å¾æ¢å¤ä¹åçè®¾ç½®ï¼ç¡®è®¤è½æ­£å¸¸å¯å¨åï¼æ¢å¤æ­¤åæåç BitLocker ä¿æ¤ã</p>
<hr/>
<p>éè¦äºè§£è¿å¥ BIOS çæ¹æ³ï¼å¯æ¥ç<a class="" href="/misc/win/bios#bios-entry-keys">ææ ·è¿å¥ BIOS</a>ã</p>
<style>html[class~="docs-doc-id-misc/win/disable-secure-boot"] .theme-code-block pre,html[class~="docs-doc-id-misc/win/disable-secure-boot"] .theme-code-block code,html[class~="docs-doc-id-misc/win/disable-secure-boot"] .theme-code-block .token-line,html[class~="docs-doc-id-misc/win/disable-secure-boot"] .theme-code-block .token{color:var(--ifm-font-color-base)!important}html[class~="docs-doc-id-misc/win/disable-secure-boot"] .theme-code-block pre{background:var(--ifm-code-background)!important}</style></div></article>