---
sidebar_position: 1
title: éè¦å¯ç¨ JavaScript
slug: /game/cod/ca/use
---

<article><div class="theme-doc-markdown markdown"><header><h1>CA ä½¿ç¨æç¨</h1></header>
<p><strong><span class="text-grey">CA èåæ³¨åãä¸è½½åä½¿ç¨è¯¦ç»æç¨</span></strong></p>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="preface"><strong>åè¨</strong><a aria-label="prefaceçç´æ¥é¾æ¥" class="hash-link" href="#preface" title="prefaceçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div class="theme-admonition theme-admonition-tip admonition_LJt0 alert alert--success"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 12 16"><path d="M6.5 0C3.48 0 1 2.19 1 5c0 .92.55 2.25 1 3 1.34 2.25 1.78 2.78 2 4v1h5v-1c.22-1.22.66-1.75 2-4 .45-.75 1-2.08 1-3 0-2.81-2.48-5-5.5-5zm3.64 7.48c-.25.44-.47.8-.67 1.11-.86 1.41-1.25 2.06-1.45 3.23-.02.05-.02.11-.02.17H5c0-.06 0-.13-.02-.17-.2-1.17-.59-1.83-1.45-3.23-.2-.31-.42-.67-.67-1.11C2.44 6.78 2 5.65 2 5c0-2.2 2.02-4 4.5-4 1.22 0 2.36.42 3.22 1.19C10.55 2.94 11 3.94 11 5c0 .66-.44 1.78-.86 2.48zM4 14h5c-.23 1.14-1.3 2-2.5 2s-2.27-.86-2.5-2z" fill-rule="evenodd"></path></svg></span>æ¸©é¦¨æç¤º</div><div class="admonitionContent__XZN"><ul>
<li class=""><strong>ä¿å­å¥½èªå·±çæ¿æ´»ç è·æ³¨åçè´¦å·å¯ç , è¥ä¸¢å¤±æ æ³æ¾ååæèªè´</strong></li>
<li class=""><strong>æ¬æç¨ä»åæ­£å¸¸æ­¥éª¤æ¼ç¤º, æ ¹æ®æç¨æä½åºç°é®é¢ä¼åèç³»ä½ çåå®¶è§£å³</strong></li>
<li class=""><strong>è¯·ä»ç»éè¯»ææåå®¹ä¸æç¤º,éå°é®é¢å°è¯åèªå·±è§£å³ (å¦åå© AI å·¥å·)</strong></li>
<li class=""><strong>æç¨å¯è½å·ææ¶ææ§,è¥ä¸éç¨è¯·åæ¶èç³»æ</strong></li>
</ul></div></div>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="detection"><strong>ç¡¬ä»¶æ£æµ</strong><a aria-label="detectionçç´æ¥é¾æ¥" class="hash-link" href="#detection" title="detectionçç´æ¥é¾æ¥" translate="no">â</a></h2>
<p><strong>ä»¥ä¸æ­¥éª¤æ¯å¨ä¸è¿è¡å¤ææä½/éè£çåæä¸å¯¹ä½ çç¡¬ä»¶åç³»ç»è¯ä¼°çæ¹æ¡,å¦ä¸æ»¡è¶³å¯éæ©æ¾å¼ææå¨è§£å³</strong></p>
<p><strong>1.æä¸ <span class="text-blue"><code>win+r</code></span> å¹¶è¾å¥ <span class="text-blue"><code>winver</code></span> åè½¦,ä»¥ä¸æ¯å¯ç¨ç³»ç»<!-- -->:Win<!-- --> 10 ä» 22H2 / Win 11 22H2 åä»¥ä¸ (å¦ä¸æ¯,ç¹å«æ³ç©çå¯æ³åæ³éè£ç³»ç»,æ U çå°±å¯ä»¥è½»æ¾æå®)</strong></p>
<div style="text-align:center"><p><img alt="" class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tPF4mcSDNuiQm9iutmn.png"/><p><img alt="" class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tPUyWqW4u3gmyYCAFgo.png"/></p></p></div>
<p><strong>2.ç¡®ä¿ <span class="text-blue"><code>BIOS</code></span> ä¸º <span class="text-blue"><code>UEFI</code></span> æ¨¡å¼,é¼ æ ç§»è³<span class="text-blue"><code>ä¸æ¹ä»£ç åå³ä¾§</code></span> ,ç¹å» <span class="text-blue"><code>å¤å¶å°åªè´´æ¿</code></span></strong></p>
<div class="language-powershell codeBlockContainer_Y94m theme-code-block" style="--prism-color:#393A34;--prism-background-color:#f6f8fa"><div class="codeBlockContent_IRmN"><pre class="prism-code language-powershell codeBlock_rbdZ thin-scrollbar" style="color:#393A34;background-color:#f6f8fa" tabindex="0"><code class="codeBlockLines_bJRA"><div class="token-line" style="color:#393A34"><span class="token plain">$env:firmware_type</span><br/></div></code></pre></div></div>
<p><strong>å³é® ç¹å»å±å¹å·¦ä¸è§ Windows å¼å§èå - ç¹å» <span class="text-blue"><code>ç»ç«¯ç®¡çå(Windows PowerShell [ç®¡çå])</code></span>,å³é®ç¹å»é»è²çªå£ - åæä¸åè½¦,ç¡®ä¿ä¸º UEFI (å¦ä¸æ¯,å¯éè£ç³»ç»æä½¿ç¨å·¥å·è½¬,å¯åè è¿é (å»ºè®®æä¸ª U ç + å¤ä»½å¥½éè¦æ°æ®)</strong></p>
<div style="text-align:center"><p><img alt="" class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tPV3UOX1qD8Xp1Eq0d4.png"/><p><img alt="" class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tPUBnvyS0hqRfynrMQj.jpg"/></p></p></div>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="status"><strong>èåç¶æ</strong><a aria-label="statusçç´æ¥é¾æ¥" class="hash-link" href="#status" title="statusçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div class="custom-link-card-container"><ul>
<li class=""><a class="" href="https://guide.maoruanx.com/home/state" rel="noopener noreferrer" target="_blank">ðèåç¶æ</a></li>
</ul></div>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="condition"><strong>å¿å¤ç¯å¢</strong><a aria-label="conditionçç´æ¥é¾æ¥" class="hash-link" href="#condition" title="conditionçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div class="environment-unified"><div class="environment-unified__heading">ä½¿ç¨åæ£æ¥</div><ol>
<li class=""><strong>ç¡®ä¿å·²ç¦ç¨å®å¨å¯å¨,</strong> <a class="" href="https://guide.maoruanx.com/misc/win/bios/#disable-secure-boot" rel="noopener noreferrer" target="_blank"><strong>ç¹å»æ¥çæ¹æ³</strong></a></li>
<li class=""><a class="" href="https://guide.maoruanx.com/misc/win/systemprotection" rel="noopener noreferrer" target="_blank"><strong>å³é­ææææ¯è½¯ä»¶</strong></a> <strong>(å¦ç¡®è®¤å·²å³å¹²åè¯·æ è§) /</strong> <strong><span class="text-blue"><code>å³é­CE ç­è°è¯è½¯ä»¶</code></span></strong></li>
<li class=""><a class="" href="https://guide.maoruanx.com/misc/win/kernel" rel="noopener noreferrer" target="_blank"><strong>å³é­Windowsåæ ¸éç¦»</strong></a></li>
<li class=""><strong>å®è£</strong> <a class="" href="https://shark.lanzn.com/b0izso9af" rel="noopener noreferrer" target="_blank"><strong>è¿è¡åºåé</strong></a> <strong>(ä¸è½½ - è¿è¡ - ä¸è·¯ç»§ç»­ - èå¿ç­å¾å åéå³å¯,è¥æ¾å®è£è¿è¯·æ è§)</strong></li>
<li class=""><strong>è¿è¡ä¸æ¬¡</strong> <a class="" href="https://guide.maoruanx.com/misc/win/protection" rel="noopener noreferrer" target="_blank"><strong>æäººèæ¬</strong></a> <strong>(è¥æ¾è¿è¡è¿è¯·æ è§)</strong></li>
</ol><div class="environment-unified__foot">è¯·ä»¥æ¬é¡µè¦æ±ä¸ºåï¼ä¸åèåçå¿å¤ç¯å¢å¯è½ä¸åã</div></div>
<h3 class="anchor anchorTargetStickyNavbar_lorJ" id="drive"><strong>æ¨èé©±å¨ç¨åº</strong><a aria-label="driveçç´æ¥é¾æ¥" class="hash-link" href="#drive" title="driveçç´æ¥é¾æ¥" translate="no">â</a></h3>
<blockquote>
<p><strong>è¯·å¡å¿æ´æ°åä¸è½½ææé©±å¨ç¨åºåå¿è¦çç¨åº</strong></p>
</blockquote>
<p><strong>Microsoft Visual C++ 2005-2019</strong></p>
<div class="custom-link-card-container"><p><a class="" href="https://www.techpowerup.com/download/visual-c-redistributable-runtime-package-all-in-one/" rel="noopener noreferrer" target="_blank">Latest Visual C++ Redistributable Runtimes All-in-One Dec 2025 Download</a></p></div>
<p><strong>DXä¿®å¤</strong></p>
<div class="custom-link-card-container"><p><a class="" href="https://shark.lanzn.com/b0izspeub" rel="noopener noreferrer" target="_blank">DXä¿®å¤å·¥å·</a></p></div>
<p><strong>Microsoft ç½ç»æ¡æ¶ 4.7.1</strong></p>
<div class="custom-link-card-container"><p><a class="" href="https://dotnet.microsoft.com/zh-cn/download/dotnet-framework/net471" rel="noopener noreferrer" target="_blank">ä¸è½½ .NET Framework 4.7.1  | .NET</a></p></div>
<div style="text-align:center"><p><img alt="" class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tOt3fPnf7m5U8swiuxS.png"/></p></div>
<p><strong>é©±å¨ç¨åºå</strong></p>
<div class="custom-link-card-container"><p><a class="" href="https://driverpack.io/zh-cn" rel="noopener noreferrer" target="_blank">DriverPack - é©±å¨æ´æ°è½¯ä»¶| ä¸è½½éç¨äº Windows 7,XP,10,8 å 8.1</a><p><strong>å®è£ææé©±å¨ç¨åº</strong></p></p></div>
<div style="text-align:center"><p><img alt="" class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tP29xiAOF305HMuDmbI.png"/></p></div>
<p><strong>è±ä¼è¾¾</strong></p>
<div class="custom-link-card-container"><p><a class="" href="https://www.nvidia.ru/Download/index.aspx?lang=ru" rel="noopener noreferrer" target="_blank">Official NVIDIA Drivers</a></p></div>
<p><strong>AMD</strong></p>
<div class="custom-link-card-container"><p><a class="" href="https://www.amd.com/en/support/download/drivers.html" rel="noopener noreferrer" target="_blank">AMD - Downlad</a></p></div>
<h3 class="anchor anchorTargetStickyNavbar_lorJ" id="antivirus"><strong>ç¦ç¨çµèé²æ¤/ææ¯</strong><a aria-label="antivirusçç´æ¥é¾æ¥" class="hash-link" href="#antivirus" title="antivirusçç´æ¥é¾æ¥" translate="no">â</a></h3>
<blockquote>
<p><strong>èªå¨å³é­ Windows æºè½å±å¹</strong><br/>
<strong>Windows Defender ç®¡ç</strong><br/>
<strong>èªå¨ç¦ç¨UACå¸æ·</strong></p>
</blockquote>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="download"><strong>ä¸è½½</strong><a aria-label="downloadçç´æ¥é¾æ¥" class="hash-link" href="#download" title="downloadçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div class="theme-admonition theme-admonition-info admonition_LJt0 alert alert--info"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 14 16"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z" fill-rule="evenodd"></path></svg></span>å°è´´å£«</div><div class="admonitionContent__XZN"><p><strong>æ°¸è¿å»æä¸ä¸ªå¥½ä¹ æ¯:ä¸è½½ä»»ä½ç¨åºä¸è¦ä¸å°å« ä¸­æ/ä¸­æç¬¦å·/å¥æªå­ç¬¦ çæä»¶å¤¹ä¸­,è¿å¯è½å¯¼è´é¨åç¨åºè¿è¡ä¸äº;å¹¶å»ºè®®å°åä¸ªç¨åº/åç¼©åæ¾å¥åç¬çæä»¶å¤¹ä¸­,é²æ­¢é¨åç¨åºéæ¾åºå¾å¤é²ææä»¶æè§£ååºå¤ªå¤æä»¶å½±åæ´æ´åº¦</strong></p></div></div>
<!-- -->
<div class="theme-tabs-container tabs-container tabList_TYeX"><ul aria-orientation="horizontal" class="tabs" role="tablist"><li aria-selected="true" class="tabs__item tabItem_v163 tabs__item--active" role="tab" tabindex="0">ç½çä¸è½½<li aria-selected="false" class="tabs__item tabItem_v163" role="tab" tabindex="-1">å®ç½ä¸è½½</li></li></ul><div class="margin-top--md"><div class="tabItem_xKIf" role="tabpanel"><div class="theme-admonition theme-admonition-info admonition_LJt0 alert alert--info"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 14 16"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z" fill-rule="evenodd"></path></svg></span>ç¹å»ä¸æ¹æ ç­¾æ¥çæ´å¤åå®¹</div></div><div class="custom-link-card-container"><p><a class="" href="https://shark.lanzouu.com/b0izt7ctg" rel="noopener noreferrer" target="_blank">CrookedArmä¸¨CA-å¯å¨å¨</a></p></div></div><div class="tabItem_xKIf" hidden="" role="tabpanel"><div class="theme-admonition theme-admonition-info admonition_LJt0 alert alert--info"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 14 16"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z" fill-rule="evenodd"></path></svg></span>ç¹å»ä¸æ¹æ ç­¾æ¥çæ´å¤åå®¹</div></div><div class="custom-link-card-container"><p><a class="" href="https://crooked-arms.com/applications/core/interface/file/attachment.php?id=2148&amp;key=53f167195ff8cd96048f951501170815" rel="noopener noreferrer" target="_blank">CA - Downlaoa</a></p></div></div></div></div>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="register"><strong>æ³¨å</strong><a aria-label="registerçç´æ¥é¾æ¥" class="hash-link" href="#register" title="registerçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div class="theme-admonition theme-admonition-danger admonition_LJt0 alert alert--danger"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 12 16"><path d="M5.05.31c.81 2.17.41 3.38-.52 4.31C3.55 5.67 1.98 6.45.9 7.98c-1.45 2.05-1.7 6.53 3.53 7.7-2.2-1.16-2.67-4.52-.3-6.61-.61 2.03.53 3.33 1.94 2.86 1.39-.47 2.3.53 2.27 1.67-.02.78-.31 1.44-1.13 1.81 3.42-.59 4.78-3.42 4.78-5.56 0-2.84-2.53-3.22-1.25-5.61-1.52.13-2.03 1.13-1.89 2.75.09 1.08-1.02 1.8-1.86 1.33-.67-.41-.66-1.19-.06-1.78C8.18 5.31 8.68 2.45 5.05.32L5.03.3l.02.01z" fill-rule="evenodd"></path></svg></span>éè¦æé</div><div class="admonitionContent__XZN"><ol>
<li class=""><strong>æ³¨åä»»ä½èåçè´¦å·å¯ç ä¸æ¸¸æåçå®å¨æ å³,ééåä½ çç¬ä¸æ äºçå¥½è®°ç,ä¸å»ºè®®è´¦å·å¯ç é½è¾å¥QQå·ç­å¾å®¹æè¢«ççä¿¡æ¯</strong></li>
<li class=""><strong>æ³¨åä»»ä½èåæå¥½åªä½¿ç¨</strong> <strong><code>æ°å­ + å­æ¯ç»å</code></strong> <strong>, é¿åº¦å¨ 8 ä½ä»¥ä¸,å°¤å¶ä¸è¦è¾å¥</strong> <strong><code>ä¸­æ</code></strong> <strong><code>ç©ºæ ¼</code></strong> <strong>ä¸</strong> <strong><code>ä¸­æç¬¦å·</code></strong> <strong>, ä¸æå°æ°èåä¸æ¯æ</strong> <strong><code>è±æç¬¦å·</code></strong></li>
<li class=""><strong>è¯·èªè¡ä¿ç®¡å¥½ææç¸å³ç æ¿æ´»ç /å¡å¯/è´¦å·ä¿¡æ¯,è¯·å¿æ³é²,é¨åèåæ²¡ææ¾åå¯ç æå¡,ä¸æ¬åºæ²¡ææä¾ç¸å³ä»£ç®¡ä¸å¡çä¹å¡ (æå­/åªæ¯ç»å¤§å®¶çç¦å©,è¯·ä¸è¦ä¾èµæ­¤æå¡),ä¸¢å¤±ç¸å³æ°æ®å¯¼è´çä»»ä½åæèªè¡æ¿æ</strong></li>
<li class=""><strong>æ³¨åæ¿æ´»å,ä½ è´¦æ·çè§£éæå½æ­¤è½¯ä»¶å¼åå¢éææ,ä¸ææ å³,è¯·ä¸¥æ ¼éµå®è§å (é¨åéè¦æå¸®å¿å¤ççæ¯å¦æ´æ¢æºå¨ç ,å±äºéå ç¦å©çä¸ç§,å æ¬åºå±äºä»£è´­æ§è´¨,è¯·å°½éèªå©å®æ),è¿åè½¯ä»¶è§åå¯¼è´çä»»ä½åæèªè¡æ¿æ (å¦ç»å¤§é¨åèåç¦æ­¢åäº«/äºæå¤çè´¦æ·)</strong></li>
</ol></div></div>
<p><strong>ä¸è½½å<span class="text-blue"><code>é¼ æ å³é®</code></span>ä»¥<span class="text-blue"><code>ç®¡çåè¿è¡</code></span>æ³¨å¥å¨</strong></p>
<blockquote>
<p><strong>é¦æ¬¡æå¼å¯è½éè¦æ´æ°,ç­å¾æ´æ°å³å¯</strong></p>
</blockquote>
<div style="text-align:center"><p><img class="img_i2Xa" decoding="async" height="253" loading="lazy" src="/assets/images/1-76a69b01dec2846f79cc44266f49dd76.avif" width="582"/></p></div>
<div style="text-align:center"><p><img alt="" class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tP5UdrKSz7Ic3J6Lh3i.jpg"/></p></div>
<blockquote>
<p><strong>æ³¨åæååæ¯ç´æ¥å¸®ä½ ç»å½å¥½ç,æ ééå¤ç»å½</strong></p>
</blockquote>
<div class="theme-admonition theme-admonition-danger admonition_LJt0 alert alert--danger"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 12 16"><path d="M5.05.31c.81 2.17.41 3.38-.52 4.31C3.55 5.67 1.98 6.45.9 7.98c-1.45 2.05-1.7 6.53 3.53 7.7-2.2-1.16-2.67-4.52-.3-6.61-.61 2.03.53 3.33 1.94 2.86 1.39-.47 2.3.53 2.27 1.67-.02.78-.31 1.44-1.13 1.81 3.42-.59 4.78-3.42 4.78-5.56 0-2.84-2.53-3.22-1.25-5.61-1.52.13-2.03 1.13-1.89 2.75.09 1.08-1.02 1.8-1.86 1.33-.67-.41-.66-1.19-.06-1.78C8.18 5.31 8.68 2.45 5.05.32L5.03.3l.02.01z" fill-rule="evenodd"></path></svg></span>éè¦æé</div><div class="admonitionContent__XZN"><ul>
<li class=""><strong>è¯·</strong> <strong><code>ä¿ç®¡å¤ä»½å¥½</code></strong> <strong>èªå·±ç</strong> <strong><code>æ¿æ´»ç </code></strong> <strong>ä»¥å</strong> <strong><code>è´¦æ·ä¿¡æ¯</code></strong> <strong>,ä¸¢å¤±ä¹åæ æ³æ¾å!!æä»¬ä¸æä¾ä»»ä½å¸æ·ä¿ç®¡æå¡!</strong></li>
<li class=""><strong>åç»­ç½ç«ä¹ä¸ä¼å¸®å¤ä»½ä½ çæ¿æ´»ç ä¿¡æ¯,è¯·ä½ èªè¡</strong> <strong><code>ä¿å­</code></strong> <strong>!</strong></li>
<li class=""><strong>æ³¨åæ¿æ´»ä¹å,è¯¥è´¦æ·ä¸æä»¬åæ å³è,ææçè´¦æ·ä¿¡æ¯,åç±ä½ ä¸ªäººåç¬è¿è¡ç»´æ¤åä½¿ç¨,è¯·èªè§éµå®åä¸ªèåè§å!</strong></li>
</ul></div></div>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="subscription"><strong>æ¿æ´»</strong><a aria-label="subscriptionçç´æ¥é¾æ¥" class="hash-link" href="#subscription" title="subscriptionçç´æ¥é¾æ¥" translate="no">â</a></h2>
<p><strong>é¼ æ å¾</strong> <strong><span class="text-blue"><code>æ³¨å¥å¨å·¦æ»</code></span></strong> <strong>,ç¶åç¹å»</strong> <strong><span class="text-blue"><code>èªå·±çIDè¿è¡æ¿æ´»</code></span></strong></p>
<div style="text-align:center"><p><img class="img_i2Xa" decoding="async" height="457" loading="lazy" src="/assets/images/2-e8920b0723268732d2419a3cab6671c5.avif" width="716"/></p></div>
<div style="text-align:center"><p><img alt="" class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tP1WfOJWb5RbzdqICN0.png"/></p></div>
<hr/>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="injection"><strong>æ³¨å¥</strong><a aria-label="injectionçç´æ¥é¾æ¥" class="hash-link" href="#injection" title="injectionçç´æ¥é¾æ¥" translate="no">â</a></h2>
<p><strong>æ¿æ´»æååä½ ç</strong> <strong><span class="text-blue"><code>æ³¨å¥å¨æ¸¸æé¡µé¢å³ä¸è§</code></span></strong> <strong>ç</strong> <strong><span class="text-blue"><code>Buy</code></span>ä¼åæ<span class="text-blue"><code>Launched</code></span></strong></p>
<p><strong>ç¹å»</strong> <strong><span class="text-blue"><code>Launched</code></span></strong> <strong>æ³¨å¥,ç¶åç­å¾æ³¨å¥å¨ä¸æ¹åºç°</strong> <strong><span class="text-blue"><code>Successfully launched</code></span>ä»£è¡¨æ³¨å¥æå</strong></p>
<div class="theme-admonition theme-admonition-warning admonition_LJt0 alert alert--warning"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 16 16"><path d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z" fill-rule="evenodd"></path></svg></span><code>Successfully launched</code> åºç°åªä¼å­å¨2ç§é,è¯·èªè¡çæ</div></div>
<p><strong>åªéè¦</strong> <strong><span class="text-blue"><code>å³é­æ³¨å¥å¨</code></span></strong> <strong>å,ç¶åè¿å¥æ¸¸æå³å¯ï¼</strong></p>
<div class="theme-admonition theme-admonition-warning admonition_LJt0 alert alert--warning"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 16 16"><path d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z" fill-rule="evenodd"></path></svg></span>å¦æä½ éè¦ä½¿ç¨<code>æ è¾¹æ¡</code>æ¸¸æ,éè¦æå¼<code>æ­è¯æ¬æµ®</code>,æ¯å¦<code>é·ç</code>/<code>å±å¹é®ç</code>ç­,<code>æå°ä½ çä¸å°çå°æ¹å³å¯</code></div></div>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="fqa"><strong>å¦è¥æ³¨å¥å¤±è´¥</strong><a aria-label="fqaçç´æ¥é¾æ¥" class="hash-link" href="#fqa" title="fqaçç´æ¥é¾æ¥" translate="no">â</a></h2>
<blockquote>
<p><strong>æ¥çä»¥ä¸æç¨,æ³¨å¥æåæ è§æ­¤æ¡.</strong></p>
</blockquote>
<div class="custom-link-card-container"><p><a class="" href="https://guide.maoruanx.com/injecterror" rel="noopener noreferrer" target="_blank">â ï¸ æ³¨å¥å¤±è´¥ææ¸¸æéªéè§£å³</a></p></div>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="shortcut-key"><strong>ä½¿ç¨</strong><a aria-label="shortcut-keyçç´æ¥é¾æ¥" class="hash-link" href="#shortcut-key" title="shortcut-keyçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div class="theme-tabs-container tabs-container tabList_TYeX"><ul aria-orientation="horizontal" class="tabs" role="tablist"><li aria-selected="true" class="tabs__item tabItem_v163 tabs__item--active" role="tab" tabindex="0">é¼ æ æä½</li></ul><div class="margin-top--md"><div class="tabItem_xKIf" role="tabpanel"><p><strong><code>HOME/INS</code> å¼åº/éèèå</strong><p><strong><code>é¼ æ ç¹å»</code> æçºµèå</strong></p></p></div></div></div></div></article>