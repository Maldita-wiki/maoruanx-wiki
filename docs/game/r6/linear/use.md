---
sidebar_position: 1
title: Linear ä½¿ç¨æç¨
slug: /game/r6/linear/use
---

<article><div class="theme-doc-markdown markdown"><header><h1>Linear ä½¿ç¨æç¨</h1></header>
<p><strong><span class="text-grey">Linear èåæ³¨åãä¸è½½åä½¿ç¨è¯¦ç»æç¨</span></strong></p>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id="preface"><strong>åè¨</strong><a aria-label="prefaceçç´æ¥é¾æ¥" class="hash-link" href="#preface" title="prefaceçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div class="theme-admonition theme-admonition-tip admonition_xJq3 alert alert--success"><div class="admonitionHeading_Gvgb"><span class="admonitionIcon_Rf37"><svg viewbox="0 0 12 16"><path d="M6.5 0C3.48 0 1 2.19 1 5c0 .92.55 2.25 1 3 1.34 2.25 1.78 2.78 2 4v1h5v-1c.22-1.22.66-1.75 2-4 .45-.75 1-2.08 1-3 0-2.81-2.48-5-5.5-5zm3.64 7.48c-.25.44-.47.8-.67 1.11-.86 1.41-1.25 2.06-1.45 3.23-.02.05-.02.11-.02.17H5c0-.06 0-.13-.02-.17-.2-1.17-.59-1.83-1.45-3.23-.2-.31-.42-.67-.67-1.11C2.44 6.78 2 5.65 2 5c0-2.2 2.02-4 4.5-4 1.22 0 2.36.42 3.22 1.19C10.55 2.94 11 3.94 11 5c0 .66-.44 1.78-.86 2.48zM4 14h5c-.23 1.14-1.3 2-2.5 2s-2.27-.86-2.5-2z" fill-rule="evenodd"></path></svg></span>æ¸©é¦¨æç¤º</div><div class="admonitionContent_BuS1"><ul>
<li class=""><strong>ä¿å­å¥½èªå·±çæ¿æ´»ç è·æ³¨åçè´¦å·å¯ç , è¥ä¸¢å¤±æ æ³æ¾ååæèªè´</strong></li>
<li class=""><strong>æ¬æç¨ä»åæ­£å¸¸æ­¥éª¤æ¼ç¤º, æ ¹æ®æç¨æä½åºç°é®é¢ä¼åèç³»ä½ çåå®¶è§£å³</strong></li>
<li class=""><strong>è¯·ä»ç»éè¯»ææåå®¹ä¸æç¤º,éå°é®é¢å°è¯åèªå·±è§£å³ (å¦åå© AI å·¥å·)</strong></li>
<li class=""><strong>æç¨å¯è½å·ææ¶ææ§,è¥ä¸éç¨è¯·åæ¶èç³»æ</strong></li>
</ul></div></div>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id="detection"><strong>ç¡¬ä»¶æ£æµ</strong><a aria-label="detectionçç´æ¥é¾æ¥" class="hash-link" href="#detection" title="detectionçç´æ¥é¾æ¥" translate="no">â</a></h2>
<p><strong>ä»¥ä¸æ­¥éª¤æ¯å¨ä¸è¿è¡å¤ææä½/éè£çåæä¸å¯¹ä½ çç¡¬ä»¶åç³»ç»è¯ä¼°çæ¹æ¡,å¦ä¸æ»¡è¶³å¯éæ©æ¾å¼ææå¨è§£å³</strong></p>
<p><strong>1.æä¸ <span class="text-blue"><code>win+r</code></span> å¹¶è¾å¥ <span class="text-blue"><code>winver</code></span> åè½¦,ä»¥ä¸æ¯å¯ç¨ç³»ç»<!-- -->:Win<!-- --> 10 ä» 22H2 / Win 11 22H2 åä»¥ä¸ (å¦ä¸æ¯,ç¹å«æ³ç©çå¯æ³åæ³éè£ç³»ç»,æ U çå°±å¯ä»¥è½»æ¾æå®)</strong></p>
<div style="text-align:center"><p><img alt="" class="img_ev3q" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/item/697c787d1af8234bd07d22f4.png"/></p><p><img alt="" class="img_ev3q" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/item/697c787d1af8234bd07d22f6.png"/></p></div>
<p><strong>2.ç¡®ä¿ <span class="text-blue"><code>BIOS</code></span> ä¸º <span class="text-blue"><code>UEFI</code></span> æ¨¡å¼,é¼ æ ç§»è³<span class="text-blue"><code>ä¸æ¹ä»£ç åå³ä¾§</code></span> ,ç¹å» <span class="text-blue"><code>å¤å¶å°åªè´´æ¿</code></span></strong></p>
<div class="language-powershell codeBlockContainer_Ckt0 theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_QJqH"><pre class="prism-code language-powershell codeBlock_bY9V thin-scrollbar" style="color:#393A34;background-color:#f6f8fa" tabindex="0"><code class="codeBlockLines_e6Vv"><span class="token-line" style="color:#393A34"><span class="token plain">$env:firmware_type</span><br/></span></code></pre></div></div>
<p><strong>å³é® ç¹å»å±å¹å·¦ä¸è§ Windows å¼å§èå - ç¹å» <span class="text-blue"><code>ç»ç«¯ç®¡çå(Windows PowerShell [ç®¡çå])</code></span>,å³é®ç¹å»é»è²çªå£ - åæä¸åè½¦,ç¡®ä¿ä¸º UEFI (å¦ä¸æ¯,å¯éè£ç³»ç»æä½¿ç¨å·¥å·è½¬,å¯åè è¿é (å»ºè®®æä¸ª U ç + å¤ä»½å¥½éè¦æ°æ®)</strong></p>
<div style="text-align:center"><p><img alt="" class="img_ev3q" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/item/694b9ed826657af64c6cf732.png"/></p><p><img alt="" class="img_ev3q" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/item/694b9ed826657af64c6cf731.webp"/></p></div>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id="å¿å¤è®¾ç½®"><strong>å¿å¤è®¾ç½®</strong><a aria-label="å¿å¤è®¾ç½®çç´æ¥é¾æ¥" class="hash-link" href="#å¿å¤è®¾ç½®" title="å¿å¤è®¾ç½®çç´æ¥é¾æ¥" translate="no">â</a></h2>
<div class="theme-admonition theme-admonition-danger admonition_xJq3 alert alert--danger"><div class="admonitionHeading_Gvgb"><span class="admonitionIcon_Rf37"><svg viewbox="0 0 12 16"><path d="M5.05.31c.81 2.17.41 3.38-.52 4.31C3.55 5.67 1.98 6.45.9 7.98c-1.45 2.05-1.7 6.53 3.53 7.7-2.2-1.16-2.67-4.52-.3-6.61-.61 2.03.53 3.33 1.94 2.86 1.39-.47 2.3.53 2.27 1.67-.02.78-.31 1.44-1.13 1.81 3.42-.59 4.78-3.42 4.78-5.56 0-2.84-2.53-3.22-1.25-5.61-1.52.13-2.03 1.13-1.89 2.75.09 1.08-1.02 1.8-1.86 1.33-.67-.41-.66-1.19-.06-1.78C8.18 5.31 8.68 2.45 5.05.32L5.03.3l.02.01z" fill-rule="evenodd"></path></svg></span>å¿å¤è®¾ç½®</div><div class="admonitionContent_BuS1"><ul>
<li class=""><strong><code>å¿é¡»</code>æç§<code>æç¨</code>å°<code>ç³»ç»ç¯å¢</code>è®¾ç½®å¥½</strong>
<ul>
<li class=""><strong><a class="" href="/injecterror/start">å¿å¤ç¯å¢è®¾ç½®æç¨</a></strong></li>
</ul>
</li>
</ul></div></div>
<hr/>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="steam"><strong>Steamè®¾ç½®</strong><a aria-label="steamçç´æ¥é¾æ¥" class="hash-link" href="#steam" title="steamçç´æ¥é¾æ¥" translate="no">â</a></h3>
<blockquote>
<p><strong>1.æå¼ä½ çSteamå®¢æ·ç«¯,å¯¼èªå°ä½ çæ¸¸æåº</strong><br/>
<strong>2.å¨æ¸¸æåè¡¨ä¸­å³é®åå»å½©è¹å­å·å´æ»</strong><br/>
<strong>3.ä»ä¸ä¸æèåä¸­éæ©âå±æ§â.è¿å°æå¼æ¸¸æçå±æ§çªå£</strong><br/>
<strong>4.ç¡®ä¿æ¨ä½äºâå¸¸è§âéé¡¹å¡ä¸­ä»¥<code>DX11å¯å¨æ¸¸æ</code></strong></p>
</blockquote>
<div style="text-align:center"><p><img alt="" class="img_ev3q" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/item/69805b93bb6a79a9e97a570b.png"/></p></div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="discord"><strong>Discord</strong><a aria-label="discordçç´æ¥é¾æ¥" class="hash-link" href="#discord" title="discordçç´æ¥é¾æ¥" translate="no">â</a></h3>
<blockquote>
<p><strong>å¦æä½ æ²¡æDiscord,å¯ä»¥æ è§æ­¤æ­¥éª¤</strong></p>
</blockquote>
<div style="text-align:center"><p><img alt="" class="img_ev3q" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/item/69805b93bb6a79a9e97a570c.png"/></p></div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="xbox"><strong>XBOX</strong><a aria-label="xboxçç´æ¥é¾æ¥" class="hash-link" href="#xbox" title="xboxçç´æ¥é¾æ¥" translate="no">â</a></h3>
<div style="text-align:center"><p><img alt="" class="img_ev3q" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/item/69805b93bb6a79a9e97a570d.png"/></p></div>
<h3 class="anchor anchorTargetStickyNavbar_Vzrq" id="booster"><strong>å éå¨</strong><a aria-label="boosterçç´æ¥é¾æ¥" class="hash-link" href="#booster" title="boosterçç´æ¥é¾æ¥" translate="no">â</a></h3>
<blockquote>
<p><strong>ç½ç»ä¸å¥½çå¡å¿èªå·±ä½¿ç¨ç§å­¦ä¸ç½</strong><br/>
<strong>ç¦æ­¢ä½¿ç¨<span class="text-blue"><code>åè´¹å éå¨</code></span></strong><br/>
<strong><span class="text-blue"><code>é·ç¥/èè·/é²ç</code></span>ç­å éå¨è¿ææè°ç<span class="text-blue"><code>å éå¨çå­</code></span>èªè¡å°è¯,ä¸è¡å°±æ¢ä¸åå éå¨</strong></p>
<blockquote>
<ul>
<li class=""><strong><a class="" href="https://uu.163.com/" rel="noopener noreferrer" target="_blank">UU</a>ï¼è·¯ç±æ¨¡å¼/æ¨¡å¼ 3 (UU/å¥æ¸¸ç¸å¯¹æç¨³)</strong></li>
<li class=""><strong><a class="" href="https://www.qiyou.cn/" rel="noopener noreferrer" target="_blank">å¥æ¸¸</a>ï¼æ¨¡å¼ 1 (UU/å¥æ¸¸ç¸å¯¹æç¨³)</strong></li>
<li class=""><strong><a class="" href="https://www.xunyou.com/" rel="noopener noreferrer" target="_blank">è¿æ¸¸</a>ï¼æ¨¡å¼ 3 (èçä¹ä¸é)</strong></li>
<li class=""><strong><a class="" href="https://www.akspeedy.com/" rel="noopener noreferrer" target="_blank">AK</a>ï¼æ¨¡å¼ 5 (èªç¨æ¨è,æ§ä»·æ¯é«,æ¶é¿è®¡ç®,ä¸è¡ç¨ æ¨¡å¼ 4)</strong><br/>
<strong><span class="text-purple">å°è¯æ´æ¢å éå¨ æ´æ¢å éå¨æ¨¡å¼ æ´æ¢å éå¨èç¹ ç´å°è½æ³¨å¥ä½¿ç¨ä¸ºæ­¢</span></strong></li>
</ul>
</blockquote>
</blockquote>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id="download"><strong>ä¸è½½</strong><a aria-label="downloadçç´æ¥é¾æ¥" class="hash-link" href="#download" title="downloadçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div class="theme-admonition theme-admonition-info admonition_xJq3 alert alert--info"><div class="admonitionHeading_Gvgb"><span class="admonitionIcon_Rf37"><svg viewbox="0 0 14 16"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z" fill-rule="evenodd"></path></svg></span>å°è´´å£«</div><div class="admonitionContent_BuS1"><p><strong>æ°¸è¿å»æä¸ä¸ªå¥½ä¹ æ¯:ä¸è½½ä»»ä½ç¨åºä¸è¦ä¸å°å« ä¸­æ/ä¸­æç¬¦å·/å¥æªå­ç¬¦ çæä»¶å¤¹ä¸­,è¿å¯è½å¯¼è´é¨åç¨åºè¿è¡ä¸äº;å¹¶å»ºè®®å°åä¸ªç¨åº/åç¼©åæ¾å¥åç¬çæä»¶å¤¹ä¸­,é²æ­¢é¨åç¨åºéæ¾åºå¾å¤é²ææä»¶æè§£ååºå¤ªå¤æä»¶å½±åæ´æ´åº¦</strong></p></div></div>
<!-- -->
<div class="custom-link-card-container"><p><a class="" href="https://launcher.linear.pub" rel="noopener noreferrer" target="_blank">Linear - Donwload</a></p></div>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id="subscription"><strong>æ¿æ´»</strong><a aria-label="subscriptionçç´æ¥é¾æ¥" class="hash-link" href="#subscription" title="subscriptionçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div class="theme-admonition theme-admonition-danger admonition_xJq3 alert alert--danger"><div class="admonitionHeading_Gvgb"><span class="admonitionIcon_Rf37"><svg viewbox="0 0 12 16"><path d="M5.05.31c.81 2.17.41 3.38-.52 4.31C3.55 5.67 1.98 6.45.9 7.98c-1.45 2.05-1.7 6.53 3.53 7.7-2.2-1.16-2.67-4.52-.3-6.61-.61 2.03.53 3.33 1.94 2.86 1.39-.47 2.3.53 2.27 1.67-.02.78-.31 1.44-1.13 1.81 3.42-.59 4.78-3.42 4.78-5.56 0-2.84-2.53-3.22-1.25-5.61-1.52.13-2.03 1.13-1.89 2.75.09 1.08-1.02 1.8-1.86 1.33-.67-.41-.66-1.19-.06-1.78C8.18 5.31 8.68 2.45 5.05.32L5.03.3l.02.01z" fill-rule="evenodd"></path></svg></span>éè¦æé</div><div class="admonitionContent_BuS1"><ol>
<li class=""><strong>æ³¨åä»»ä½èåçè´¦å·å¯ç ä¸æ¸¸æåçå®å¨æ å³,ééåä½ çç¬ä¸æ äºçå¥½è®°ç,ä¸å»ºè®®è´¦å·å¯ç é½è¾å¥QQå·ç­å¾å®¹æè¢«ççä¿¡æ¯</strong></li>
<li class=""><strong>æ³¨åä»»ä½èåæå¥½åªä½¿ç¨</strong> <strong><code>æ°å­ + å­æ¯ç»å</code></strong> <strong>, é¿åº¦å¨ 8 ä½ä»¥ä¸,å°¤å¶ä¸è¦è¾å¥</strong> <strong><code>ä¸­æ</code></strong> <strong><code>ç©ºæ ¼</code></strong> <strong>ä¸</strong> <strong><code>ä¸­æç¬¦å·</code></strong> <strong>, ä¸æå°æ°èåä¸æ¯æ</strong> <strong><code>è±æç¬¦å·</code></strong></li>
<li class=""><strong>è¯·èªè¡ä¿ç®¡å¥½ææç¸å³ç æ¿æ´»ç /å¡å¯/è´¦å·ä¿¡æ¯,è¯·å¿æ³é²,é¨åèåæ²¡ææ¾åå¯ç æå¡,ä¸æ¬åºæ²¡ææä¾ç¸å³ä»£ç®¡ä¸å¡çä¹å¡ (æå­/åªæ¯ç»å¤§å®¶çç¦å©,è¯·ä¸è¦ä¾èµæ­¤æå¡),ä¸¢å¤±ç¸å³æ°æ®å¯¼è´çä»»ä½åæèªè¡æ¿æ</strong></li>
<li class=""><strong>æ³¨åæ¿æ´»å,ä½ è´¦æ·çè§£éæå½æ­¤è½¯ä»¶å¼åå¢éææ,ä¸ææ å³,è¯·ä¸¥æ ¼éµå®è§å (é¨åéè¦æå¸®å¿å¤ççæ¯å¦æ´æ¢æºå¨ç ,å±äºéå ç¦å©çä¸ç§,å æ¬åºå±äºä»£è´­æ§è´¨,è¯·å°½éèªå©å®æ),è¿åè½¯ä»¶è§åå¯¼è´çä»»ä½åæèªè¡æ¿æ (å¦ç»å¤§é¨åèåç¦æ­¢åäº«/äºæå¤çè´¦æ·)</strong></li>
</ol></div></div>
<p><strong>ä¸è½½å<span class="text-blue"><code>é¼ æ å³é®</code></span>ä»¥<span class="text-blue"><code>ç®¡çåè¿è¡</code></span>æ³¨å¥å¨</strong></p>
<div style="text-align:center"><p><img alt="" class="img_ev3q" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/item/69805c76bb6a79a9e97a5721.png"/></p></div>
<blockquote>
<p><strong>EACï¼Rust/APEX</strong><br/>
<strong>BEï¼R6/EFT/ARK/DayZ</strong></p>
</blockquote>
<p><strong>ä¸è½½å<span class="text-blue"><code>é¼ æ å³é®</code></span>ä»¥<span class="text-blue"><code>ç®¡çåè¿è¡</code></span>æ³¨å¥å¨</strong></p>
<p><strong>ç¹å»</strong> <strong><span class="text-blue"><code>Authenticate</code></span>éªè¯æ¿æ´»ç </strong></p>
<div class="theme-admonition theme-admonition-danger admonition_xJq3 alert alert--danger"><div class="admonitionHeading_Gvgb"><span class="admonitionIcon_Rf37"><svg viewbox="0 0 12 16"><path d="M5.05.31c.81 2.17.41 3.38-.52 4.31C3.55 5.67 1.98 6.45.9 7.98c-1.45 2.05-1.7 6.53 3.53 7.7-2.2-1.16-2.67-4.52-.3-6.61-.61 2.03.53 3.33 1.94 2.86 1.39-.47 2.3.53 2.27 1.67-.02.78-.31 1.44-1.13 1.81 3.42-.59 4.78-3.42 4.78-5.56 0-2.84-2.53-3.22-1.25-5.61-1.52.13-2.03 1.13-1.89 2.75.09 1.08-1.02 1.8-1.86 1.33-.67-.41-.66-1.19-.06-1.78C8.18 5.31 8.68 2.45 5.05.32L5.03.3l.02.01z" fill-rule="evenodd"></path></svg></span>éè¦æé</div><div class="admonitionContent_BuS1"><ul>
<li class=""><strong>è¯·</strong> <strong><code>ä¿ç®¡å¤ä»½å¥½</code></strong> <strong>èªå·±ç</strong> <strong><code>æ¿æ´»ç </code></strong> <strong>ä»¥å</strong> <strong><code>è´¦æ·ä¿¡æ¯</code></strong> <strong>,ä¸¢å¤±ä¹åæ æ³æ¾å!!æä»¬ä¸æä¾ä»»ä½å¸æ·ä¿ç®¡æå¡!</strong></li>
<li class=""><strong>åç»­ç½ç«ä¹ä¸ä¼å¸®å¤ä»½ä½ çæ¿æ´»ç ä¿¡æ¯,è¯·ä½ èªè¡</strong> <strong><code>ä¿å­</code></strong> <strong>!</strong></li>
<li class=""><strong>æ³¨åæ¿æ´»ä¹å,è¯¥è´¦æ·ä¸æä»¬åæ å³è,ææçè´¦æ·ä¿¡æ¯,åç±ä½ ä¸ªäººåç¬è¿è¡ç»´æ¤åä½¿ç¨,è¯·èªè§éµå®åä¸ªèåè§å!</strong></li>
</ul></div></div>
<div style="text-align:center"><p><img alt="" class="img_ev3q" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/item/69805c77bb6a79a9e97a5723.png"/></p></div>
<p><strong>ç¹å»</strong> <strong><span class="text-blue"><code>Launch</code></span>å è½½æ³¨å¥å¨</strong></p>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id="injection"><strong>æ³¨å¥</strong><a aria-label="injectionçç´æ¥é¾æ¥" class="hash-link" href="#injection" title="injectionçç´æ¥é¾æ¥" translate="no">â</a></h2>
<p><strong>å è½½å®æå</strong> <strong><span class="text-blue"><code>å³é®-ä»¥ç®¡çåèº«ä»½è¿è¡</code></span></strong> <strong>æ³¨å¥å¨</strong></p>
<div style="text-align:center"><p><img alt="" class="img_ev3q" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/item/69805c77bb6a79a9e97a5722.png"/></p></div>
<p><strong>è¯·èå¿ç­å¾å è½½</strong></p>
<div style="text-align:center"><p><img alt="" class="img_ev3q" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/item/69805c77bb6a79a9e97a5724.png"/></p></div>
<div style="text-align:center"><p><img alt="" class="img_ev3q" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/item/69805c77bb6a79a9e97a5725.png"/></p></div>
<p><strong>ç­å°</strong> <strong><span class="text-blue"><code>æ³¨å¥å¨ä¸è½½å®æèªå¨å³é­å</code></span></strong> <strong>è¿å¥</strong> <strong><span class="text-blue"><code>æ¸¸æ</code></span>å³å¯</strong></p>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id="shortcut-key"><strong>ä½¿ç¨</strong><a aria-label="shortcut-keyçç´æ¥é¾æ¥" class="hash-link" href="#shortcut-key" title="shortcut-keyçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div class="theme-tabs-container tabs-container tabList__CuJ"><ul aria-orientation="horizontal" class="tabs" role="tablist"><li aria-selected="true" class="tabs__item tabItem_LNqP tabs__item--active" role="tab" tabindex="0">é¼ æ æä½</li></ul><div class="margin-top--md"><div class="tabItem_Ymn6" role="tabpanel"><p><strong><code>INS</code> å¼åº/éèèå</strong></p><p><strong><code>é¼ æ ç¹å»</code> æçºµèå</strong></p></div></div></div></div></article>