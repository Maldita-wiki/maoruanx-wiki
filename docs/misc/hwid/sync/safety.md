---
sidebar_position: 1
title: éè¦å¯ç¨ JavaScript
slug: /misc/hwid/sync/safety
---

<article><div class="theme-doc-markdown markdown"><header><h1>è´­ä¹°é¡»ç¥ãå®å¨ä¸è®¸å¯è¯´æ</h1></header>
<p><strong><span class="text-grey">æ¬é¡µæ±æ»å®ç½äº§åé¡µãå®å¨æç« ä¸æå¡æ¡æ¬¾ä¸­çéè¦éå¶ãå¼å§æä½åè¯·å®æ´éè¯»ã</span></strong></p>
<div class="theme-admonition theme-admonition-info admonition_LJt0 alert alert--info"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 14 16"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z" fill-rule="evenodd"></path></svg></span>æ¬åºå¨å®åå</div><div class="admonitionContent__XZN"><p>æ¬åºåªéå®âä¸æ¬¡ç¡¬è§£âåâæ°¸ä¹ç¡¬è§£ï¼è½¯è§£æç»åâãä¸æ¬¡ç¡¬è§£ä¸åå«è½¯è§£ï¼æç»ååå«æ éæ¬¡è½¯è§£éæ°å¤çã1 æ¬¡æ°¸ä¹ç¡¬è§£å®è£ï¼ä»¥å Lifetime æ´æ°ä¸æ¯æãè®¾å¤è¿ç§»åé¢å¤ç¡¬è§£ä»¥æ¬åºååé¡µä¸åè´§è¯´æä¸ºåã</p></div></div>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="system"><strong>ç³»ç»ä¸æ°æ®é£é©</strong><a aria-label="systemçç´æ¥é¾æ¥" class="hash-link" href="#system" title="systemçç´æ¥é¾æ¥" translate="no">â</a></h2>
<p>SYNC å±äºéè¦è¾é«ç³»ç»æéçè½¯ä»¶ãå®ç½å®å¨æç« ä¹æç¡®è¯´æï¼è¿ç±»å·¥å·å¯è½å¸¦æ¥ä»¥ä¸é£é©ï¼</p>
<ul>
<li class="">æ¥æºä¸æçç¨åºå¯è½åå«æ¨é©¬ãæç¿ç¨åºæå­æ®çªååè½ã</li>
<li class="">åæ ¸çº§é©±å¨å¯è½é æèå±ãå¯å¨å¾ªç¯æé©±å¨å²çªã</li>
<li class="">ç¡¬è§£æ¶å BIOS / SMBIOS å Windows éè£ï¼éè¯¯æä½å¯è½å¯¼è´ç³»ç»æ æ³å¯å¨æ Windows æ¿æ´»ååã</li>
<li class="">æ¸¸æä¸åä½å¼ç³»ç»ä¼æç»­æ´æ°ï¼âå½åå¯ç¨âä¸ç­äºæ°¸ä¹ä¸ä¼å¤±ææè¢«æ£æµã</li>
</ul>
<div class="theme-admonition theme-admonition-danger admonition_LJt0 alert alert--danger"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 12 16"><path d="M5.05.31c.81 2.17.41 3.38-.52 4.31C3.55 5.67 1.98 6.45.9 7.98c-1.45 2.05-1.7 6.53 3.53 7.7-2.2-1.16-2.67-4.52-.3-6.61-.61 2.03.53 3.33 1.94 2.86 1.39-.47 2.3.53 2.27 1.67-.02.78-.31 1.44-1.13 1.81 3.42-.59 4.78-3.42 4.78-5.56 0-2.84-2.53-3.22-1.25-5.61-1.52.13-2.03 1.13-1.89 2.75.09 1.08-1.02 1.8-1.86 1.33-.67-.41-.66-1.19-.06-1.78C8.18 5.31 8.68 2.45 5.05.32L5.03.3l.02.01z" fill-rule="evenodd"></path></svg></span>å®å¨åºçº¿</div><div class="admonitionContent__XZN"><ol>
<li class="">åªä¸è½½ <a href="https://sync.top/" rel="noopener noreferrer" target="_blank">SYNC å®ç½ï¼sync.topï¼</a> æä¾çæä»¶ã</li>
<li class="">ä½¿ç¨ç¡¬è§£åååå¼å®¹æ§æ£æµåå®æ´å¤ä»½ã</li>
<li class="">ä¸è¿è¡ç¬¬ä¸æ¹âç ´è§£çââåè´¹ä¿®å¤å¨âææ¥æºä¸æçé©±å¨ã</li>
<li class="">ä¸æç§æ§æç¨èªè¡ä¿®æ¹ BIOSãTPMãç£çéµåææ³¨åè¡¨ã</li>
<li class="">ä¸å¨å¬å¼èå¤©ãæªå¾ææ¥å¿ä¸­æ³é²æ¿æ´»ç ãå¯ç ãé®ç®±éªè¯ç åä»æ¬¾ä¿¡æ¯ã</li>
</ol></div></div>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="account"><strong>è´¦å·ä¸å¹³å°è§å</strong><a aria-label="accountçç´æ¥é¾æ¥" class="hash-link" href="#account" title="accountçç´æ¥é¾æ¥" translate="no">â</a></h2>
<p>ç¡¬ä»¶æ è¯å¤çä¸ç­äºæ¸¸æè´¦å·è§£å°ï¼ä¹ä¸è½æ¿ä»£å®æ¹ç³è¯ãæ¸¸ææå¹³å°å¯è½æç¬¬ä¸æ¹å·¥å·è§ä¸ºè¿åæå¡æ¡æ¬¾ï¼å¹¶ç»§ç»­éåè´¦å·æè®¾å¤å¤ç½ã</p>
<p>å¦æä½ è®¤ä¸ºå°ç¦å±äºè¯¯å¤ï¼ä¼åä½¿ç¨æ¸¸ææå¹³å°çå®æ¹ç³è¯æ¸ éãä½¿ç¨ SYNC ååºèªè¡ç¡®è®¤å½å°æ³å¾ãæ¸¸ææ¡æ¬¾åè´¦å·é£é©ã</p>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="license"><strong>SYNC è®¸å¯éå¶</strong><a aria-label="licenseçç´æ¥é¾æ¥" class="hash-link" href="#license" title="licenseçç´æ¥é¾æ¥" translate="no">â</a></h2>
<p>æ ¹æ®å®ç½å¬å¼æ¡æ¬¾ï¼</p>
<ul>
<li class="">è®¿é®æé»è®¤ä¸å¯è½¬è®©ã</li>
<li class="">ç¦æ­¢å±äº«å·²æ¿æ´»è´¦å·æéæ°ååç¨åºã</li>
<li class="">ç¦æ­¢ç ´è§£ãåç¼è¯ãæ¶æåææä¸ä¼ è½¯ä»¶æä»¶ä¸çé¢åå®¹ã</li>
<li class="">è®¸å¯å¯è½å è¿è§ä»æ¬¾äºè®®ãæ¶ææä»æå±äº«è¡ä¸ºè¢«ç»æ­¢ã</li>
<li class="">æç»åç Lifetime æçä»¥å¯¹åºäº§åä»åæ¯æä¸ºåæï¼âæ éæ¬¡âæè½¯è§£éæ°å¤çï¼ä¸ä»£è¡¨æ éæ¬¡ç¡¬è§£ãæ éæ¬¡æ¢æºæèªå¨åå«æªæ¥æ°äº§åã</li>
</ul>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="privacy"><strong>è®¾å¤ä¿¡æ¯ä¸éç§</strong><a aria-label="privacyçç´æ¥é¾æ¥" class="hash-link" href="#privacy" title="privacyçç´æ¥é¾æ¥" translate="no">â</a></h2>
<p>å®ç½æ¡æ¬¾è¯´æï¼æå¡å¯è½æ¶éç¨äºéªè¯ç HWIDãé®ç®±ãæµè§å¨è¯­è¨ãæä½ç³»ç»ãIP å°åãæ¸¸æåç¨æ·åä»¥åçæ§ç¨åºå­å¨ä¿¡æ¯ãè´­ä¹°æä½¿ç¨ååºéè¯»å®æ¶ <a href="https://sync.top/tos" rel="noopener noreferrer" target="_blank">æå¡æ¡æ¬¾</a>ã</p>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="purchase-policy"><strong>æ¬åºè´­ä¹°è§å</strong><a aria-label="purchase-policyçç´æ¥é¾æ¥" class="hash-link" href="#purchase-policy" title="purchase-policyçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div class="theme-admonition theme-admonition-danger admonition_LJt0 alert alert--danger"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 12 16"><path d="M5.05.31c.81 2.17.41 3.38-.52 4.31C3.55 5.67 1.98 6.45.9 7.98c-1.45 2.05-1.7 6.53 3.53 7.7-2.2-1.16-2.67-4.52-.3-6.61-.61 2.03.53 3.33 1.94 2.86 1.39-.47 2.3.53 2.27 1.67-.02.78-.31 1.44-1.13 1.81 3.42-.59 4.78-3.42 4.78-5.56 0-2.84-2.53-3.22-1.25-5.61-1.52.13-2.03 1.13-1.89 2.75.09 1.08-1.02 1.8-1.86 1.33-.67-.41-.66-1.19-.06-1.78C8.18 5.31 8.68 2.45 5.05.32L5.03.3l.02.01z" fill-rule="evenodd"></path></svg></span>æä¸åè¯·ç¡®è®¤</div><div class="admonitionContent__XZN"><p>æ¬åºéå®çæ¯æ°å­åè½¯ä»¶è®¸å¯åæ¿æ´»ç ã<strong>ä¸åå¹¶å®æåè´§åï¼ä¸æ¯æåæ¶ãéæ¢æéæ¬¾</strong>ãè¯·å¨ä»æ¬¾åå®æ´éè¯»æç¨ï¼ç¡®è®¤è´­ä¹°çæ¯âä¸æ¬¡ç¡¬è§£âè¿æ¯âæ°¸ä¹ç¡¬è§£ï¼è½¯è§£æç»åâï¼å¹¶ç¡®è®¤è®¾å¤å¼å®¹æ§ãç®æ æ¸¸æç¶æåæä½è¦æ±ï¼æ³å¾æ³è§å¦æå¼ºå¶è§å®çé¤å¤ã</p></div></div>
<p>ä¸åæåµåä¸è½ä½ä¸ºéæ¢çç±ï¼</p>
<ul>
<li class="">æ²¡æååå¼å®¹æ§æ£æµï¼</li>
<li class="">ä¹°éâä¸æ¬¡ç¡¬è§£âæâæ°¸ä¹ç¡¬è§£ï¼è½¯è§£æç»åâï¼</li>
<li class="">ç®æ æ¸¸æå¤äºç»´æ¤ãæ´æ°æä¸´æ¶ä¸å¯ç¨ç¶æï¼</li>
<li class="">ç¨æ·ä¸ä¼æä½ãæ²¡æéè¯»æç¨ææ²¡ææ Loader æç¤ºæ§è¡ï¼</li>
<li class="">ç¨æ·èªè¡ä¿®æ¹ BIOSãTPMãç£çæç³»ç»è®¾ç½®å¯¼è´å¤±è´¥ï¼</li>
<li class="">æ¸¸æè´¦å·æ¬èº«è¢«å°ï¼è¯¯ä»¥ä¸ºæ¹æºå¨ç å¯ä»¥æ¢å¤åè´¦å·ï¼</li>
<li class="">æ¿æ´»ç ãè´¦å·æé®ç®±ä¿¡æ¯è¢«ç¨æ·èªè¡æ³é²ã</li>
</ul>
<p>å¦æéå°æ¿æ´»ãç»å®æè¿è¡é®é¢ï¼æ¬åºæä¾çæ¯é®é¢æ ¸æ¥ãæç¨æå¼åææ¯æ¯æï¼ä¸æ¿è¯ºä»¥éæ¬¾æ¹å¼å¤çã</p>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="support"><strong>æ¯æå¥å£</strong><a aria-label="supportçç´æ¥é¾æ¥" class="hash-link" href="#support" title="supportçç´æ¥é¾æ¥" translate="no">â</a></h2>
<ul>
<li class="">
<a href="https://sync.top/contact-us" rel="noopener noreferrer" target="_blank">å®æ¹èç³»é¡µé¢</a>
</li>
<li class="">
<a href="https://sync.top/discord" rel="noopener noreferrer" target="_blank">å®æ¹ Discord è·³è½¬é¡µ</a>
</li>
<li class="">
<a href="https://sync.top/customer" rel="noopener noreferrer" target="_blank">å®¢æ·é¢æ¿</a>
</li>
<li class="">
<a href="https://syncv2.statuspage.io/" rel="noopener noreferrer" target="_blank">å®æ¹ç¶æé¡µ</a>
</li>
<li class="">
<a href="https://sync.top/tos" rel="noopener noreferrer" target="_blank">æå¡æ¡æ¬¾</a>
</li>
</ul>
<div style="margin-top:32px"><span style="color:#8E8E93;font-size:13px">ä¿®æ¹æ¥æ: 2026-08-18 08:21 (åäº¬æ¶é´)</span></div></div></article>